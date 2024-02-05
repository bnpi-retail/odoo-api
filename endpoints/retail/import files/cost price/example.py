import requests

from os import getenv
from typing import Union


username = getenv("USERNAME")
password = getenv("PASSWORD")
db_odoo = getenv("DB_ODOO")
url = getenv("BASE_URL")

path = "/api/v1/retail/import/cost_price"
feed_xml_path = "./feed_xml.xml"
data_for_download = "cost_price"

def connect_to_odoo_api_with_auth(db_odoo: str, username: str, password:str) -> Union[str, bool]:
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

def send_requests(data_for_download: str) -> int:
    session_id = connect_to_odoo_api_with_auth(db_odoo, username, password)
    if session_id is False: return False

    endpoint = f"{url}{path}"
    headers = {"Cookie": f"session_id={session_id}"}

    payload = {"data_for_download": data_for_download}

    with open(feed_xml_path, 'rb') as file:
        file_content = file.read()

    files = {'file': ('output.xml', file_content)}

    response = requests.post(endpoint, headers=headers, files=files, data=payload)
    return response.status_code

response = send_requests(data_for_download)
print(response)