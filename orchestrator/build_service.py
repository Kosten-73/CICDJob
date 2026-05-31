# build_service.py

import subprocess
from config import WORKSPACE


class BuildService:

    def build_maven_project(self):
        result = subprocess.run(
            ["mvn", "clean", "package"],
            cwd=WORKSPACE
        )

        if result.returncode != 0:
            raise Exception("Maven build failed")

        print("Maven build success")
