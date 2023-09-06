{
    'name': 'Guru Airline',
    'version': '1.0',
    'author': 'Juan Salcedo - salcedo.salazar@gmail.com',
    'summary': 'Tracking de vuelos',
    'sequence': 10,
    'description': """
Guru Airline
====================
Módulo para realizar tracking de vuelos de la empresa Guru Soluciones.
    """,
    'category': 'Tools',
    'website': 'https://www.gurusoluciones.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/airline_menus.xml',
        'views/airline_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
