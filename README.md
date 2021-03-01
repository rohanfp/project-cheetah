# Project Cheetah


### Problem Description
To enhance speed of continuous scraper by managing lambda container resource.


### High Level Algorithm
- Pick service name and avoidable IPs by utilizing status feed.
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