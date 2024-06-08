from odoo import models, fields, api

class SchoolYear(models.Model):
    _name = 'school.year'
    _description = 'Les Années scolaires'

    name = fields.Char(string='Nom', compute='_compute_name', store=True)
    start_date = fields.Date(string='Date de début', required=True)

    @api.depends('start_date')
    def _compute_name(self):
        for record in self:
            if record.start_date:
                start_year = record.start_date.year
                end_year = start_year + 1
                record.name = f"{start_year}/{end_year}"
