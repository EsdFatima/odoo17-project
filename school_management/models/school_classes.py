from odoo import models, fields

class SchoolYear(models.Model):
    _name = 'school.classes'
    _description = 'Les Classes Scolaire'

    name = fields.Char(string='Classe', required=True)
    sub_level_id = fields.Many2one('school.sub.level',string='Sous-niveau', required=True)

