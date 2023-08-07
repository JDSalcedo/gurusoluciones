from odoo import fields, models


class GuruAcademy(models.Model):
    _name = 'guru.academy'  # table: guru_academy
    _description = 'Tabla de Academias'

    name = fields.Char(string='Nombre', required=True)
    street = fields.Char(string='Dirección')
    nro = fields.Integer(string='Nro')
    horario_apertura = fields.Float(string='Horario Apertura')
    horario_cierre = fields.Float(string='Horario Cierre')
    fecha_fundacion = fields.Date(string='Fundado en')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'El nombre debe ser único.')
    ]
