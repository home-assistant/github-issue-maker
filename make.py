from pathlib import Path
from pprint import pprint
from datetime import datetime
import sys
import requests
import json

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = "balloob"
TOKEN = Path(".token").read_text().strip()

# The repository to add this issue to
REPO_OWNER = "home-assistant"
REPO_NAME = "home-assistant"


def make_github_issue(title, body, labels):
    # Create an issue on github.com using the given parameters
    # Url to create issues via POST
    url = "https://api.github.com/repos/%s/%s/import/issues" % (REPO_OWNER, REPO_NAME)

    # Headers
    headers = {
        "Authorization": "token %s" % TOKEN,
        "Accept": "application/vnd.github.golden-comet-preview+json",
    }

    # Create our issue
    data = {
        "issue": {
            "title": title,
            "body": body,
            # "created_at": created_at,
            # "closed_at": closed_at,
            # "updated_at": updated_at,
            # "assignee": assignee,
            # "milestone": None,
            # "closed": False,
            "labels": labels,
        }
    }

    # Add the issue to our repository
    response = requests.request("POST", url, json=data, headers=headers)

    print(response.status_code)
    pprint(response.json())

    if response.status_code == 202:
        print('Successfully created Issue "%s"' % title)
    else:
        print('Could not create Issue "%s"' % title)
        print("Response:", response.content)


template = Path("./issues/device_trigger.markdown").read_text()

for domain in [
    "alarm_control_panel",
    "automation",
    "calendar",
    "camera",
    "climate",
    "cover",
    "device_tracker",
    "fan",
    "lock",
    "media_player",
    "remote",
    "vacuum",
    "water_heater",
]:
    title = f"Add device trigger support to the {domain} integration"
    body = template.replace("{{ DOMAIN }}", domain)
    labels = ["Hacktoberfest", "Help wanted"]

    make_github_issue(title, body, labels)
