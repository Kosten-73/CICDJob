from github_service import GitHubService
from version_service import VersionService
from build_service import BuildService
from security_service import SecurityService
from deploy_service import DeployService
from jira_service import JiraService
from confluence_service import ConfluenceService


class PipelineOrchestrator:

    def __init__(self):

        self.github = GitHubService()
        self.version = VersionService()
        self.build = BuildService()
        self.security = SecurityService()
        self.deploy = DeployService()
        self.jira = JiraService()
        self.confluence = ConfluenceService()

    def run(self):

        print("STEP 1: Clone repository")
        self.github.clone_repository()

        print("STEP 2: Branch validation")
        release_branch = self.github.get_release_branch()

        if release_branch:
            print(f"Release branch found: {release_branch}")
        else:
            print("No release branch")

            new_version = self.version.increase_minor()

            self.github.create_release_branch(
                new_version
            )

        print("STEP 3: Maven build")
        self.build.build_maven_project()

        print("STEP 4: Security scanning")
        self.security.run_dependency_check()
        self.security.run_trivy_scan()
        self.security.run_sonarqube_scan()

        print("STEP 5: Deploy TEST 1")
        self.deploy.deploy_test_environment_1()

        print("STEP 6: Deploy TEST 2")
        self.deploy.deploy_test_environment_2()

        print("STEP 7: Jira")
        self.jira.create_release_task("1.1.0")

        print("STEP 8: Confluence")
        self.confluence.create_release_page(
            "1.1.0"
        )

        print("Pipeline completed")


if __name__ == "__main__":
    PipelineOrchestrator().run()
