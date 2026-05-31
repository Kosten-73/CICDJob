# security_service.py

import subprocess
from config import WORKSPACE


class SecurityService:

    def run_dependency_check(self):
        subprocess.run([
            "dependency-check",
            "--scan",
            WORKSPACE
        ])

    def run_trivy_scan(self):
        subprocess.run([
            "trivy",
            "fs",
            WORKSPACE
        ])

    def run_sonarqube_scan(self):
        subprocess.run([
            "sonar-scanner"
        ])
