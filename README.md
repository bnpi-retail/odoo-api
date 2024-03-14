# Documentation for Odoo APIs
  
### Base URL
 - https://retail.bnpi.dev/

### authenticate
request:
URL: /web/session/authenticate
METHOD: post
BODY:     {
           "jsonrpc": "2.0",
           "method": "call",
           "params": {
               "db": "db_odoo",
               "login": "admin",
               "password": "admin"
               }
           }
response:
{
    "jsonrpc": "2.0",
    "id": null,
    "result": {
        "uid": 2,
        "is_system": true,
        "is_admin": true,
        "user_context": {
            "lang": "en_US",
            "tz": "Asia/Tbilisi",
            "uid": 2
        },
        "db": "db_odoo",
        "server_version": "16.0-20240115",
        "server_version_info": [
            16,
            0,
            0,
            "final",
            0,
            ""
        ],
        "support_url": "https://www.odoo.com/buy",
        "name": "Mitchell Admin",
        "username": "admin",
        "partner_display_name": "YourCompany, Mitchell Admin",
        "company_id": 1,
        "partner_id": 3,
        "web.base.url": "http://0.0.0.0:8070",
        "active_ids_limit": 20000,
        "profile_session": null,
        "profile_collectors": null,
        "profile_params": null,
        "max_file_upload_size": 134217728,
        "home_action_id": false,
        "cache_hashes": {
            "translations": "eba47dad4272cb05eb4718387183c08a894454f9",
            "load_menus": "b2030befa585e85729b530f849ff203c055df9ef16f1d96cc668660ea81fed09"
        },
        "currencies": {
            "1": {
                "symbol": "€",
                "position": "after",
                "digits": [
                    69,
                    2
                ]
            }
        },
        "bundle_params": {
            "lang": "en_US"
        },
        "user_companies": {
            "current_company": 1,
            "allowed_companies": {
                "1": {
                    "id": 1,
                    "name": "YourCompany",
                    "sequence": 0
                }
            }
        },
        "show_effect": true,
        "display_switch_company_menu": false,
        "user_id": [
            2
        ]
    }
}
  
### Get session_id
The session ID is contained in cookies.
response.cookies["session_id"]
  
### Example request to send 1C cost price
request:
URL: /api/v1/retail/import/cost_price
METHOD: post
HEADER PARAMETERS: Cookie=session_id
BODY:
{
    "data_for_download": "cost_price",
    "file": "Base64_Encoded_File_Cost_price_from_1c"
}
