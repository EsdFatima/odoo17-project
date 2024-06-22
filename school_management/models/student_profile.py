from odoo import models, fields, api


class StudentProfile(models.Model):
    _name = 'student.profile'
    _description = 'Profil de l\'étudiant'

    name = fields.Char(string='Nom', required=True)
    name_ar = fields.Char(string='Nom (Arab)')
    photo = fields.Image(max_width=1920, max_height=1920)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Genre', default='male')
    reg_number_bac = fields.Char(string='Numéro d\'enregistrement BAC')
    reg_number = fields.Char(string='Numéro d\'enregistrement')
    address = fields.Char(string='Adresse')
    birth_place = fields.Char(string='Lieu de naissance')
    birthday = fields.Date(string='Date de naissance')
    birth_certification_no = fields.Char(string='Numéro Acte de Naissance')
    father_name = fields.Char(string='Le prénom du père')
    mother_lastname = fields.Char(string='Nom de famille de la mère')
    mother_name = fields.Char(string='Le prénom de la mère')
    phone = fields.Char(string='Numéro de téléphone')
    identification_no = fields.Char(string='Numéro d\'identification')
    commune_id = fields.Many2one('commune', string='Commune')
    state_id = fields.Many2one('state', string='Wilaya')
    partner_ids = fields.Many2many('res.partner', string='Personnes Autorisées')
    partner_id = fields.Many2one('res.partner', string='Contact')

    @api.model
    def create(self, vals):
        # Create a new contact in the res.partner model
        partner = self._create_or_update_partner(vals)

        # Set the partner_id field to the newly created contact
        vals['partner_id'] = partner.id

        # Create the student profile record
        return super(StudentProfile, self).create(vals)

    def write(self, vals):
        if vals:
            # Update existing contact if necessary
            self._create_or_update_partner(vals)

        # Update the student profile
        return super(StudentProfile, self).write(vals)

    def _create_or_update_partner(self, vals):

        # Find existing partner or create a new one
        partner = self.partner_id or self.env['res.partner'].create({
            'name': vals.get('name', self.name),
            'image_1920': vals.get('photo', self.photo),
            'street': vals.get('address', self.address),
            'phone': vals.get('phone', self.phone),
        })

        # Update partner information
        partner.write({
            'name': vals.get('name', self.name),
            'image_1920': vals.get('photo', self.photo),
            'street': vals.get('address', self.address),
            'phone': vals.get('phone', self.phone),
        })

        return partner
    def open_contact(self):
        partner_id = self.partner_id.ids
        return {
            'type': 'ir.actions.act_window',
            'name': 'Contact',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', partner_id)],
        }
