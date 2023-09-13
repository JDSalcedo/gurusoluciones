from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    airline_id = fields.Many2one('guru.airline', string='Aerolínea')
    airplane_id = fields.Many2one('guru.airplane', string='Aeroplano')

    @api.onchange('airline_id')
    def _onchange_airline_id(self):
        # validation
        return {
            # 'warning': {'title': 'Error', 'message': 'Mensaje de Error'},
            'value': {'airplane_id': False},
            # 'domain': {'airplane_id': [('airline_id', '=', self.airline_id.id)]}
        }
