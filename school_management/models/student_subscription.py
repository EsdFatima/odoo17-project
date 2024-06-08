from odoo import models, fields, api

class StudentSubscription(models.Model):
    _name = 'student.subscription'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Inscription étudiant'
    _rec_name = "student_id"

    school_year = fields.Many2one('school.year', string='Année scolaire',required=True)
    student_id = fields.Many2one('student.profile',string='Étudiant(e)')
    registration_date = fields.Date(string='Date d\'inscription')
    class_id = fields.Many2one('school.classes', string='Classe')
    sub_level_id = fields.Many2one('school.sub.level', string='Sous-niveau')
    level_id = fields.Many2one('school.level', string='Niveau')
    photo = fields.Image(related='student_id.photo', string='Photo')

    def _update_sub_level_domain(self):
        if self.level_id:
            return [('level_id', '=', self.level_id.id)]
        else:
            return []

    # Override the default domain of sub_level_id
    sub_level_id_domain = fields.Many2many(domain=_update_sub_level_domain)






