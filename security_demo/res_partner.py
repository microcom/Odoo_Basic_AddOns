# coding: utf-8
from openerp import models, fields

class res_partner(models.Model):
    _inherit = 'res.partner'

    pet_ids = fields.One2many('animal.pet', 'partner_id')



class animal_pet(models.Model):
    _name = 'animal.pet'
    _description = 'Pet'

    name = fields.Char(string='Name')
    birthdate = fields.Date(string='Birthdate', groups='security_demo.group_animal_pet_manager')
    partner_id = fields.Many2one('res.partner')
