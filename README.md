# flask-rack
Containerizing a generic flask application with one service per container.

## Quick Start
It shold be fine to clone this repo and just spin everything up with `docker-compose up` (adding whatever options you want).
At least for now this repo isn't going to do anything interesting beyond working out the connection between an nginx http server and a uWSGI webserver, each in its own container.
There will be a mostly empty flask application which is just there to see it work.
