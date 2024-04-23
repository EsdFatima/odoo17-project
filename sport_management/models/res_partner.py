from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    purchased_hours = fields.Float(string='Purchased Hours')

