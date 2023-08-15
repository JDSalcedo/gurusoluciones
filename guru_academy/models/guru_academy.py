from odoo import api, fields, models

PENDING = 'pending'
ALTA = 'alta'
BAJA = 'baja'


class GuruAcademy(models.Model):
    _name = 'guru.academy'  # table: guru_academy
    _description = 'Tabla de Academias'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    street = fields.Char(string='Dirección')
    nro = fields.Integer(string='Nro', group_operator=False)
    horario_apertura = fields.Float(string='Horario Apertura', group_operator=False)
    horario_cierre = fields.Float(string='Horario Cierre', group_operator=False)
    fecha_fundacion = fields.Date(string='Fundado en')
    # create_uid = fields.Many2one(string='Creado por')
    active = fields.Boolean(string='Activo', default=True)
    sede_ids = fields.One2many(comodel_name='guru.academy.sede', inverse_name='academy_id', string='Sedes')
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
    academy_id = fields.Many2one(
        'guru.academy', string='Academia', required=True, ondelete='restrict'
    )
    sequence = fields.Integer(string='Secuencia', default=10)
