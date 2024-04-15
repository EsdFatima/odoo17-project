from odoo import models, fields

class SportActivity(models.Model):
    _name = 'sport.activity'
    _description = 'Sport Activity'

    name = fields.Char(string='Activity Name', required=True)
    description = fields.Text(string='Description')