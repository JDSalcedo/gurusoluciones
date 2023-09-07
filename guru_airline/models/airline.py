from odoo import fields, models


class Airline(models.Model):
    _name = 'guru.airline'  # table: guru_airline
    _description = 'Tabla para registro de Aerolíneas'

    name = fields.Char(string='Nombre', required=True)
    country_id = fields.Many2one(comodel_name='res.country', string='País', required=True)
    street = fields.Char(string='Dirección')
    zip = fields.Char(string='Código Postal', size=7)
    phone = fields.Char(string='Teléfono')
