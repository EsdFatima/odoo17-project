from odoo import models, fields

class SportSession(models.Model):
    _name = 'sport.session'
    _description = 'Sport Session'

    name = fields.Char(string='Session Name', required=True)
    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    activity_id = fields.Many2one('sport.activity', string='Activity')
    trainer_id = fields.Many2one('res.partner', string='Trainer')
    participant_ids = fields.Many2many('res.partner', string='Participants')
