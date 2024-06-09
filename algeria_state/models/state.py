from odoo import models, fields, api

class State(models.Model):
    _name = 'state'
    _description = 'State'
    _rec_name = "nom"


    nom = fields.Char(string='Nom')