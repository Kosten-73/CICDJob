# version_service.py

import semver


class VersionService:

    def __init__(self):
        self.current_version = "1.0.0"

    def increase_minor(self):
        self.current_version = semver.bump_minor(
            self.current_version
        )

        return self.current_version
