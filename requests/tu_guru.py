import requests

api_auth_url = 'https://keycloak.quieroclientes.com/auth/realms/Comunidad/protocol/openid-connect/token'
grant_type = 'client_credentials'
client_id = 'odoo-guru'
client_secret = '***********'

try:
    response = requests.post(
        api_auth_url,
        headers={'content-type': 'application/x-www-form-urlencoded'},
        data=[('grant_type', grant_type), ('client_id', client_id), ('client_secret', client_secret)],
        timeout = 0.001
    )
    response.raise_for_status()

    response = response.json()
    print(response['access_token'])

except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)
