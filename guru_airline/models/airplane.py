import re

from odoo import api, fields, models
from odoo.exceptions import UserError

from .constants import (
    READY,
    BAJA,
    RE_PHONE
)


class AirPlane(models.Model):
    _name = 'guru.airplane'
    _description = 'Tabla para registro de flota aérea'

    name = fields.Char(required=True, string='Nombre')
    type = fields.Selection([
        ('carga', 'Carga'),
        ('comercial', 'Comercial'),
        ('militar', 'Militar')
    ], string='Tipo', required=True)
    capacity = fields.Integer(string='Capacidad', required=True)
    engine_qty = fields.Integer(string='Cant. Motores', required=True)
    state = fields.Selection(
        [(READY, 'Listo'), (BAJA, 'De Baja')],
        default=READY,
        string='Estado',
        required=True
    )
    active = fields.Boolean(default=True, string='Activo')
    airline_id = fields.Many2one(
        'guru.airline',
        string='Aerolínea',
        domain=[('state', '=', READY)],
        required=True,
        ondelete='restrict'
        # ondelete='set null'
        # ondelete = 'cascade'
    )
    country_id = fields.Many2one(related='airline_id.country_id')
    # country_id = fields.Many2one(related='airline_id.country_id', store=True)  es para tenerlo almacenado en la tabla
    phone = fields.Char(compute='_compute_phone', string='Teléfono', store=True)
    zip = fields.Char(string='Zip', size=7)

    _sql_constraints = [
        ('unique_name_airline', 'unique(name, airline_id)', 'El nombre del aeroplano debe ser único por aerolínea'),
        ('check_engine_qty', 'CHECK(engine_qty > 0)', 'La Cantidad de Motores debe ser mayor a cero')
    ]

    @api.constrains('capacity')
    def _check_capacity(self):
        for record in self:
            if record.capacity < 1:
                raise UserError('La capacidad no puede ser menor a cero')

    @api.depends('airline_id')
    def _compute_phone(self):
        for record in self:
            record.phone = record.airline_id.phone

    @api.onchange('airline_id')
    def _onchange_zip(self):
        if not self.zip:
            self.zip = self.airline_id.zip

    @api.onchange('phone')
    def _onchange_phone(self):
        if self.phone:
            if not re.match(RE_PHONE, self.phone):
                # raise UserError('No es un teléfono válido')
                return {
                    'warning': {'title': 'Error', 'message': 'Teléfono inválido'},
                    # 'value':{'phone': False}
                    'value': {'phone': self._origin.phone}  # self.origin es el objeto antes de corregir
                }
