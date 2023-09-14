from odoo import fields, models


class GuruProductLog(models.Model):
    _name = 'guru.product.log'  # table: guru_product_log
    _description = 'Log de Estados de Producto'

    model = fields.Char(
        required=True,
        string='Modelo de documento relacionado'
    )
    res_id = fields.Integer(
        required=True,
        string='ID del documento relacionado'
    )
    user_id = fields.Many2one(
        'res.users',
        string='Usuario',
        default=lambda self: self.env.user.id
    )
    initial_state = fields.Char(string='Estado inicial')
    final_state = fields.Char(string='Estado final')
    date = fields.Datetime(string='Fecha de Cambio')
    message = fields.Char(string='Mensaje')
    technical_message = fields.Text(string='Mensaje técnico')

    def save(self, model, res_id, initial_state, final_state, message, technical_message=''):
        res = self.create({
            'model': model,
            'res_id': res_id,
            'initial_state': initial_state,
            'final_state': final_state,
            'message': message,
            'technical_message': technical_message,
            'date': fields.Datetime.context_timestamp(self, fields.Datetime.now()),
        })
        return res
