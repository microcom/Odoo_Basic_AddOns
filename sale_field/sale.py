# coding: utf-8
from openerp import models, fields, api


class sale_order_line(models.Model):
    _inherit = "sale.order.line"

    @api.one
    def _compute_line_bidou(self):
        self.line_bidou = self.product_uos_qty * self.price_unit

    line_bidou = fields.Integer('Bidou', compute=_compute_line_bidou)


class sale_order(models.Model):
    _inherit = "sale.order"

    @api.one
    def _compute_bidou(self):
        bidou = 0
        for line in self.order_line:
            bidou += line.line_bidou
        self.bidou = bidou

    bidou = fields.Integer('Bidou total', compute=_compute_bidou)
