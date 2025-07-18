# Open Digital Architecture Canvas

[![Supported-component-version](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftmforum-oda%2Foda-canvas%2Fmain%2Fcharts%2Fcanvas-oda%2FChart.yaml&query=%24.appVersion&label=Supported-component-version)](https://github.com/tmforum-oda/oda-canvas)
[![Canvas-version](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftmforum-oda%2Foda-canvas%2Fmain%2Fcharts%2Fcanvas-oda%2FChart.yaml&query=%24.version&label=Canvas-version)](https://github.com/tmforum-oda/oda-canvas)
[![License](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftmforum-oda%2Foda-canvas-ctk%2Fmain%2Fpackage.json&query=%24.license&label=License&color=%09%23a3ff00)](https://github.com/tmforum-oda/oda-canvas/blob/main/LICENSE)

[![bdd](https://img.shields.io/badge/BDD_tests-8A2BE2?style=flat-square&color=grey)](https://reports.cucumber.io/report-collections/f62e87a7-f6bf-4aaf-b603-d4fa2b05b630)[![passed](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fmessages.cucumber.io%2Fapi%2Freport-collections%2Ff62e87a7-f6bf-4aaf-b603-d4fa2b05b630%2Freports&query=%24.reports%5B-1%3A%5D.statusCounts.PASSED&style=flat-square&label=Passed%3A%20&labelColor=%230BDA51&color=%230BDA51)](https://reports.cucumber.io/report-collections/f62e87a7-f6bf-4aaf-b603-d4fa2b05b630)[![undef](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fmessages.cucumber.io%2Fapi%2Freport-collections%2Ff62e87a7-f6bf-4aaf-b603-d4fa2b05b630%2Freports&query=%24.reports%5B-1%3A%5D.statusCounts.UNDEFINED&style=flat-square&label=Undefined%3A%20&labelColor=%23FFC000&color=%23FFC000)](https://reports.cucumber.io/report-collections/f62e87a7-f6bf-4aaf-b603-d4fa2b05b630)[![failed](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fmessages.cucumber.io%2Fapi%2Freport-collections%2Ff62e87a7-f6bf-4aaf-b603-d4fa2b05b630%2Freports&query=%24.reports%5B-1%3A%5D.statusCounts.FAILED&style=flat-square&label=Failed%3A%20&labelColor=%23D22B2B&color=%23D22B2B)
](https://reports.cucumber.io/report-collections/f62e87a7-f6bf-4aaf-b603-d4fa2b05b630)




The Open Digital Architecture (ODA) Canvas is an execution environment for ODA Components and the release automation part of a CI/CD pipeline. This repository contains the Reference Implementation, open-source code, use-cases and test-kit for a [TM Forum ODA canvas](https://www.tmforum.org/oda/deployment-runtime/oda-canvas/). You are free to use this as a starting point for your own ODA Canvas implementation. 

The [Usecase Library](usecase-library/README.md) shows how ODA Components interact with the ODA Canvas. The [Feature definition and Test Kit](feature-definition-and-test-kit/README.md) details the features required to be a fully compliant ODA Canvas and a set of tests that can be used to validate any ODA Canvas. The [source code](source/README.md) contains the source code for the operators that are part of the ODA Canvas.

The Reference Implementation of the ODA Canvas will be used for ODA Component certification. 



## Installation

see [Installation Guide](installation/README.md) for installation instructions.


## Introduction to ODA Canvas

There is an introductory video on the ODA Canvas at:

[![How do I buy or build an ODA Canvas?](https://img.youtube.com/vi/dYyyCDPlVHY/0.jpg)](https://youtu.be/B5lF94l-Dek?si=gKQAW57j8GEDx6Yv&t=1)

The ODA Canvas is itself a modular architecture, with independent **operators** that embed the management and operations activities in software. The **Component Management** operator manages the lifecycle of each component, and the de-composition into ExposedAPIs, IdentityConfigs and other sub-resources (that are processed by their corresponding operators). The **API Management** operators manage the API Gateway and/or Service Mesh to provide security, throttling and other non-functional services to allow API endpoints to be exposed to external consumers. You deploy the matching API Management operator for whatever API Gateway or Service Mesh you are using. The **Identitiy Config** operator configures the Identity Management Services. The **Secrets Management** operator is an optional operator to configure secrets. The **Dependency Management** operator provides services to allow a Component to discover API dependencies. We foresee new operator types becoming available as the ODA Canvas matures.

The ODA Canvas reference implementation includes example operators to that are freely available for organizations to re-use, extend or replace with their own implementations. We expect a typical production implementation will use a combination of standard operators and custom operators that can implement that organizations specific operational policies.

For more information see [Software Operators](source/operators/README.md)


## ODA Canvas Design

The design (including ongoing work) of the ODA Canvas is documented in [ODA Canvas Design](Canvas-design.md).

Security principles for the ODA Canvas design are documented in [ODA Security Principles](SecurityPrinciples.md).


## Release notes


| Version    | Release notes                         |
|:----------:|---------------------------------------|
| 1.2.3      | June 2025 release ahead of DTW                                                   |
| 1.2.2      | First update incorporating fixes since general availability launch               |
| 1.2.0      | Release of `v1` component specification and general availability of ODA Canvas   |
| 1.1.8      | Final changes to `v1beta4` component specification                               |
| 1.1.7      | Updated to `v1beta4` component specification                                     |
| 1.1.5      | Multiple fixes                                                                   |
| 1.1.4      | Added secretsmanagement-operator                                                 |
| 1.1.3      | Moved operators to use `tmforumodacanvas` docker repository                      |
| 1.1.2      | Added dependentApiSimpleOperator                                                 |
| 1.1.1      | Bug fix release - Webhook handles empty specification field for exposedAPI. Tested against kubernetes 1.29.        |
| 1.1.0      | Added support for multiple specifications of each Open-API. The v1beta3 `exposedAPI` object defines its `specification` property as an array. This is specifically designed to allow TM Forum Gen5 Open-APIs (which can be specified alongside Gen4 APIs).  <BR/> The [Webhook](./source/webhooks) will automatically convert v1beta2 and v1beta1 specifications to v1beta3 with an array of 1.          |
| 1.0.0      | First tracked release for component version v1beta3 (also supports N-2 versions i.e. v1beta2 and v1beta1).


## For Developers

How to work with this repository:

* [How-To work with Dockerimages](./docs/developer/work-with-dockerimages.md)
