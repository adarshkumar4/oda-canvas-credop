# Carbon-Management-Operator
Electricity is generated from various sources, each with different carbon emissions. Renewable sources (wind, solar, hydro) emit little to no carbon, while fossil fuels (coal, gas) emit more, with coal being the highest.
Carbon awareness means understanding that the energy you consume does not always have the same impact in terms of carbon intensity - it varies depending on the time and place it is consumed. So, doing more when electricity is cleaner i.e.more energy comes from low carbon sources and doing less when electricity is dirtier i.e. more energy comes from high carbon sources.
Carbon intensity measures how much carbon (CO2e) is emitted per kilowatt-hour (KWh) of electricity consumed. The standard unit of carbon intensity is gCO2eq/kWh, or grams of carbon per kilowatt hour.
If your computer is plugged directly into a wind farm, its electricity would have a carbon intensity of 0 gCO2eq/kWh since a wind farm emits no carbon to produce that electricity. However, most people can't plug directly into wind farms; instead, they plug into power grids supplied with electricity from various sources.Once on a grid, you can't control which sources supply the electricity you are using; you simply get a mix of everything. So, your carbon intensity will be a mix of all the current power sources in a grid, both the lower- and the higher-carbon sources.

Carbon intensity also changes over time due to the inherent variability of renewable energy caused by the unpredictability of weather conditions. For example, when it's cloudy or the wind isn't blowing, carbon intensity increases since more of the electricity in your mix comes from sources that emit carbon.

https://learn.greensoftware.foundation/assets/images/08_variability_CI-f14dcd8660f96d9c22f8eeab43a9378e.png
Carbon aware software does more when it can leverage greener energy sources, and less when the energy CO2 emissions are higher.
Being carbon aware means responding to shifts in carbon intensity by increasing or decreasing your demand. If your work allows you to be flexible with when and where you run workloads, you can shift accordingly - consuming electricity when the carbon intensity is lower and pausing production when it is higher. For example, training a Machine Learning model at a different time or region with much lower carbon intensity.
[Studies](https://ieeexplore.ieee.org/document/6128960) show these actions can result in 45% to 99% carbon reductions depending on the number of renewables powering the grid.
move your computation to another physical location where the current carbon intensity is lower. It might be a region that naturally has lower carbon sources of energy. For example, moving to different hemispheres depending on the season for more sunlight hours.
shift to another time. Perhaps later in the day or night when it's sunnier or windier and, therefore, the carbon intensity is lower.We can predict future carbon intensity reasonably well through advances in weather forecasting.


Kubernetes is built in a way that it can make carbon-aware decisions balanced against the technical requirements of the system
 extend the Kubernetes Scheduler to take advantage of the natural fluctuations in carbon intensities in our existing power grids to minimize the amount of carbon in the atmosphere that your Kubernetes cluster is responsible for.

The bulk of the functionality comes from the Kubernetes Scheduler itself and a research paper titled “A
[Low Carbon Kubernetes Scheduler](http://ceur-ws.org/Vol-2382/ICT4S2019_paper_28.pdf)
In short, the Scheduler takes Pods (one or more of your containers) and assigns them to run on Nodes (virtual or physical machines). It does a good job on its own of placing Pods to keep an even distribution across Nodes and ensure enough resources (memory, CPU, etc.) are available to run workloads. However, the Scheduler also lets you define your own rules for how to assign Nodes to Pods. This is where we can inject carbon intensity data as another factor for the Scheduler to use when placing Pods. 
Carbon intensity data for electrical grids around the world is available through APIs like WattTime. They provide a Marginal Operating Emissions Rate (MOER) value that represents the pounds of carbon emitted to create a megawatt of energy — the lower the MOER, the cleaner the energy. WattTime’s API provides both a real-time and projected carbon intensity value for a location like zip code or Latitude and Longitude coordinate (GPS). 
We can query the API to get the carbon intensity of the location of each of our Nodes and feed this to the Scheduler’s algorithm to make a carbon-aware decision about where to place the new Pod.
With a MOER value assigned to each Node, we need to account for assigning a weight across multiple Nodes. A simplified approach is to take the MOER value of an individual node and divide it by the total MOER values across all nodes to get a normalized percentage weighting of each Node. Save these weightings to a YAML file and by applying them as a Priority for the Scheduler, your Pods will now be assigned to Nodes with lower MOER values where possible.
This sample YAML file should be periodically updated as carbon intensities change and re-applied to the Scheduler. Executing the weighting calculation as its own process will allow you to add additional factors to your weighting algorithm, like latency or predicted MOER values. 
These three pieces together–Scheduler, Carbon Intensity Data and Weighting Algorithm–allows any Kubernetes instance to become carbon aware. It can take advantage of natural fluctuations in carbon intensity to ensure your application requires the least amount of carbon to meet your business and customer needs. There are a lot of positive changes in carbon reduction, having an automated way of shifting your workloads around like this allows you to quickly take advantage of improvements and help reduce demand on higher carbon emitting sources.
Factors like data sovereignty, latency, and the complexity of shifting infrastructure around should be taken into consideration before going down this path.
[Carbon emission-aware job scheduling for Kubernetes deployments](https://link.springer.com/article/10.1007/s11227-023-05506-7)

Kubernetes operator that aims to reduce carbon emissions by helping KEDA scale Kubernetes workloads based on carbon intensity. Carbon intensity is a measure of how much carbon dioxide is emitted per unit of energy consumed. By scaling workloads according to the carbon intensity of the region or grid where they run, we can optimize the carbon efficiency and environmental impact of our applications.
This operator can use carbon intensity data from third party sources such as WattTime, Electricity Map or any other provider, to dynamically adjust the scaling behavior of KEDA. The operator does not require any application or workload code change, and it works with any KEDA scaler.
Use cases for the operator include low priority and time flexible workloads that support interuptions in dev/test environments. Some examples of these are non-critical data backups, batch processing jobs, data analytics processing, and ML training jobs.
The carbon aware KEDA operator retrieves the carbon intensity data from a ConfigMap, which is generated by a third party component.
the Kubernetes Carbon Intensity Exporter operator, which builds on the carbon-aware-sdk, to provide
 carbon intensity data in the Kubernetes cluster, so it can be used by operators for carbon aware decision making.
 The "Kubernetes carbon intensity exporter" retrieves 24-hour carbon intensity forecast data every 12 hours. Upon successful data pull, the old configmap will be deleted and a new configmap with the same name will be created.
 Any other Kubernetes operator or workload can read the configMap for utilizing the carbon intensity data.
Making carbon aware scaling decisions:
As an admin you create a CarbonAwareKedaScaler spec for targetRef : scaledObject or scaledJob
Then the operator will update KEDA scaledObjects and scaledJob maxReplicaCount field, based on the current carbon intensity.
The current logic for carbon aware scaling is based on carbon intensity metric only, which is independent of the workload usage.
The operator will not compute a desired replicaCount for your scaledObjects or scaledJobs, as this is the responsibility of KEDA and HPA. The operator would define a "ceiling for allowed maxReplicas" based on carbon intensity of the current time.
In practice, this operator will throttle workloads and prevent them from bursting during high carbon intensity periods, and allow more scaling when carbon intensity is lower.
data exporter by which Kubernetes operators can leverage the carbon intensity data from 3rd party for carbon-aware workload scheduling.
We provide a helm chart to help install the exporter. Note that this data exporter ONLY retrieves the carbon intensity data from WattTime OR Electricity Maps.
The data exporter will retrieve the 24-hour carbon intensity forecast data from WattTime every 12 hours. Upon successful data pull, the old configmap will be deleted and a new configmap with the same name will be created. If the data pull hits failures, the new confgimap is still created with the last seen binary data and the failure reason should be mentioned in the value of the message key. Any Kubernetes operator can read the configmap for utilizing the carbon intensity data.
The EmissionData struct is defined in here. https://github.com/Azure/kubernetes-carbon-intensity-exporter/blob/main/pkg/sdk/api/emissions_data.go
Building AI models when carbon emissions are lower
Deploying software into the cloud in locations that have greener energy sources
Running software updates at greener energy time windows
Using data to run hypothetical models to understand how you could start driving impact and reduce emissions, drive business cases for change, and create a greener future.
You can reduce the carbon footprint of your application by just running things at different times and in different locations.
When software does more when the electricity is clean and do less when the electricity is dirty, or runs in a location where the energy is cleaner, we call this carbon aware software.
carbon efficient vs carbon aware software.
With the Carbon Aware SDK you can build software that chooses to run when the wind is blowing, enable systems to follow the sun, moving around the world to where energy is the greenest, and create tools that give insights and help software innovators to make greener software decisions. All of this helps reduce carbon emissions.
Machine Learning (ML) workloads are a great example of long running compute intensive workloads, that often are also not time critical. By moving these workloads to a different time, the carbon emissions from the ML training can be reduced by up to 15%, and by moving the location of the training this can be reduced even further, at times by up to 50% or more.
Did you know that data centres emit more carbon than aviation or shipping? And it is not slowing down, with some research forecasting that computing will contribute 14% of global emissions by 2040. Even worse, a significant portion of these emissions is wasted on non-production resources running outside office hours, always having your application scaled out for peak hours. This is not only bad for the planet but also for your cloud bill.
the scale of our applications to:
Current events, for example, in terms of incoming web requests or messages in a Kafka topic. Sizing your application based on how much work it has alleviates overprovisioning and always-on resources.
The availability of clean energy. The electricity on the data centre's power grid comes from different sources, such as coal, nuclear, and solar. We should do more when the energy is cleaner, i.e., the carbon intensity is lower to reduce emissions further.
 make our applications greener by making them event-driven and carbon-aware.
 these properties at the level of the Kubernetes cluster using KEDA (Kubernetes Event-Driven Autoscaler) and Microsoft's Carbon Aware KEDA Operator, so all applications in the cluster can benefit without becoming more complex themselves.
