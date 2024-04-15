from odoo import models, fields

class SportTimeSlot(models.Model):
    _name = 'sport.time.slot'
    _description = 'Sport Time Slot'

    name = fields.Char(string='Slot Name', required=True)
    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    activity_id = fields.Many2one('sport.activity', string='Activity')
    participant_id = fields.Many2one('res.partner', string='Participant')
