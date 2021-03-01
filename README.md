# Project Cheetah


### Problem Description
To enhance speed of continuous scraper by managing lambda container resource.


### High Level Algorithm
- Consume status feed produced by the 'slow' scraper
- Log each status feed row into cheetah status file
- Return a list of avoidable IPs using cheetah status file
    - First priority is given to IPs not utilized by the service before
    - Second priority is given to IPs not utilized before in a given span of time - currently any IP that was utilized less than 5 seconds before is sent to avoid list.
- Initiate request for scraping
- Force cold start if each resource has been utilized *well*.


### Assumption
- Scraper lambda container to update status feed each time a request to competitor API is made
- Scraper lambda container to *pass* a request for scraping if its using an *avoidable IP*


### Instructions
- Please run the following steps in terminal.
```
    cd project-cheetah
    python3 -m venv venv
    source venv/bin/activate
    bash simulate.sh 30
```