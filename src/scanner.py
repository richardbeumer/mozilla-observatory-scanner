import requests
import json
import os
from logger import Logger

log = Logger.get_logger(__name__)
log.info('Scan Started')

def scan(site):
    log.info('Scanning: %s', site)
    response = requests.post("https://observatory-api.mdn.mozilla.net/api/v2/scan?host=" + site)
    result = response.json()
    if result.get('grade') == None:
        log.error('Scan for: %s failed with error: %s', site, result['error'])
        return result
    else:
        return result

def get_grade(site):
    scan_result = scan(site)
    if scan_result.get('grade') == None:
        return "Error: " + scan_result['error']
    return scan_result['grade']


def get_grades():
    sites = json.loads(os.environ['SITES'])
    data = {}
    for site in sites:
        data[site] = get_grade(site)
    return data

def post_slack(data):
    webhook_url = os.environ['SLACK_WEBHOOK']
    lines = [f'{key}: {value}' for key, value in data.items()]
    lines = '\n'.join(lines)

    text = """
    Scan results from Mozilla Observatory:\n{data}
    """
    text = text.format(data=lines)

    slack_data = {'text': text}

    requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )

post_slack(get_grades())
log.info("Scan Finished")