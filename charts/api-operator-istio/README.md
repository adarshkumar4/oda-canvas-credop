# api-operator-istio

![Version: 1.0.3](https://img.shields.io/badge/Version-1.0.3-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v1beta4](https://img.shields.io/badge/AppVersion-v1beta4-informational?style=flat-square)

A helm chart to deploy the api operator for istio

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| configmap.loglevel | string | `"20"` |  |
| deployment.apiopImage | string | `"tmforumodacanvas/api-operator-istio"` |  |
| deployment.apiopImagePullPolicy | string | `"IfNotPresent"` |  |
| deployment.apiopPrereleaseSuffix | string | `nil` |  |
| deployment.apiopVersion | string | `"0.6.0"` |  |
| deployment.credentialName | string | `"istio-ingress-cert"` |  |
| deployment.dataDog.enabled | bool | `false` |  |
| deployment.hostName | string | `"*"` |  |
| deployment.httpsRedirect | bool | `true` |  |
| deployment.ingressClass.enabled | bool | `false` |  |
| deployment.ingressClass.name | string | `"nginx"` |  |
| deployment.istioGateway | bool | `true` |  |
| deployment.keycloak.port | int | `8080` |  |
| deployment.monitoredNamespaces | string | `"components"` |  |
| deployment.operatorName | string | `"api-operator-istio"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)