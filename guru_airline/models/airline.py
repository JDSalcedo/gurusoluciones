from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

from .constants import (
    PENDING,
    READY,
    BAJA
)


class Airline(models.Model):
    _name = 'guru.airline'  # tabla: guru_airline
    _description = 'Tabla para registro de Aerolíneas'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def default_get(self, fields):
        res = super(Airline, self).default_get(fields)
        # code
        return res

    name = fields.Char(string='Nombre', required=True)
    country_id = fields.Many2one(comodel_name='res.country', string='País', copy=False)
    street = fields.Char(string='Dirección')
    zip = fields.Char(string='Zip', size=7, default=lambda self: self._default_zip())
    phone = fields.Char(string='Teléfono')
    active = fields.Boolean(default=True, string='Activo')
    state = fields.Selection(
        [(PENDING, 'Pendiente'), (READY, 'Listo'), (BAJA, 'De Baja')],
        default=PENDING,
        string='Estado',
        required=True
    )
    airplane_ids = fields.One2many(
        comodel_name='guru.airplane',
        inverse_name='airline_id',
        string='Aeroplanos',
        copy=True
    )
    airplane_count = fields.Integer(compute='_compute_airplane_count')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'El nombre de la Aerolínea debe ser único.')
    ]

    def _default_zip(self):
        return '123'

    def action_set_baja(self):
        self.ensure_one()
        self.write({'state': BAJA})

    def action_open_wizard(self):
        """
            Se llama a una acción registrada en XML.
            Y le actualiza algunos campos.
            :return: Action
        """
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('guru_airline.guru_airline_action')
        action['domain'] = [('id', '=', self.id)]
        action['target'] = 'new'
        return action

    def action_open_archived_wizard(self):
        """
            Crea una acción nueva de forma temporal.
            :return: Action
        """
        self.ensure_one()
        # country = self.env['res.country'].search([('name', '=', 'Antártida')])
        return {
            'name': 'Aeroplanes Archivadas',
            'type': 'ir.actions.act_window',
            'res_model': 'guru.airline',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': [self.env.ref('guru_airline.guru_airline_view_form').id],
            'target': 'new',
            'res_id': self.id,
            # 'context': {
            #     'default_zip': '15080',
            #     'default_country_id': country.id,
            # },
        }

    def action_show_airplane(self):
        self.ensure_one()
        return True

    def _compute_airplane_count(self):
        for rec in self:
            rec.airplane_count = len(rec.airplane_ids)

    @api.model
    def create(self, values):
        try:
            if values['zip']:
                int(values['zip'])
        except ValueError:
            # values['zip'] = False
            # values['name'] = 'Juan'
            # values.update({'zip': False, 'name': 'Juan'})
            raise ValidationError('No es un Zip válido.')
        return super(Airline, self).create(values)
        # Uso
        # country_model = self.env['res.country']
        # country_model.create({'name': 'Aerolinea 5', 'state': PENDING})

    def write(self, vals):
        try:
            # if 'zip' in vals and vals['zip']:
            if vals.get('zip', False):
                int(vals['zip'])
        except ValueError:
            raise ValidationError('No es un Zip válido.')
        return super(Airline, self).write(vals)
        # Uso
        # country_id = self.env['res.country'].search([('code', '=', 'PE')])
        # country_id.write({'zip': '123456'})

    def unlink(self):
        country_id = self.env['res.country'].search([('code', '=', 'PE')])
        if self.env.user.country_id.id == country_id.id:
            raise UserError('Usuarios de Perú no pueden eliminar registros.')

        if self.airplane_ids:
            raise UserError('No puede eliminar registros con Aeroplanos asociados.')
        # if self.state == READY:
        #     raise UserError('No puede eliminar registros en Estado Listo.')
        return super(Airline, self).unlink()
        # Uso
        # country_id = self.env['res.country'].search([('code', '=', 'PE')])
        # country_id.unlink()

    def copy(self, default=None):
        if default is None:
            default = {}
        default['name'] = f'{self.name}_copia'
        return super(Airline, self).copy(default)
        # Uso
        # country_id = self.env['res.country'].search([('code', '=', 'PE')])
        # country_peru_id = country_id.copy(default={'code': 'PE3'})
