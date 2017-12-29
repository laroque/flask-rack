# flask-rack
Containerizing a generic flask application with one service per container.

## Quick Start
It shold be fine to clone this repo and just spin everything up with `docker-compose up` (adding whatever options you want).
At least for now this repo isn't going to do anything interesting beyond working out the connection between an nginx http server and a uWSGI webserver, each in its own container.
There will be a mostly empty flask application which is just there to see it work.

## Open Questions
1. How do I deal with the following situation. I have one nginx server running on somename.org. I have a flask application in a container serving some page containername:5000/some_page_path and responds to db requests to containername:5000/some_db_interface, which are used in AJAX posts to that url. The problem being that the client is looking at somename.org/some_page_name and needs to make a post that nginx will forward properly.
