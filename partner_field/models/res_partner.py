# coding: utf-8
from openerp import fields, models

COLORS = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
]


class ResPartner(models.Model):
    _inherit = "res.partner"

    favorite_color = fields.Selection(COLORS, 'Favorite Color', default='blue')
