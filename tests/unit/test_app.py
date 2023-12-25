from abc import ABC

import pytest

from event_driven_app.entities import Command, CommandHandler, Event, EventHandler

from event_driven_app.application import App


class MockService:
    pass


@pytest.fixture
def app():
    return App()


def test_register_services(app):
    mock_services = {MockService: MockService()}
    app.register_services(mock_services)

    assert isinstance(app.service_manager.get_service(MockService), MockService)


class MockEvent(Event):
    pass


class MockEventHandler(EventHandler):
    def __init__(self, event: Event):
        super().__init__()

    def handle(self):
        pass


def test_register_events(app):
    mock_events = {MockEvent: [MockEventHandler]}
    app.register_events(mock_events)

    # Assert the event handler is registered for the event
    assert MockEvent in app.event_manager._handlers
    assert type(app.event_manager._handlers[MockEvent]) == list
    assert MockEventHandler in app.event_manager._handlers[MockEvent]


class MockCommand(Command):
    pass


class MockCommandHandler(CommandHandler, ABC):

    def __init__(self, command: Command):
        super().__init__()

    def execute(self, command: Command):
        pass


def test_register_commands():
    app = App()
    mock_commands = {MockCommand: MockCommandHandler}
    app.register_commands(mock_commands)

    # Assert the command handler is registered for the command
    assert MockCommand in app.command_manager._handlers
    assert app.command_manager._handlers[MockCommand] == MockCommandHandler
