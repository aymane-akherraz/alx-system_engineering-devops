# Postmortem

### Issue Summary:

The outage lasted about 2 hours from 1 to 3 am (GMT+01:00 Friday 11 September 2023). The problem was from the web server, it was down, so the users had a denial of service in that period of time and from the statistics we found that there was about 50% of users affected in this duration, and the root cause was a hardware issue.

### Timeline:

The issue was detected at 1:00 am.
The issue was detected by our monitoring alert (Datadog) and it did send an email to the dev team.
Unfortunately, at that time all of the team personnel were at their houses and were sleeping except for one but it wasn’t online. At 2:00 am that engineer by coincidence did look at his email inbox so he found the email sent by the monitoring tool then he did call the others and they head to the company because they had to as i said it was a hardware issue, so they did investigate all the machines, first the assumption was that it could be from hard drives but it wasn’t that.
The investigation paths were: first to find the machines that are not functioning and then investigate and search them in order to find the root cause of the issue.
The incident escalated to the whole team because when the first one knows he did acknowledge all the others.
The incident was resolved after two hours of the outage, it did take time because they needed to check all the machines in order to find the one with the issue and did fix it.
### Root cause and resolution :

The issue was caused by a specific machine in which we found a dead motherboard and this machine was one of the servers running web server inside of it so when it did go down all the load was redirected to the others which do not have a huge capacity like this one had, so they easily got overloaded.
Fortunately, we’ve fixed the issue and get rid of that machine and replace it with a new one much better than the old one.
### Corrective and preventative measures must contain:

All the machines need to be improved and to be equal in hardware resources, so we’ve made a To do list:
Replace all the old machines with new and more powerful ones.
A mandatory health check will be done every week to ensure that no problem like that happens in the future.
All the machines will be equal in configuration and in hardware and software resources in order to guarantee stability and efficiency.

