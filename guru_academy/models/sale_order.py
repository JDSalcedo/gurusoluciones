from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_gift = fields.Boolean(string='Es regalo')
