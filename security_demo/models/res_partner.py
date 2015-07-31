# coding: utf-8
from openerp import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    pet_ids = fields.One2many('animal.pet', 'partner_id')


class AnimalPet(models.Model):
    _name = 'animal.pet'
    _description = 'Pet'

    name = fields.Char(string='Name')
    birthdate = fields.Date(string='Birthdate', groups='security_demo.group_animal_pet_manager')
    sex = fields.Selection([('masculin', 'Masculin'), ('feminin', 'Féminin')], string='Sex')
    partner_id = fields.Many2one('res.partner')
