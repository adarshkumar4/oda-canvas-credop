import kopf
import requests
import base64
import logging
import kubernetes.client
from kubernetes import config
from kubernetes.client.rest import ApiException
import os
import json

config.load_kube_config()

# https://34.42.225.108
# credsOp_client_id = os.environ.get("CLIENT_ID")
# credsOp_client_secret = os.environ.get("CLIENT_SECRET")
# url = os.environ.get("KEYCLOAK_BASE")
# realm = os.environ.get("KEYCLOAK_REALM")

# Basic configuration
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('CredentialsOperator')
logger.setLevel(logging.INFO)
logger.info(f'Logging set to %s', logging.INFO)


credsOp_client_id = "credsop"
credsOp_client_secret =  "U447ybPAq3zZe1Lv7ys2oCajmcz4p3ce"
url = "http://34.173.174.235:8083/auth"
realm = "odari"

logger.info(f"{credsOp_client_id}, {credsOp_client_secret}, {url} , {realm}")

try:
    r = requests.post(
            url + "/realms/"+ realm +"/protocol/openid-connect/token",
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data={
                    "client_id": credsOp_client_id,
                    "client_secret":credsOp_client_secret,
                    "grant_type": "client_credentials",
            },
        )
    r.raise_for_status()
    token = r.json()["access_token"]
except requests.HTTPError as e:
    raise RuntimeError(
        f"request for token failed with HTTP status {r.status_code}: {e}"
    ) from None
else:
    logger.info( f'token : {token}' )


client_id = credsOp_client_id

try:
    r = requests.get(
            url + "/admin/realms/" + realm + "/clients",
            params={"clientId": client_id},
            headers={"Authorization": "Bearer " + token},
        )
        
    client_secret = r.json()[0]["secret"]
except requests.HTTPError as e:
    raise RuntimeError(
        f"request for client_secret failed with HTTP status {r.status_code}: {e}"
    ) from None
else:
    logger.info( f'client_secret : {client_secret}' )
   

encoded_client_id = base64.b64encode(client_id.encode('utf-8')).decode('utf-8')
encoded_client_secret = base64.b64encode(client_secret.encode('utf-8')).decode('utf-8')


# decoded_client_id = base64.b64decode(encoded_client_id).decode('utf-8')

logger.info( f'encoded_client_id : {encoded_client_id}' )

try:
    core_v1_api = kubernetes.client.CoreV1Api()

    secret = kubernetes.client.V1Secret(
        metadata=kubernetes.client.V1ObjectMeta(name=client_id + "-secret"),
        data={"client_id": encoded_client_id, "client_secret": encoded_client_secret}  # Base64 encoded values
    )

    core_v1_api.create_namespaced_secret(namespace="default", body=secret)
except ApiException as e:
    reason = json.loads(e.body)['reason']
    if(reason == "AlreadyExists"):
        logger.info( 'secret already exists no need to create it again' )
    else:  
        logger.error(
            f"secret creation failed : {e} "
        )
else:
    logger.info( 'secret created' )

    
    

    print('meta:', meta)
    print('\n spec:', spec)
    print('\n status:', status)
    print('\n body:', body)
    print('\n namespace:', namespace)
    print('\n labels:', labels)
    print('\n name:', name)
    print('\n old:', old)
    print('\n new:', new)
