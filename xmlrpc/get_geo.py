import xmlrpc.client

PROD = True

dominio = "https://gurusoluciones.odoo.com" if PROD else "https://gurusoluciones-desa-09-01-9532780.dev.odoo.com"
db = "guru-publicar-main-3540736" if PROD else "gurusoluciones-desa-09-01-9532780"
login = "salcedo.salazar@gmail.com"
password = "********"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(dominio))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(dominio))

uid = common.authenticate(db, login, password, {})
element_id = ['274591']
rpta = models.execute_kw(db, uid, password, 'guru.service', 'get_geo', [element_id])
print(rpta)
