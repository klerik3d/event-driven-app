from unittest.mock import Mock

import pytest

from event_driven_app.services.service_manager import ServiceManager


class MockService:
    pass


class TestServiceManager:
    @pytest.fixture
    def service_manager(self):
        return ServiceManager(Mock())

    def test_service_manager_initialization(self, service_manager):
        assert (
            len(service_manager._services) == 1
        ), "ServiceManager should initialize with an logger _services dictionary."
        assert list(service_manager._services.keys())[0].__name__ == 'Logger'

    def test_set_service(self, service_manager):
        mock_service_instance = MockService()
        service_manager.set_service(MockService, mock_service_instance)
        assert (
            service_manager._services[MockService] == mock_service_instance
        ), "set_service should correctly add service instances."

    def test_get_service_with_existing_service(self, service_manager):
        mock_service_instance = MockService()
        service_manager.set_service(MockService, mock_service_instance)
        retrieved_service = service_manager.get_service(MockService)
        assert (
            retrieved_service == mock_service_instance
        ), "get_service should return the correct service instance for an existing service."

    def test_get_service_with_non_existing_service(self, service_manager):
        retrieved_service = service_manager.get_service(MockService)
        assert (
            retrieved_service is None
        ), "get_service should return None when the service does not exist."
