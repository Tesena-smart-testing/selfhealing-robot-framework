import docker
client = docker.from_env()
print(client.containers.get('f4601503b060').logs()) 
## TODO: replace the container ID with container name or other way how to identify the "hlm-proxy" container for easier setup
## TODO: extract the sentence "Report available at http://..." from the log output and write it to RobotFW log.html file on the test suite level (on the top)
## TODO: try to write info about the healed locator in the RobotFW log.html file on the place where the element was used (on the test step level)