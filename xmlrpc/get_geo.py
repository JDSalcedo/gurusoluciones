import xmlrpc.client

PROD = False

dominio = "https://gurusoluciones.odoo.com" if PROD else "https://gurusoluciones-desa-09-11-9655079.dev.odoo.com"
db = "guru-publicar-main-3540736" if PROD else "gurusoluciones-desa-09-11-9655079"
login = "salcedo.salazar@gmail.com"
password = "********"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(dominio))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(dominio))

uid = common.authenticate(db, login, password, {})
element_id = ['274591']

# rpta = models.execute_kw(db, uid, password, 'guru.service', 'get_geo', [element_id])
# models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {'name': "Newer partner"}])
rpta = models.execute_kw(db, uid, password, 'project.task', 'message_post', [[57195]], {'body': 'Prueba mensaje'})
print(rpta)




