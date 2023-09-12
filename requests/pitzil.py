import requests

api_auth_url = 'https://keycloak.quieroclientes.com/auth/realms/Comunidad/protocol/openid-connect/token'
grant_type = 'client_credentials'
client_id = 'odoo-guru'
client_secret = 'ZxLvjIau5nYNEEbdFT2ia03UrpSzCCiV'
try:
    response = requests.post(
        api_auth_url,
        headers={'content-type': 'application/x-www-form-urlencoded'},
        data=[('grant_type', grant_type), ('client_id', client_id), ('client_secret', client_secret)]
    )
    if response.status_code == 200:
        response = response.json()
    if 'access_token' not in response:
        print(response.reason)
    if 'access_token' in response:
        print(response['access_token'])
except Exception as error:
    print(error)
