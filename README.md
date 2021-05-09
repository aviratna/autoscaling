# Autoscaling
Autoscaling for container platform

There is a need for autoscaling solution which is configurable, data driven, policy based, supports multi-cloud which can be configured with parameters other than CPU, Memory etc

Features:
Kubernetes can only monitor the CPU & Memory
Below solution can monitor various parameters like number of connections to HAProxy, load on HAProxy etc
Can be extended to any application
Dynamic Load Balancer configuration, any app can use it
Solution is configuration based, no hard coding
Container will get attached to load balancer based on ENV variable passed or docker label during run time
Audit for autoscaling

Use cases:
To scale the containers based on number of connection
Autoscaling Rules
Dynamic update of load balancer with newly provisioned containers
Audit table for tracking the containers, timestamp, policy applied to understand the pattern

