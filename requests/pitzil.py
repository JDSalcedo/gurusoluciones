import json
import requests

url = "https://test.traficogarantizado.com/rest/hibu/sur/plan/save"

payload = {
    "id": "*************",
    "value": {
        "planType": "TM400",
        "iypCode": "16647608",
        "accountCode": "CL32415",
        "accountName": "COMPAÑIA DE TRANSPORTE MARITIMO S.A",
        "url": "https://www.amarillas.cl/fichas/ctm--chile--sa_16647608",
        "industryCode": "942568",
        "countryCode": 56,
        "stateCode": "05",
        "cityCode": 0,
        "months": 99,
        "endDate": 1955404800000
    }
}

def _get_pitzil_response(rp):
    rpta = dict()
    if 'error' in rp:
        rpta.update({
            'status': 'FAILURE',
            'mensaje': f"{rp['error']['code']}: {rp['error']['description']}"
        })
    else:
        rpta.update({
            'status': 'SUCCESS',
            'mensaje': rp['status']['description'],
            'id': rp['value']['id']
        })
    return rpta

try:
    response = requests.post(
        url,
        headers={'content-type': 'application/json'},
        auth=('**', '*****'),
        data=json.dumps(payload),
        timeout=(5, 30)
    )
    response = response.json()
    print(_get_pitzil_response(response))
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)