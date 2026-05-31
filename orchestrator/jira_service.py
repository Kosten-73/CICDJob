# jira_service.py

from jira import JIRA
from config import *


class JiraService:

    def __init__(self):
        self.jira = JIRA(
            server=JIRA_URL,
            basic_auth=(JIRA_USER, JIRA_TOKEN)
        )

    def create_release_task(self, version):
        issue = self.jira.create_issue(
            project=JIRA_PROJECT,
            summary=f"Release {version}",
            description="Automatic release pipeline",
            issuetype={'name': 'Task'}
        )

        print(issue.key)

    def move_release_status(self, issue_key, transition_id):
        self.jira.transition_issue(
            issue_key,
            transition_id
        )
