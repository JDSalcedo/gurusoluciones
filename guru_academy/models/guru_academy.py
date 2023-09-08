from odoo import api, fields, models
from odoo.exceptions import UserError

PENDING = 'pending'
ALTA = 'alta'
BAJA = 'baja'


class GuruAcademy(models.Model):
    _name = 'guru.academy'  # table: guru_academy
    _description = 'Tabla de Academias'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre', required=True, tracking=True, copy=False)
    street = fields.Char(string='Dirección')
    nro = fields.Integer(string='Nro', group_operator=False)
    horario_inicio = fields.Float(string='Horario Apertura', group_operator=False)
    horario_cierre = fields.Float(string='Horario Cierre', group_operator=False)
    fecha_fundacion = fields.Date(string='Fundado en')
    # create_uid = fields.Many2one(string='Creado por')
    active = fields.Boolean(string='Activo', default=True)
    sede_ids = fields.One2many(comodel_name='guru.academy.sede', inverse_name='academy_id', string='Sedes', copy=False)
    sede_count = fields.Integer(compute='_compute_sede_count', string='# Sedes', store=True)
    state = fields.Selection([
        (PENDING, 'Pendiente'),
        (ALTA, 'De Alta'),
        (BAJA, 'De Baja')
    ], default=PENDING, string='Estado')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'El nombre debe ser único.')
    ]

    @api.depends('sede_ids')
    def _compute_sede_count(self):
        for academy in self:
            academy.sede_count = len(academy.sede_ids)

    def copy(self, default=None):
        default = dict(default or {})
        default['name'] = f'{self.name}_copy'
        return super(GuruAcademy, self).copy(default)

    def action_set_pendiente(self):
        self.ensure_one()
        self.write({'state': PENDING})

    def action_set_alta(self):
        self.ensure_one()
        self.write({'state': ALTA})

    def action_set_baja(self):
        self.ensure_one()
        self.write({'state': BAJA})


class GuruAcademySede(models.Model):
    _name = 'guru.academy.sede'
    _description = 'Tabla Sede de Academia'
    # _order = 'street'

    name = fields.Char(string='Nombre', required=True)
    street = fields.Char(string='Dirección', required=True)
    active = fields.Boolean(string='Activo', default=True)
    academy_id = fields.Many2one('guru.academy', string='Academia', required=True, ondelete='restrict')
    student_ids = fields.One2many(comodel_name='guru.academy.student', inverse_name='sede_id', string='Alumnos')
    sequence = fields.Integer(string='Secuencia', default=10)
    student_count = fields.Integer(compute='_compute_student_count', string='# Alumnos', store=True)

    @api.depends('student_ids')
    def _compute_student_count(self):
        for sede in self:
            sede.student_count = len(sede.student_ids)


class GuruAcademyStudent(models.Model):
    _name = 'guru.academy.student'
    _description = 'Tabla Alumno de Sede de Academia'
    # _order = 'street'

    name = fields.Char(string='Nombre', required=True)
    lastname = fields.Char(string='Apellido', required=True)
    street = fields.Char(string='Dirección', required=True)
    age = fields.Integer(string='Edad', required=True)
    active = fields.Boolean(string='Activo', default=True)
    sede_id = fields.Many2one('guru.academy.sede', string='Sede', required=True, ondelete='restrict')
    user_id = fields.Many2one('res.users', string='Usuario')
    sequence = fields.Integer(string='Secuencia', default=10)

    _sql_constraints = [
        ('name_lastname_sede_id_unique', 'unique(name,lastname,sede_id)', 'El nombre debe ser único.'),
        ('user_id_unique', 'unique(user_id)', 'El usuario relacionado debe ser único por Alumno.'),
    ]

    # @api.model_create_multi
    @api.model
    def create(self, values):
        age = values['age']
        if age > 99 or age < 0:
            raise UserError('La Edad del Alumno debe estar entre 0 y 99 años.')
        if 'user_id' not in values or not values['user_id']:
            login = values['lastname'].replace(' ', '_').lower()
            user_values = {
                'name': values['name'],
                'login': f'{login}_new',
            }
            user_id = self.env['res.users'].create(user_values)
            # new_user_id = user_id.copy({'login': f'{login}_copy'})
            # values['user_id'] = user_id.id
            values.update({'user_id': user_id.id})
        return super(GuruAcademyStudent, self).create(values)

    def write(self, values):
        if 'age' in values:
            age = values['age']
            if age > 99 or age < 0:
                raise UserError('La Edad del Alumno debe estar entre 0 y 99 años.')
        return super(GuruAcademyStudent, self).write(values)

    def copy(self, default=None):
        default = dict(default or {})
        default['name'] = f'{self.name}_copy'
        default['user_id'] = False
        return super(GuruAcademyStudent, self).copy(default)

    def unlink(self):
        self.write({'active': False})
        return True
        # return super(GuruAcademyStudent, self).unlink()
