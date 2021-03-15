import requests
import json
from decouple import config


"""
Grabs the authentication crumb and converts to JSON
"""
response = requests.get(
    config('JENKINS_URL')
    + "/crumbIssuer/api/json",
    auth=('jgruenbaum', config("JENKINS_TOKEN")))

response = json.loads(response.text)

"""
Posts request to the job url, passing ip_address
as a parameter.
"""
job_trigger_response = requests.post(
    config('JENKINS_URL')
    + '/job/ip_auto_block/buildWithParameters?token='
    + config('IP_JOB_TOKEN')
    + """&ip_address='127.0.0.1'""",
    headers=response,
    auth=(config("USERNAME"), config("JENKINS_TOKEN")))
