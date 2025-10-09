# Carbon-Management-Operator

## Carbon Intensity
Carbon intensity measures how much carbon (CO2e) is emitted per kilowatt-hour (KWh) of electricity consumed. The standard unit of carbon intensity is gCO2eq/kWh, or grams of carbon per kilowatt hour.
 
## Carbon Aware Software
Carbon awareness is the understanding that the environmental impact of electricity consumption varies based on the time and location of consumption, due to the fluctuating availability of renewable energy sources. Electricity is produced from a mix of sources, each with its own carbon emissions profile — renewables like wind, solar, and hydro generates minimal carbon, while fossil fuels such as coal and gas produces much more, with coal being the most carbon-intensive. The carbon footprint of energy used is determined primarily by its source, then the amount consumed.

Carbon-aware software is designed to increase electricity usage when the grid is supplied by cleaner, low-carbon sources, and decrease usage when the grid relies more on high-carbon sources. This approach helps minimize overall carbon emissions by aligning energy consumption with periods of lower carbon intensity of grid.

[Studies](https://ieeexplore.ieee.org/document/6128960) shows that these actions can result in 45% to 99% carbon reductions depending on the number of renewables powering the grid.


## We can make our softwares Carbon Aware by following these approaches :

### Scheduling workloads according to the carbon intensity of the region or grid where they run:
Use Case:
For example, training a Machine Learning model at a different time or region with much lower carbon intensity.By leveraging real-time data on grid carbon intensity, carbon aware software can schedule computational tasks, adjust performance settings, or shift workloads to times and places where renewable energy sources are more prevalent, minimizing the overall carbon footprint.

Kubernetes Scheduler evenly distributes Pods across Nodes and ensures enough resources (memory, CPU, etc.) are available to run workloads.It also lets define logic to assign Nodes to Pods.Hence Kubernetes Scheduler can be use d schedule workloads by assigning Nodes to pods based on carbon intensity data of electrical grids to minimize the carbon emission.Carbon intensity data for electrical grids can be retrieved through APIs like WattTime and Electricity maps.
We can query the API to get the carbon intensity of the location of each of our Nodes and create a YAML file for that and feed that YAML to the Scheduler’s algorithm to make a carbon-aware decision about where to place the new Pod.This sample YAML file should be periodically updated as carbon intensities change and re-applied to the Scheduler.

Through this approach we can take advantage of natural fluctuations in carbon intensity to ensure our application requires the least amount of carbon to meet our business and customer needs and help reduce demand on higher carbon emitting sources.

Factors like data sovereignty, latency, and the complexity of shifting infrastructure around should be taken into consideration before going down this path.


This approach is available here https://greensoftware.foundation/articles/carbon-aware-kubernetes
Few Alorithms related to this approach are available here :
The bulk of the functionality comes from the Kubernetes Scheduler itself and a research paper titled “A
[Low Carbon Kubernetes Scheduler](http://ceur-ws.org/Vol-2382/ICT4S2019_paper_28.pdf)
[Carbon emission-aware job scheduling for Kubernetes deployments](https://link.springer.com/article/10.1007/s11227-023-05506-7)


### Scaling workloads according to the carbon intensity of the region or grid where they run:

We can scale workloads without making any changes to the codes of the workloads by developing a Kubernetes operator which uses any KEDA (Kubernetes Event-Driven Autoscaler) scaler to scale workloads based on carbon intensity data of the electrical grids and independent of the workload usage. Carbon intensity data for electrical grids can be retrieved from third party sources such as WattTime, Electricity Map or any other provider. These datas from third party sources can be used to create a configMap which can be read by Kubernetes operator to dynamically adjust the scaling behavior of KEDA scaler and set maxReplicaCount to limit scaling workloads during high carbon intensity periods, and allow more scaling when carbon intensity is lower.

This Approach with detailed solution is available here : https://github.com/Azure/carbon-aware-keda-operator.

Use case : low priority and time flexible workloads that support interuptions in dev/test environments. Some examples of these are 
non-critical data backups
batch processing jobs
data analytics processing
ML training jobs.
Building AI models when carbon emissions are lower
Deploying software into the cloud in locations that have greener energy sources
Running software updates at greener energy time windows
Using data to run hypothetical models to understand how you could start driving impact and reduce emissions, drive business cases for change, and create a greener future.



With the Carbon Aware SDK you can build software that chooses to run when the wind is blowing, enable systems to follow the sun, moving around the world to where energy is the greenest, and create tools that give insights and help software innovators to make greener software decisions. All of this helps reduce carbon emissions.

Machine Learning (ML) workloads are a great example of long running compute intensive workloads, that often are also not time critical. By moving these workloads to a different time, the carbon emissions from the ML training can be reduced by up to 15%, and by moving the location of the training this can be reduced even further, at times by up to 50% or more.

Did you know that data centres emit more carbon than aviation or shipping? And it is not slowing down, with some research forecasting that computing will contribute 14% of global emissions by 2040. Even worse, a significant portion of these emissions is wasted on non-production resources running outside office hours, always having your application scaled out for peak hours. This is not only bad for the planet but also for your cloud bill.

the scale of our applications to:

Current events, for example, in terms of incoming web requests or messages in a Kafka topic. Sizing your application based on how much work it has alleviates overprovisioning and always-on resources.
The availability of clean energy. The electricity on the data centre's power grid comes from different sources, such as coal, nuclear, and solar. We should do more when the energy is cleaner, i.e., the carbon intensity is lower to reduce emissions further.

 make our applications greener by making them event-driven and carbon-aware.

 these properties at the level of the Kubernetes cluster using KEDA (Kubernetes Event-Driven Autoscaler) and Microsoft's Carbon Aware KEDA Operator, so all applications in the cluster can benefit without becoming more complex themselves.
