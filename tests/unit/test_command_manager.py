import pytest

from src.entities import Command, CommandHandler
from src.services import (CommandManager, DependencyInjector, EventManager,
                          ServiceManager)


# Mock classes for testing
class MockCommand(Command):
    pass


class MockHandler(CommandHandler):
    handled = False

    def __init__(self, command):
        super().__init__()
        self.command = command

    def handle(self):
        MockHandler.handled = True


@pytest.fixture
def command_manager():
    return CommandManager()


@pytest.fixture
def service_manager():
    return ServiceManager()


@pytest.fixture
def dependency_injector(service_manager):
    return DependencyInjector(service_manager)


@pytest.fixture
def event_manager():
    return EventManager()


def test_trigger_with_registered_handler(
    command_manager, dependency_injector, event_manager
):
    mock_command = MockCommand()

    # Registering the mock handler for the mock command
    command_manager.register_handler(MockCommand, MockHandler)

    # Trigger the command
    command_manager.execute(mock_command, event_manager, dependency_injector)

    # Assert that the handle method of the mock handler was called once
    assert MockHandler.handled


def test_trigger_with_unregistered_command(
    command_manager, event_manager, dependency_injector
):
    unregistered_command = MockCommand()

    # No handler should be called
    # Depending on your implementation, you might want to assert that no error is raised
    with pytest.raises(ValueError):
        command_manager.execute(
            unregistered_command, event_manager, dependency_injector
        )
