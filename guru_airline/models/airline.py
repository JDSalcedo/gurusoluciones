from odoo import fields, models


class Airline(models.Model):
    _name = 'guru.airline'
    _description = 'Tabla para el registro de aerolineas'

    name = fields.Char(string='Nombre', required=True)
    country_id = fields.Many2one(comodel_name='res.country', string='País')
    street = fields.Char(string='Dirección')
    zip = fields.Char(string='Zip', size=7)
    phone = fields.Char(string='Teléfono')

