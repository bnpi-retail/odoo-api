import requests


username="1suser@mail.ru"
password="z,EqK33fxYaP,z4"
db_odoo = "db_odoo"


url = "https://retail.bnpi.dev/"
path = "/api/v1/retail/import/cost_price"
feed_xml_path = "./feed_xml.xml"


def connect_to_odoo_api_with_auth(db_odoo, username, password):
    session_url = f"{url}/web/session/authenticate"
    data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "db": db_odoo,
            "login": username,
            "password": password,
        },
    }
    session_response = requests.post(session_url, json=data)
    session_data = session_response.json()

    if session_data.get("result") and session_response.cookies.get("session_id"):
        session_id = session_response.cookies["session_id"]
        return session_id
    else:
        print(f'Error: Failed to authenticate - {session_data.get("error")}')
        return False

def send_file():
    session_id = connect_to_odoo_api_with_auth(db_odoo, username, password)
    if session_id is False: return False

    endpoint = f"{url}{path}"
    headers = {"Cookie": f"session_id={session_id}"}

    payload = {"data_for_download": "cost_price"}

    with open(feed_xml_path, 'rb') as file:
        files = {'file': ('output.xml', file)}
        response = requests.post(endpoint, headers=headers, files=files, data=payload)
        return response.status_code

response = send_file()
print(response)