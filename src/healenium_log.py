from robot.api.deco import keyword
import docker
import regex

@keyword
def getHealeniumReportLink():
    client = docker.from_env()
    logs = client.containers.get('hlm-proxy').logs()
    reportlink = regex.search(r"(?r)Report available at .*", logs.decode("utf-8")) # find last occurence of this regex
    return reportlink[0]