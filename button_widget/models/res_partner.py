# coding: utf-8
from openerp import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.onchange('increase_age')
    def _onchange_increase_age(self):
        print '********', self.increase_age
        if self.increase_age:
            self.age += 1
            self.increase_age = False

    age = fields.Integer('Age', default=9)
    increase_age = fields.Boolean('Increase')
