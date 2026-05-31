# github_service.py

import os
import subprocess
from github import Github
from config import *


class GitHubService:

    def __init__(self):
        self.github = Github(GITHUB_TOKEN)
        self.repo = self.github.get_repo(GITHUB_REPOSITORY)

    def clone_repository(self):
        clone_url = self.repo.clone_url.replace(
            "https://",
            f"https://{GITHUB_TOKEN}@"
        )

        if not os.path.exists(WORKSPACE):
            subprocess.run([
                "git",
                "clone",
                clone_url,
                WORKSPACE
            ])

    def get_release_branch(self):
        branches = self.repo.get_branches()

        for branch in branches:
            if branch.name.startswith("release/"):
                return branch.name

        return None

    def get_develop_branch(self):
        return "develop"

    def create_release_branch(self, version):
        source = self.repo.get_branch("develop")

        self.repo.create_git_ref(
            ref=f"refs/heads/release/{version}",
            sha=source.commit.sha
        )

        print(f"Release branch release/{version} created")
