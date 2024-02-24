# Simple web stack

## What is a server:
A server is a computer (composed by hardware and software) that provides a service to other computers or programs by processing requests and delivering data over the internet or a local network to its clients. A server can be physical or virtual or both at the same time, we can have for example one physical server which is running four other virtual servers on it.

## What is the role of the domain name:
The principal role of the domain name is helping users to easily find their way around the Internet by just entering the domain name of the web site instead of the long and complex IP adresses which are very hard to remember.

## What type of DNS record www is in www.foobar.com:
www is of type CNAME because it's just an alias for the principal domain name foobar.com, so both of them are pointing to the same IP address

## What is the role of the web server:
The web server is responsable for storing, processing, and delivering requested information or webpages to end users

## What is the role of the application server:
The role of the application server is processing data and using business logic to provide the correct information to end users

## What is the role of the database:
The role of the database is to store, retrieve, and update any sort of data in an organized way.

## What is the server using to communicate with the computer of the user requesting the website:
The server is using the HTTP (Hypertext Transfer Protocol) to communicate with the computer of the user requesting the website, first the browser sends an HTTP Request to the server and the server responds back using HTTP and serves the documents as requested by the client, so that the browser can finally present the Web Page.
## Some issues with this infrastructure:

### SPOF:
Single point of failure (SPOF) is any non-redundant part of a system that, if dysfunctional, would cause the entire system to fail. A single point of failure is antithetical to the goal of high availability in a computing system or network, a software application, a business practice, or any other industrial system.
There might be single points of failure. If the web server or application server goes down, it can bring down the entire system, leading to downtime.
### Downtime:
Server downtime is the period when your web services are inaccessible to your website or web application visitors for example when deploying new code or maintenance is needed then the web server needs to be restarted so the whole system has to be shut down

### scalability:
Scalability can become an issue as the demand on the system grows, as traffic increases, certain components of the stack might become performance bottlenecks. For instance, the application server might not handle a large number of concurrent connections efficiently, or the database might struggle to keep up with the increasing volume of queries.
