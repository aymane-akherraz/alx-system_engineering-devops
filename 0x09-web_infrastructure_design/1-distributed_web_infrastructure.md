# Distributed web infrastructure

## For every additional element, why you are adding it:
In this structure we've added a load balancer and another server, so we've added a load balancer in order to distribute incoming traffic across those two servers, preventing any single server from becoming overwhelmed. This ensures that the system can handle a larger volume of requests and provides a better experience for users by minimizing response times. and we also added another server in order to achieve higher availability and fault tolerance. If one server fails or needs maintenance, the other server can continue to handle requests, ensuring that the application remains accessible and operational. This reduces the risk of downtime and improves reliability for your users.

## What distribution algorithm your load balancer is configured with and how it works:
The load balancer is configured with Robin-Round algorithm, because we have two servers with the same capacity so this algo is the most suitable in our case because requests are served by the server sequentially one after another, after sending the request to the last server, it starts from the first server again and the round goes on, so Round Robin passes each new connection request to the next server in line, eventually distributing connections evenly across the array of machines being load balanced.

## Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both:
My load-balancer is enabling an Active-Active setup, the two servers are active and can be used to improve scalability as well as provide high availability. When using an Active-Active setup, all instances handle requests concurrently in the other hand when using an Active-Passive setup the active instance handles requests and the passive instance remains on standby, in case the active instance is down the Passive instance will turn on application services can successfully resume processing.

## How a database Primary-Replica (Master-Slave) cluster works:
In a Primary-Replica (Master-Slave) database cluster architecture, there is a primary (master) database server and one or more replica (slave) database servers.
The Primary Database Server is the main server responsible for handling read and write operations, it receives write operations (such as INSERT, UPDATE, DELETE) from client applications and executes them on the database, after executing a write operation, the primary server replicates the changes to the replica servers to ensure data consistency across the cluster.

The Replica Database Servers are read-only copies of the primary database, they replicate data from the primary server to maintain a synchronized copy of the database. Replica servers handle read operations (such as SELECT queries) from client applications, offloading the primary server and improving read scalability. Replication is typically asynchronous, meaning that there might be a slight delay between when a write operation is performed on the primary server and when it is replicated to the replica servers.

Here is how the Replication Process works:
The replication process involves copying the changes made to the primary database's data and applying them to the replica servers.
The primary server logs all changes to its data in a replication log (often called a "binlog" or "WAL" - Write-Ahead Log).
Replica servers periodically connect to the primary server and retrieve these changes from the replication log.
The replica servers apply the changes to their own databases, ensuring that they stay synchronized with the primary server.

## What is the difference between the Primary node and the Replica node in regard to the application:
From the application's perspective, the primary node is responsible for handling both read and write operations and serves as the authoritative source of data, while replica nodes replicate data from the primary node and serve as read-only copies optimized for handling read queries. The application interacts with the primary node for write operations and with replica nodes for read operations, allowing for a balanced and scalable database architecture.
## Some issues with this infrastructure:

### Where are SPOF:
The SPOF in this structure is the load balancer because we have only one so if fails it will disrupt the flow of traffic to the backend servers, rendering the application inaccessible to users.

### Security issues:
In a distributed web infrastructure, there are several security issues that need to be addressed to ensure the protection of data, applications, and users.
In this structure we're using HTTP as our communication protocol which is not secure because all communications sent over regular HTTP connections are in 'plain text' and can be read by any hacker, so this presents a clear danger if the communication is on an order form and includes your credit card details or social security number. We also haven't implemented any firewalls to restrict access to sensitive resources and prevent unauthorized access from external networks.

### No monitoring:
Without monitoring, administrators lack visibility into the health, performance, and usage of the distributed infrastructure. They may not be aware of potential bottlenecks, resource constraints, or impending failures until they impact the system's operation or user experience.
When issues arise, the lack of monitoring makes it challenging to identify the root cause and troubleshoot problems effectively. Administrators may resort to manual inspection or guesswork, leading to longer resolution times and increased downtime.
Without monitoring, security breaches may go unnoticed, allowing attackers to exploit vulnerabilities or exfiltrate sensitive data without detection.
Performance issues, outages, or security incidents that go undetected without monitoring can degrade the user experience, leading to dissatisfaction, loss of trust, and potential churn among customers or users.

