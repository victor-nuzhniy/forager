"""Module for testing forager_service."""
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from asgiref.sync import async_to_sync
from faker import Faker

from forager_service import HunterService
from forager_service.exceptions import ArgumentValidationError
from tests.forager_service.conftest import get_query


class TestServiceDomainSearch:
    """Class for testing Service domain_search method."""

    @patch("forager_service.config.Service._perform_request")
    def test_domain_search(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test domain_search method."""
        domain: str = faker.city()
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_service(api_key)
        mock_request.side_effect = lambda x, y, **kwargs: get_query(x, y, **kwargs)
        result = HunterService().get_service().domain_search(domain)
        url, params, kwargs_dict = result
        assert url == "https://api.hunter.io/v2/domain-search"
        assert params["domain"] == domain
        assert params["api_key"] == api_key
        assert kwargs_dict["raw"] is False

    def test_domain_search_error(
        self,
        faker: Faker,
    ) -> None:
        """Test domain_search method, validation error case."""
        domain: int = faker.random_int()
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_service(api_key)
        with pytest.raises(ArgumentValidationError) as ex_info:
            HunterService().get_service().domain_search(domain)
        assert str(ex_info.value) == "domain has wrong type."


class TestServiceADomainSearch:
    """Class for testing Service adomain_search method."""

    @patch("forager_service.config.Service._aperform_request", new_callable=AsyncMock)
    def test_adomain_search(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test adomain_search method."""
        domain: str = faker.city()
        limit: int = faker.random_int(min=4, max=7)
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_service(api_key)
        mock_request.side_effect = lambda x, y, **kwargs: get_query(x, y, **kwargs)
        result = async_to_sync(HunterService().get_service().adomain_search)(
            domain, limit=limit
        )
        url, params, kwargs_dict = result
        assert url == "https://api.hunter.io/v2/domain-search"
        assert params["domain"] == domain
        assert params["limit"] == limit
        assert params["api_key"] == api_key
        assert kwargs_dict["raw"] is False


class TestServiceEmailFinder:
    """Class for testing Service email_finder method."""

    @patch("forager_service.config.Service._perform_request")
    def test_email_finder(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test email_finder method."""
        domain: str = faker.city()
        full_name: str = f"{faker.first_name()} {faker.last_name()}"
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_service(api_key)
        mock_request.side_effect = lambda x, y, **kwargs: get_query(x, y, **kwargs)
        result = HunterService().get_service().email_finder(domain, full_name=full_name)
        url, params, kwargs_dict = result
        assert url == "https://api.hunter.io/v2/email-finder"
        assert params["domain"] == domain
        assert params["full_name"] == full_name
        assert params["api_key"] == api_key
        assert kwargs_dict["raw"] is False


class TestServiceAEmailFinder:
    """Class for testing Service aemail_finder method."""

    @patch("forager_service.config.Service._aperform_request", new_callable=AsyncMock)
    def test_aemail_finder(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test aemail_finder method."""
        domain: str = faker.city()
        first_name: str = faker.first_name()
        last_name: str = faker.last_name()
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_service(api_key)
        mock_request.side_effect = lambda x, y, **kwargs: get_query(x, y, **kwargs)
        result = async_to_sync(HunterService().get_service().aemail_finder)(
            domain, first_name=first_name, last_name=last_name
        )
        url, params, kwargs_dict = result
        assert url == "https://api.hunter.io/v2/email-finder"
        assert params["domain"] == domain
        assert params["first_name"] == first_name
        assert params["last_name"] == last_name
        assert params["api_key"] == api_key
        assert kwargs_dict["raw"] is False


class TestServiceVerifyEmail:
    """Class for testing Service verify_email method."""

    @patch("forager_service.config.Service._perform_request")
    def test_verify_email(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test verify_email method."""
        email: str = faker.email()
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_service(api_key)
        mock_request.side_effect = lambda x, y, **kwargs: get_query(x, y, **kwargs)
        result = HunterService().get_service().verify_email(email)
        url, params, kwargs_dict = result
        assert url == "https://api.hunter.io/v2/email-verifier"
        assert params["email"] == email
        assert params["api_key"] == api_key
        assert kwargs_dict["raw"] is False


class TestServiceAVerifyEmail:
    """Class for testing Service averify_email method."""

    @patch("forager_service.config.Service._aperform_request", new_callable=AsyncMock)
    def test_averify_email(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test averify_email method."""
        email: str = faker.email()
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_service(api_key)
        mock_request.side_effect = lambda x, y, **kwargs: get_query(x, y, **kwargs)
        result = async_to_sync(HunterService().get_service().averify_email)(email)
        url, params, kwargs_dict = result
        assert url == "https://api.hunter.io/v2/email-verifier"
        assert params["email"] == email
        assert params["api_key"] == api_key
        assert kwargs_dict["raw"] is False


class TestServiceEmailCount:
    """Class for testing Service email_count method."""

    @patch("forager_service.config.Service._perform_request")
    def test_email_count(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test email_count method."""
        domain: str = faker.city()
        email_type: str = faker.random_element(elements=("personal", "generic"))
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_service(api_key)
        mock_request.side_effect = lambda x, y, **kwargs: get_query(x, y, **kwargs)
        result = (
            HunterService().get_service().email_count(domain, email_type=email_type)
        )
        url, params, kwargs_dict = result
        assert url == "https://api.hunter.io/v2/email-count"
        assert params["domain"] == domain
        assert params["type"] == email_type
        assert kwargs_dict["raw"] is False


class TestServiceAEmailCount:
    """Class for testing Service aemail_count method."""

    @patch("forager_service.config.Service._aperform_request", new_callable=AsyncMock)
    def test_aemail_count(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test aemail_finder method."""
        domain: str = faker.city()
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_service(api_key)
        mock_request.side_effect = lambda x, y, **kwargs: get_query(x, y, **kwargs)
        result = async_to_sync(HunterService().get_service().aemail_count)(domain)
        url, params, kwargs_dict = result
        assert url == "https://api.hunter.io/v2/email-count"
        assert params["domain"] == domain
        assert kwargs_dict["raw"] is False
