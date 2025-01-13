import kopf
import requests
import base64
import logging
import kubernetes.client
from kubernetes.client.rest import ApiException
import json
import os

logging_level = os.environ.get("LOGGING", logging.INFO)
logger = logging.getLogger('CredentialsOperator')
logger.setLevel(int(logging_level))
logger.info("Logging set to %s", logging_level)

credsOp_client_id = os.environ.get("CLIENT_ID")
credsOp_client_secret = os.environ.get("CLIENT_SECRET")
url = os.environ.get("KEYCLOAK_BASE")
realm = os.environ.get("KEYCLOAK_REALM")

GROUP = "oda.tmforum.org"
IDENTITYCONFIG_VERSION = "v1"
IDENTITYCONFIG_PLURAL = "identityconfigs"

logger.info(f"{credsOp_client_id}, {credsOp_client_secret}, {url} , {realm}")

# @kopf.on.resume(GROUP, IDENTITYCONFIG_VERSION, IDENTITYCONFIG_PLURAL, retries=5)
# @kopf.on.create(GROUP, IDENTITYCONFIG_VERSION, IDENTITYCONFIG_PLURAL, retries=5)
@kopf.on.update(GROUP, IDENTITYCONFIG_VERSION, IDENTITYCONFIG_PLURAL, retries=5)
def credsOp(
    meta, spec, status, body, namespace, labels, name, old, new, **kwargs
):

    # del unused-arguments for linting
    del status, labels, kwargs


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

    client_id = name

    logger.info( f'client_id : {client_id}' )

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
            raise kopf.TemporaryError(
                f"secret creation failed : {e} "
            )
    else:
        logger.info( 'secret created' )