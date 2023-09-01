from odoo import fields, models


class Attendance(models.Model):
    _name = 'guru.academy.attendance'
    _description = 'Tabla de registro de Asistencias de Alumnos.'

    def _default_date(self):
        return fields.Datetime.now()

    def _default_user_id(self):
        return self.env.user.id

    sede_id = fields.Many2one('guru.academy.sede', string='Sede', required=True)
    date = fields.Datetime(default=_default_date, string='Fecha y hora', readonly=True)
    # date_now = fields.Datetime(default=fields.Datetime.now, string='Fecha y hora')
    user_id = fields.Many2one('res.users', default=_default_user_id, string='Alumno', readonly=True)
