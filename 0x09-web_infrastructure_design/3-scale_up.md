# Scale up

## For every additional element, why you are adding it:
In this structure we've added 1 load-balancer (HAproxy) configured as cluster with the other one and 1 server with splited components (web server,
 application server, database)
Using two load balancers configured as a cluster offers several benefits, primarily focused on enhancing reliability, availability, and scalability  of the load balancing infrastructure. Clustering load balancers provides redundancy and fault tolerance, ensuring continuous availability of load balancing services even if one load balancer fails. If one load balancer becomes unavailable due to hardware failure, software crash, or network issue, the other load balancer seamlessly takes over its responsibilities, preventing service disruptions and downtime.

Separating components onto individual servers allows each component to scale independently based on its specific resource needs and workload demands. For example, if the database server experiences increased data volume or query load, it can be scaled vertically or horizontally without affecting the performance of other components such as the web server or application server. it also ensures that resources (CPU, memory, disk I/O) are dedicated to specific tasks and are not shared or contended by other components. This improves resource utilization, prevents resource contention, and reduces the risk of performance degradation or bottlenecks caused by competing workloads.

