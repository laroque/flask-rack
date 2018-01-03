
## Notes
To update an nginx configuration on the fly, you can do:
`nginx -s reload`
This will gracefully reload the configuration without interruption.
More usefully, if your configuration files are all mounted into the container,
`docker-compose exec http nginx -s reload`
will do the trick.
