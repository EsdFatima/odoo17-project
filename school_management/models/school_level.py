from odoo import models, fields

class SchoolYear(models.Model):
    _name = 'school.level'
    _description = 'Les Niveaux Scolaires'

    name = fields.Char(string='Nom du niveau', required=True)

