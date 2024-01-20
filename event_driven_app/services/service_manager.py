from logging import Logger
from typing import (
    Any,
    Callable,
    Dict,
    Type,
)


class ServiceManager:
    """
    Manages service instances for dependency injection.
    """

    def __init__(self, logger: Logger):
        self._services: Dict[Type, Any] = {Logger: logger}
        self._services_provider: Dict[Type, Any] = {}

    def get_service(self, service_type: Type) -> Any:
        """
        Retrieves a service instance of the specified type.

        :param service_type: The type of the service to retrieve.
        :return: The service instance or None if not found.
        """
        if service_type in self._services_provider:
            return self._services_provider[service_type]()
        return self._services.get(service_type)

    def set_service(self, service_type: Type, instance: Any) -> None:
        """
        Sets a service instance for a specified type.

        :param service_type: The type of the service.
        :param instance: The instance of the service to be registered.
        """
        self._services[service_type] = instance

    def set_service_provider(self, service_type: Type, provider: Callable) -> None:
        """
        Sets a service provider as callable.

        :param service_type: The type of the service.
        :param provider: action return service.
        """
        self._services_provider[service_type] = provider
