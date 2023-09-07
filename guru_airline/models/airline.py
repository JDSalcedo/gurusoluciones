from odoo import fields, models


class Airline(models.Model):
    _name = 'guru.airline'  # tabla: guru_airline
    _description = 'Tabla para registro de Aerolíneas'

    name = fields.Char(string='Nombre', required=True)
    country_id = fields.Many2one(comodel_name='res.country', string='País')
    street = fields.Char(string='Dirección')
    zip = fields.Char(string='Zip', size=7)
    phone = fields.Char(string='Teléfono')
    active = fields.Boolean(default=True, string='Activo')
    state = fields.Selection(
        [('pending', 'Pendiente'), ('ready', 'Listo'), ('baja', 'De Baja')],
        default='pending',
        string='Estado',
        required=True
    )
