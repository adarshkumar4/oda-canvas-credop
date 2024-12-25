import kopf
import requests
import base64
import kubernetes.client
from kubernetes import config

config.load_kube_config()

url = "http://34.173.174.235:8083/auth"

realm = "odari"
client_id = "credsop"

GROUP = "oda.tmforum.org"
IDENTITYCONFIG_VERSION = "v1"
IDENTITYCONFIG_PLURAL = "identityconfigs"

print("kopf")

@kopf.on.update(GROUP, IDENTITYCONFIG_VERSION, IDENTITYCONFIG_PLURAL, retries=5)
def credsOp(
    meta, spec, status, body, namespace, labels, name, old, new, **kwargs
):

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


    token = r1.json()["access_token"]



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

