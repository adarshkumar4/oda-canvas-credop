# Credentials Management Operator

Client for credentials management operator is created in IDM through keycloak installation [chart](https://github.com/tmforum-oda/oda-canvas/blob/c5dc6d8c9a04a456941ba7ae10c9a8e6b51b1398/charts/canvas-oda/values.yaml#L114)  during keycloak installation. 

In [values.yaml](https://github.com/tmforum-oda/oda-canvas/blob/main/charts/credentialsmanagement-operator/values.yaml) :

  client_id = clientID of credentials management operator client in keycloak which should be same as mentioned in keycloak installation [chart](https://github.com/tmforum-oda/oda-canvas/blob/c5dc6d8c9a04a456941ba7ae10c9a8e6b51b1398/charts/canvas-oda/values.yaml#L114).
  
  client_secret =  secret of credentials management operator client in keycloak which needs to be manually fetched from keycloak and add it to [values.yaml](https://github.com/tmforum-oda/oda-canvas/blob/main/charts/credentialsmanagement-operator/values.yaml) or pass it as an argument during helm installation or set as an environment variable.

  kcbase: keycloak's base url, which should be configured by following [pattern](https://github.com/tmforum-oda/oda-canvas/blob/3d02df8f8680347c0df933c1f19b2e89ec00aee4/charts/credentialsmanagement-operator/values.yaml#L25C13-L25C121) 
  
  kcrealm: keycloak's realm, which should same as mentioned in installation charts.
  
These variables are used by operator to authenticate and get a token,which can be changed directly in values.yaml or passed as an argument in helm install or can be set as an environment variable.


#Installation

Clone oda-canvas project

git clone https://github.com/tmforum-oda/oda-canvas.git
cd oda-canvas


Manually copy client secret of credentialsmanagement-operator client from keycloak and add it as an argument during helm install :

helm install credman-op charts/credentialsmanagement-operator -n canvas --set=credentials.client_secret=pDWc*****ITn
