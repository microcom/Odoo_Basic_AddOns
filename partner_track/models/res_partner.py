# coding: utf-8
from openerp import api, fields, models


# noinspection PyTypeChecker,PyPep8
class ResPartner(models.Model):
    _inherit = "res.partner"

    # by default, the user creating a partner becomes a follower of those messages
    @api.model
    def create(self, values):
        # use mail_create_nosubscribe to skip the creator
        created = super(ResPartner, self.with_context(mail_create_nosubscribe=True)).create(values)
        # this line for alternate_supervisor_id case below
        created.subscribe_conditionals(values)
        return created

    # fields named 'user_id' with track_visibility set are automatically subscribed
    user_id = fields.Many2one(track_visibility='always')

    # other fields with track_visibility must be added to auto_follow_fields
    # note that hr_employee removes the need for track_visibility
    supervisor_id = fields.Many2one('res.users', 'Supervisor', track_visibility='onchange')

    @api.v7
    def _message_get_auto_subscribe_fields(self, cr, uid, updated_fields, auto_follow_fields=None, context=None):
        if auto_follow_fields is None:
            auto_follow_fields = ['user_id', 'supervisor_id']
        # noinspection PyProtectedMember
        return super(ResPartner, self)._message_get_auto_subscribe_fields(cr, uid, updated_fields, auto_follow_fields,
                                                                          context=context)

    # if subscribed under complex conditions, we must call message_subscribe() ourselves
    alternate_supervisor_id = fields.Many2one('res.users', 'Alternate')

    @api.multi
    def write(self, values):
        res = super(ResPartner, self).write(values)
        for record in self:
            # we also modified create() above
            record.subscribe_conditionals(values)
        return res

    @api.one
    def subscribe_conditionals(self, values):
        current_supervisor_id = values.get('supervisor_id', self.supervisor_id.id)
        current_alternate_id = values.get('alternate_supervisor_id', self.alternate_supervisor_id.id)
        # use new alternate if no supervisor
        if not current_supervisor_id:
            # new alternate or removed supervisor
            if 'alternate_supervisor_id' in values or 'supervisor_id' in values:
                user = self.env['res.users'].browse(current_alternate_id)
                self.message_subscribe([user.partner_id.id])
