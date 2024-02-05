# Documentation for Odoo APIs

### Base URL
 - https://retail.bnpi.dev/api/v1/

### Get session_id
```
def connect_to_odoo_api_with_auth(
    db_odoo: str,
    username: str,
    password: str
) -> Union[str, bool]:
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
```
---
### Example request with session_id
```
def send_requests():
    session_id = connect_to_odoo_api_with_auth(db_odoo, username, password)
    if session_id is False: return False

    endpoint = f"{url}{path}"
    headers = {"Cookie": f"session_id={session_id}"}

    payload = {"parametr": "parametr"}

    with open(feed_xml_path, 'rb') as file:
        files = {'file': ('output.xml', file)}

    response = requests.post(endpoint, headers=headers, files=files, data=payload)
    return response.status_code
```
