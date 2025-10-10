# Carbon Management Operator

## Carbon Intensity
Carbon intensity refers to the amount of carbon dioxide equivalent (CO2e) emitted for each kilowatt-hour (kWh) of electricity consumed, typically measured in grams of CO2e per kWh (gCO2eq/kWh). It quantifies the carbon emissions produced per unit of energy used.

## Carbon Aware
Carbon awareness is the understanding that the environmental impact of electricity consumption varies based on the time and location of consumption, due to the fluctuating availability of renewable energy sources. Electricity is produced from a mix of sources, each with its own carbon emissions profile — renewables like wind, solar, and hydro generates minimal carbon, while fossil fuels such as coal and gas produces much more, with coal being the most carbon-intensive. The carbon footprint of energy used is determined primarily by its source, then the amount consumed.

## Carbon Aware Software
Carbon-aware software is designed to increase electricity usage when the grid is supplied by cleaner, low-carbon sources, and decrease usage when the grid relies more on high-carbon sources. This approach helps minimize overall carbon emissions by aligning energy consumption with periods of lower carbon intensity of grid.

[Studies](https://ieeexplore.ieee.org/document/6128960) shows that these actions can result in 45% to 99% carbon reductions depending on the number of renewables powering the grid.

### We can achieve carbon awareness in software by adopting the following approaches :

#### Scheduling workloads based on the carbon intensity of the region or grid in which they operate :
Workload scheduling can be achieved without modifying the workloads themselves by developing a Kubernetes operator that leverages the Kubernetes Scheduler to allocate workloads based on the carbon intensity of electrical grids, independent of workload usage. The Kubernetes Scheduler ensures Pods are evenly distributed across Nodes while maintaining sufficient resources (e.g., memory, CPU) for workload execution. Carbon intensity data for electrical grids can be sourced from third-party providers such as WattTime, Electricity Maps, or any other provider.

The operator would query APIs to retrieve the carbon intensity for the location of each Node and generate a YAML file containing this data. This YAML file can then be injected into the Kubernetes Scheduler, enabling it to assign Nodes to Pods based on carbon intensity data, thereby minimizing carbon emissions. As carbon intensity fluctuates over time, the YAML file should be periodically updated and re-applied to the Scheduler.

To implement this approach effectively without disrupting business requirements, considerations such as infrastructure complexity, latency, and data sovereignty must also be addressed.

This approach is detailed in the Green Software Foundation article on [Carbon-Aware Kubernetes](https://greensoftware.foundation/articles/Carbon-Aware-kubernetes). 
Key algorithms supporting this method are described in the research paper [A Low Carbon Kubernetes Scheduler](http://ceur-ws.org/Vol-2382/ICT4S2019_paper_28.pdf) and in studies on [Carbon emission-aware job scheduling for Kubernetes deployments](https://link.springer.com/article/10.1007/s11227-023-05506-7). Much of the core functionality relies on the Kubernetes Scheduler itself.


### Scaling workloads according to the carbon intensity of the region or grid where they run:

Workloads can be scaled without modifying their code by creating a Kubernetes operator that integrates with a KEDA (Kubernetes Event-Driven Autoscaler) scaler. This operator uses carbon intensity data from third-party providers like WattTime or Electricity Maps to guide scaling decisions independently of workload usage. The operator queries these APIs to retrieve location-specific carbon intensity data and stores it in a configMap. This configMap is then used to dynamically adjust the KEDA scaler’s behavior, setting the maxReplicaCount to restrict scaling during periods of high carbon intensity and allowing greater scaling when carbon intensity is low. Since carbon intensity fluctuates over time, the configMap should be regularly updated and re-applied to ensure effective scaling.


A detailed solution for this approach can be found at: [Azure Carbon-Aware KEDA Operator](https://github.com/Azure/carbon-aware-keda-operator).

By adopting these strategies, organizations can leverage natural variations in carbon intensity to minimize the carbon footprint of their applications, better meet business and customer requirements, decrease reliance on high-carbon energy sources, and lower operational costs by optimizing resource usage.



Use Case: By utilizing real-time grid carbon intensity data, carbon-aware software can optimize when and where computational tasks are executed, adjust performance settings, or shift workloads to periods and regions with greater availability of renewable energy, thereby reducing the overall carbon footprint.

Machine Learning (ML) workloads, which are typically compute-intensive and not time-sensitive, can benefit significantly from this approach. Scheduling ML training during times of lower carbon intensity can cut emissions by up to 15%, and relocating training to greener regions can achieve reductions of 50% or more.

Other suitable candidates for carbon-aware scheduling include low-priority, time-flexible workloads that tolerate interruptions, such as:

Non-critical data backups
Batch processing jobs
Data analytics tasks
Building AI models when carbon emissions are lower
Deploying software to cloud regions with cleaner energy
Running software updates during greener energy windows
Additionally, leveraging data to run hypothetical models can help organizations identify opportunities to reduce emissions, build business cases for change, and contribute to a more sustainable future.



