import pytest

from event_driven_app.services import DependencyInjector, ServiceManager


# Mock classes and services for testing
class MockService:
    pass


class MockClassWithDependency:
    def __init__(self, mock_service: MockService):
        self.mock_service = mock_service


class MockClassWithoutDependency:
    def __init__(self):
        pass


class TestDependencyInjector:
    @pytest.fixture
    def service_manager(self):
        sm = ServiceManager()
        sm.set_service(MockService, MockService())
        return sm

    @pytest.fixture
    def dependency_injector(self, service_manager):
        return DependencyInjector(service_manager)

    def test_dependency_injector_initialization(
        self, dependency_injector, service_manager
    ):
        assert (
            dependency_injector.service_manager is service_manager
        ), "DependencyInjector should initialize with the provided ServiceManager."

    def test_prepare_dependency_with_no_dependencies(self, dependency_injector):
        deps = dependency_injector.prepare_dependency(MockClassWithoutDependency)
        assert (
            deps == {}
        ), "prepare_dependency should return an empty dict for classes without dependencies."

    def test_prepare_dependency_with_dependencies(
        self, dependency_injector, service_manager
    ):
        deps = dependency_injector.prepare_dependency(MockClassWithDependency)
        assert isinstance(
            deps.get("mock_service"), MockService
        ), "prepare_dependency should return correct dependencies for classes with dependencies."
