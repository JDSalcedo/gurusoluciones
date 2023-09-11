from odoo import fields, models

from .constants import (
    PENDING,
    READY,
    BAJA
)


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
        [(PENDING, 'Pendiente'), (READY, 'Listo'), (BAJA, 'De Baja')],
        default=PENDING,
        string='Estado',
        required=True
    )
    airplane_ids = fields.One2many(
        comodel_name='guru.airplane',
        inverse_name='airline_id',
        string='Aeroplanos'
    )

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
