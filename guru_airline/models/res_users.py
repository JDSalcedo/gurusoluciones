from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    airline_ids = fields.Many2many(
        comodel_name='guru.airline',
        relation='guru_airline_res_users_no_rel',
        column1='user_id',
        column2='airplane_id',
        string='Aerolíneas NO Permitidas'
    )
