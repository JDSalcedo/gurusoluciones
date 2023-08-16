from odoo import fields, models


class Users(models.Model):
    _inherit = 'res.users'

    student_id = fields.Many2one('guru.academy.student', string='Alumno')