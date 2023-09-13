{
    'name': 'Guru Log',
    'version': '1.0',
    'author': 'Guru Desarrollo - gabriela.carbajales@gurusoluciones.com',
    'summary': 'Log de Productos de Gurú',
    'sequence': 10,
    'description': """
Log de Productos de Gurú
========================
Módulo para registrar movimientos de estados en productos de Guru Soluciones.
    """,
    'category': 'Tools',
    'website': 'https://www.gurusoluciones.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/guru_product_log_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
