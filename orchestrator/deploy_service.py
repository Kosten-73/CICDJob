# deploy_service.py

import subprocess


class DeployService:

    def deploy_test_environment_1(self):
        subprocess.run([
            "docker-compose",
            "up",
            "-d"
        ])

        print("TEST ENV 1 deployed")

    def deploy_test_environment_2(self):
        print("Deploying to TEST ENV 2")
