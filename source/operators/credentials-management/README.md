# Credentials Management Operator





## Installation

1. Clone oda-canvas project

    ```bash
    git clone https://github.com/tmforum-oda/oda-canvas.git
    cd oda-canvas
    ```

2. Install Credentials-Management-Operator
   
    Client for Credentials-Management-Operator is created in IDM through keycloak installation [chart](https://github.com/tmforum-oda/oda-canvas/blob/c5dc6d8c9a04a456941ba7ae10c9a8e6b51b1398/charts/canvas-oda/values.yaml#L114)  during keycloak installation. 

    Manually copy **secret** of Credentials-Management-Operator **client** `credentialsmanagement-operator` in keycloak and add it in [values.yaml](https://github.com/tmforum-oda/oda-canvas/blob/main/charts/credentialsmanagement-operator/values.yaml#L23).:
        
     ```yaml
     client_secret: pDWc*****ITn
     ```

     Using updated **values.yaml** directly Install the operator using the following command.
  
      ```bash
      helm install credman-op charts/credentialsmanagement-operator -n canvas -f values.yaml
      ```
    **"or"**
   
     If you prefer to use the **--set** option instead of editing **values.yaml**.You can add **secret** inline without modifying your values file:
  
      ```bash
      helm install credman-op charts/credentialsmanagement-operator -n canvas --set=credentials.client_secret=pDWc*****ITn
      ```
      **"or"**
     
     If you want you can set it as an environment variable 
