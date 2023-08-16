{
    'name': 'Guru Academy',
    'version': '1.0',
    'author': 'Gabi - gabriela.cabajales@gmail.com',
    'summary': 'Academia Gurú',
    'sequence': 10,
    'description': """
Academia Gurú
====================
Módulo para registrar las capacitaciones/cursos dictados en Guru Soluciones.
    """,
    'category': 'Academy/eLearning',
    'website': 'https://www.gurusoluciones.com',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/guru_academy_menus.xml',
        'views/guru_academy_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
