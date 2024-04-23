from odoo import models, fields, api
from odoo.exceptions import UserError
class SportTimeSlot(models.Model):
    _name = 'sport.time.slot'
    _description = 'Sport Time Slot'

    name = fields.Char(string='Slot Name', required=True)
    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    participant_id = fields.Many2one('res.partner', string='Participant')
    product_id = fields.Many2one('product.product', string='Product')
    sale_order_ids = fields.Many2many('sale.order', string='Sale Orders', compute='_compute_sale_order_ids', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ], string='State', default='draft')

    @api.depends('sale_order_ids')
    def _compute_sale_order_ids(self):
        for record in self:
            record.sale_order_ids = self.env['sale.order'].search([('sport_time_slot_ids', 'in', record.ids)])
    def action_confirm(self):
        for participant in self.participant_id:
            # Calculate total session hours
            total_session_hours = (self.end_time - self.start_time).total_seconds() / 3600

            # Deduct session duration from purchased hours of the participant
            participant.write({'purchased_hours': participant.purchased_hours - total_session_hours})

            if participant.purchased_hours < 0:
                raise UserError("Participant %s does not have enough purchased hours" % participant.name)

            existing_sale_order = self.env['sale.order'].search([
                ('partner_id', '=', participant.id),
                ('state', 'not in', ['cancel', 'done']),
                ('sport_time_slot_ids', 'in', self.ids),  # Filter by the current slot IDs
            ], limit=1)
            if existing_sale_order:
                # If a sale order already exists for the participant, update the existing product or add a new product
                existing_order_line = existing_sale_order.order_line.filtered(
                    lambda line: line.product_id == self.product_id)
                if existing_order_line:
                    # Update the existing product line
                    existing_order_line.write({
                        'name': self.name,
                        'product_uom_qty': total_session_hours,
                    })
                else:
                    # Add a new product line
                    existing_sale_order.write({
                        'order_line': [(0, 0, {
                            'product_id': self.product_id.id,
                            'name': self.name,
                            'product_uom_qty': total_session_hours,
                        })]
                    })
            else:
                # If no sale order exists, create a new one with the product
                sale_order = self.env['sale.order'].create({
                    'partner_id': participant.id,
                    'order_line': [(0, 0, {
                        'product_id': self.product_id.id,
                        'name': self.name,
                        'product_uom_qty': total_session_hours,
                    })],
                    'sport_time_slot_ids': [(4, self.id)],
                })
        self.write({'state': 'confirmed'})

        return True

    def open_sale_order(self):
        sale_order_ids = self.sale_order_ids.ids
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Orders',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', sale_order_ids)],
        }
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sport_time_slot_ids = fields.Many2many('sport.time.slot', string='Sport time slot')


