# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Bug(models.Model):
    _name = 'bugs.bug'
    _description = 'Bug'

    name = fields.Char('Name', required=True)
    description = fields.Char('Description', required=True)
    priority = fields.Many2one('bugs.priority', 'Priority', required=True,
                                       default=lambda self: self.env['ir.model.data'].xmlid_to_res_id('bugs.bug_priority_low'))
    state = fields.Many2one('bugs.state', 'State', required=True,
        default=lambda self: self.env['ir.model.data'].xmlid_to_res_id('bugs.state_new'))
    detection_date = fields.Date('Detection date', default=lambda self: fields.Datetime.now())
    estimated_time = fields.Integer('Estimated time (H)')
    color = fields.Char('Color', related='priority.color')


class Priority(models.Model):
    _name = "bugs.priority"

    name = fields.Char('Priority', required=True)
    color = fields.Char('Color')

class State(models.Model):
    _name = "bugs.state"
    _order = 'sequence'

    name = fields.Char('Name')
    sequence = fields.Integer('Sequence')