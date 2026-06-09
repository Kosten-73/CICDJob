import pytest

def test_increase_minor():

    service = VersionService()

    assert service.increase_minor() == "1.1.0"