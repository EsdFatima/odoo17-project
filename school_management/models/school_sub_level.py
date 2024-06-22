from odoo import models, fields

class SchoolYear(models.Model):
    _name = 'school.sub.level'
    _description = 'Sous-niveau scolaire'

    name = fields.Char(string='Sous-niveau', required=True)
    level_id = fields.Many2one('school.level',string='Niveau', required=True)

