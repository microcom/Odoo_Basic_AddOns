# coding: utf-8
from openerp import models, fields, api


class res_partner(models.Model):
    _inherit = "res.partner"

    @api.one
    @api.onchange('test_master')
    def onchange_test(self):
        self.test_change = self.test_master

    @api.one
    @api.depends('test_master')
    def _compute_master(self):
        self.depend_master = self.test_master

    @api.one
    # @api.depends('test_change')
    def _compute_change(self):
        self.depend_change = self.test_change

    test_master = fields.Char('Master')
    test_change = fields.Char('Change')
    depend_master = fields.Char('Depend Master', compute=_compute_master)
    depend_change = fields.Char('Depend Change', compute=_compute_change)

    test_master2 = fields.Char(related='test_master')

    @api.one
    @api.onchange('test_master2')
    def onchange_two(self):
        self.test_master = self.test_master2
