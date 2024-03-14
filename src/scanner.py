import requests
import json
import os
from logger import Logger

log = Logger.get_logger(__name__)
log.info('Scan Started')

def scan(site):
    url = "https://http-observatory.security.mozilla.org/api/v1/analyze?host=" + site
    data = {}
    data['rescan'] = 'true'
    data['hidden'] = 'true'
    log.info('Scanning: %s', site)
    response = requests.post(url=url, data=data)
    result = response.json()
    print(result)
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

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    print(response.status_code)

post_slack(get_grades())