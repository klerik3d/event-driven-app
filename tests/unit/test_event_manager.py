import pytest

from src.entities import Event, EventHandler
from src.services import DependencyInjector, EventManager, ServiceManager


# Mock classes for testing
class MockEvent(Event):
    pass


class MockHandler(EventHandler):
    handled = False

    def __init__(self, event):
        super().__init__()
        self.event = event

    def handle(self):
        MockHandler.handled = True


@pytest.fixture
def event_manager():
    return EventManager()


@pytest.fixture
def service_manager():
    return ServiceManager()


@pytest.fixture
def dependency_injector(service_manager):
    return DependencyInjector(service_manager)


def test_trigger_with_registered_handler(event_manager, dependency_injector):
    mock_event = MockEvent()

    # Registering the mock handler for the mock event
    event_manager.register_handler(MockEvent, MockHandler)

    # Trigger the event
    event_manager.trigger(mock_event, dependency_injector)

    # Assert that the handle method of the mock handler was called once
    assert MockHandler.handled


def test_trigger_with_unregistered_event(event_manager, dependency_injector):
    unregistered_event = MockEvent()

    # No handler should be called
    # Depending on your implementation, you might want to assert that no error is raised
    event_manager.trigger(unregistered_event, dependency_injector)
    assert True
