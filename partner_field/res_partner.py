# coding: utf-8
from openerp import models, fields, api

COLORS = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
]


class res_partner(models.Model):
    _inherit = "res.partner"

    favorite_color = fields.Selection(COLORS, 'Favorite Color', default='blue')
