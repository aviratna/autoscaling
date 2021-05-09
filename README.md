# Autoscaling
Autoscaling for container platform

There is a need for autoscaling solution which is configurable, data driven, policy based, supports multi-cloud which can be configured with parameters other than CPU, Memory etc

**Features:**
Kubernetes can only monitor the CPU & Memory
Below solution can monitor various parameters like number of connections to HAProxy, load on HAProxy etc
Can be extended to any application
Dynamic Load Balancer configuration, any app can use it
Solution is configuration based, no hard coding
Container will get attached to load balancer based on ENV variable passed or docker label during run time
Audit for autoscaling

**Use cases:**
To scale the containers based on number of connection
Autoscaling Rules
Dynamic update of load balancer with newly provisioned containers
Audit table for tracking the containers, timestamp, policy applied to understand the pattern

**Logic**

Connection to MySQL Database to read the policy rules

Connection to MongoDB to check for unprocessed records

Read the alerts for autoscaling

Get current datetime

Search for un processed records

Container frontend Rule

Get the Docker API details

TLS Configuration for accessing remote docker API using certs

Inspect the container to get docker label, cpu, memory, volume details required for docker run command

Read docker labels

Action copy it from alert notifications

Get the Autoscale policy based on docker label or Service Name. docker label will take the priority and then db configruation

##**Policy Type: Service Availability**

As part of Service Availability 
If service stops, start the service
If service delete event, create new service from same image and pass docker labels from previous container
Also check for how to allocate the ElastAlert
Start the container if stopped and type = service availability

#**Policy Type: Scale Up**

Take the min, max dynamically. Based on if condition of stats.
Check for Min Max value for number of container created against db as checking for container with same docker label in different VCH will be more cycle
Or Check for Min Max value captured through ElastAlert portal. And check for

#**Policy Type: Dynamic Load Balancer**

Policy Type: Dynamic Load Balancer (HAProxy, Nginx or Traefik). Once application is scale upscale down, check how to connect to load balancer. 
Container should take care of connection LB dynamically based on label or API

Policy Type: Monitor the Load Balancer (HAProxy, Nginx, Traefik, Envoy) Response Time. 
Call above scale up & scale down application based on application alert. Above function can be reused

Logic: Capture the Service Name from Alert. Search for Container list using filter Label-service that Docker Label And apply the Scale Up & Scale Down policy

#**Policy Type: Scale Down**

Take the min, max dynamically. Based on if condition of stats
Do the docker inspect using API to search for other scaled container based on label search, get container id and delete

Update the record in Autoscale History for Scale Down Tracking 
Update the Database for Audit purpose.

#**Traefik: Load Balancer Scale Up**

Count No of records
Inspect the container to get the Docker Label, cpu, memory, volume details required for docker run commands 
Based on number of container with that service name scale up and scale down 
Insert the record in Autoscale History

#**Traefik: Load balancer Scale Down**

Count No of records
Inspect the container to get the Docker Label, cpu, memory, volume details required for docker run commands 
Based on number of container with that service name scale down 
Insert the record in Autoscale History

#**HAProxy Load balancer Scale Up**

Inspect the container to get the Docker Label, cpu, memory, volume details required for docker run commands
Get HAProxy label passed to Container
Update the HAProxy Configuration Dynamically 
