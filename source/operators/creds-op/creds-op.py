# import kopf

# https://34.42.225.108

# GROUP = "oda.tmforum.org"
# IDENTITYCONFIG_VERSION = "v1"
# IDENTITYCONFIG_PLURAL = "identityconfigs"


# @kopf.on.update(GROUP, IDENTITYCONFIG_VERSION, IDENTITYCONFIG_PLURAL, retries=5)
# def credsOp(
#     meta, spec, status, body, namespace, labels, name, old, new, **kwargs
# ):

#     try:
#         r = requests.post(
#             self._url + "/realms/master/protocol/openid-connect/token",
#             data={
#                 "username": user,
#                 "password": pwd,
#                 "grant_type": "password",
#                 "client_id": "admin-cli",
#                 },
#             )
#             r.raise_for_status()
#             return r.json()["access_token"]
#         except requests.HTTPError as e:
#             raise RuntimeError(
#                 f"get_token failed with HTTP status {r.status_code}: {e}"
#             ) from None

    

import requests
import base64
import kubernetes.client
from kubernetes import config

config.load_kube_config()
# kcBaseURL = os.environ.get("KEYCLOAK_BASE")
# kcRealm = os.environ.get("KEYCLOAK_REALM")

url = "http://34.173.174.235:8083/auth"

realm = "odari"
client_id = "credsop"


r1 = requests.post(
    url + "/realms/odari/protocol/openid-connect/token",
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    data={
            "client_id": "credsop",
            "client_secret":"U447ybPAq3zZe1Lv7ys2oCajmcz4p3ce",
            "grant_type": "client_credentials",
        },
    )

# url = "http://34.173.174.235:8083/auth/realms/odari/protocol/openid-connect/token"

# payload = 'client_id=credsop&client_secret=U447ybPAq3zZe1Lv7ys2oCajmcz4p3ce&grant_type=client_credentials'


# response = requests.request("POST", url, headers=headers, data=payload)

# # print(response.text)

token = r1.json()["access_token"]

# print(token)

r2 = requests.get(
        url + "/admin/realms/" + "odari" + "/clients",
        params={"clientId": "credsop"},
        headers={"Authorization": "Bearer " + token},
        )
        
client_secret = r2.json()[0]["secret"]

print("client_secret : "+ client_secret)


encoded_client_id = base64.b64encode(client_id.encode('utf-8')).decode('utf-8')
encoded_client_secret = base64.b64encode(client_secret.encode('utf-8')).decode('utf-8')


decoded_client_id = base64.b64decode(encoded_client_id).decode('utf-8')

print(encoded_client_id + "\n" + encoded_client_secret)

core_v1_api = kubernetes.client.CoreV1Api()

secret = kubernetes.client.V1Secret(
    metadata=kubernetes.client.V1ObjectMeta(name=client_id + "-secret"),
    data={"client_id": encoded_client_id, "client_secret": encoded_client_secret}  # Base64 encoded values
)

core_v1_api.create_namespaced_secret(namespace="default", body=secret)

# for d in r2.json() :
#     print(d["id"])





# url2 = "http://34.173.174.235:8083/auth/admin/realms/odari/clients"

# payload2 = {}
# headers2 = {
#   'Authorization': 'Bearer '+response.json()["access_token"]
# }

# response2 = requests.request("GET", url2, headers=headers2, data=payload2)

# print(response2.json())
