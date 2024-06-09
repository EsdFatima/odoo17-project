from odoo import models, fields, api

class Commune(models.Model):
    _name = 'commune'
    _description = 'Commune'

    name = fields.Char(string='Name')
    code_postal = fields.Char(string='Code Postal')
    state_id = fields.Many2one('state', string='State')
