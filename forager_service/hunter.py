"""Configuration module for Forager project."""
from __future__ import annotations

from typing import Optional

from forager_service.app_services.async_service import AsyncService
from forager_service.app_services.crud_service import CRUDService
from forager_service.app_services.service import Service


class HunterService(object):
    """Singlton class for initialized instance."""

    _hunter_service: Optional[Service] = None
    _async_hunter_service: Optional[AsyncService] = None
    _crud_service: CRUDService = CRUDService()

    def __new__(cls, *args, **kwargs) -> HunterService:
        """Create new instance, if it's None, otherwise use earlier created one."""
        if getattr(cls, 'instance', None) is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

    def initialize_service(self, api_key: str) -> None:
        """Initialize hunter instance."""
        self._hunter_service = Service(api_key)

    def initialize_async_service(self, api_key: str) -> None:
        """Initialize async hunter instance."""
        self._async_hunter_service = AsyncService(api_key)

    @property
    def service(self) -> Service:
        """Get hunter service instance."""
        return self._hunter_service

    @property
    def async_service(self) -> AsyncService:
        """Get hunter service instance."""
        return self._async_hunter_service

    @property
    def crud_service(self) -> CRUDService:
        """Get CRUDService instance."""
        return self._crud_service
