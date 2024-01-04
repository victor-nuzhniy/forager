"""Configuration module for Forager project."""
from __future__ import annotations

from typing import Optional


class HunterService:
    """Singlton class for initialized instance."""

    _hunter_service: Optional[Service] = None

    def __new__(cls, *args, **kwargs) -> HunterService:
        """Create new instance, if it's None, otherwise use earlier created one."""
        if not hasattr(cls, "instance"):
            cls.instance = super(HunterService, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def initialize_service(self, api_key: str):
        """Initialize hunter instance."""
        self._hunter_service = Service(api_key)

    def get_service(self):
        """Get hunter service instance."""
        return self._hunter_service


class Service:
    """Service for performing api calls."""

    def __init__(self, api_key: str) -> None:
        """Initialize service."""
        self.api_key: str = api_key
        self.endpoint: str = "https://api.hunter.io/v2/"

    def domain_search(
        self,
        domain: Optional[str] = None,
        company: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        email_type: Optional[str] = None,
        seniority: Optional[str] = None,
        department: Optional[str] = None,
        required_field: Optional[str] = None,
        raw: bool = False,
    ):
        """
        Perform domain_research request. Return all found email addresses.

        :param domain: str The domain on which to search for emails. Must be
        defined if company is not.

        :param company: str The name of the company on which to search for emails.
        Must be defined if domain is not.

        :param limit: int The maximum number of emails to give back. Default is 10.

        :param offset: int The number of emails to skip. Default is 0.

        :param email_type: str The type of emails to give back. Can be one of
        'personal' or 'generic'.

        :param seniority: str The seniority level of the owners of emails to give
        back. Can be 'junior', 'senior', 'executive' or a combination of them delimited
        by a comma.

        :param department: str The department where the owners of the emails to give
        back work. Can be 'executive', 'it', 'finance', 'management', 'sales', 'legal',
        'support', 'hr', 'marketing', 'communication' or a combination of
        them delimited by a comma.

        :param required_field: str Get only email addresses that have the selected
        field(s). The possible values are 'full_name', 'position', 'phone_number'.
        Several fields can be selected (comma-delimited).

        :param raw: bool Gives back the entire response instead of just the 'data'.

        :return: Full payload of the query as a dict, with email addresses
        found.
        """
        pass
