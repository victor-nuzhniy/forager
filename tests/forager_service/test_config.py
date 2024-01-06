"""Module for testing forager_service."""
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from asgiref.sync import async_to_sync
from faker import Faker

from forager_service.config import HunterService
from forager_service.exceptions import ArgumentValidationError
from tests.forager_service.conftest import get_query


class TestServiceDomainSearch(object):
    """Class for testing Service domain_search method."""

    @patch('forager_service.config.Service._perform_request')
    def test_domain_search(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test domain_search method."""
        domain: str = faker.city()
        api_key: str = 'some_key'
        HunterService().initialize_service(api_key)
        mock_request.side_effect = get_query
        received_data = HunterService().service.domain_search(domain)
        url, kwargs = received_data
        assert url == 'https://api.hunter.io/v2/domain-search'
        assert kwargs.get('param_dict')['domain'] == domain
        assert kwargs.get('param_dict')['api_key'] == api_key
        assert kwargs['raw'] is False

    def test_domain_search_error(
        self,
        faker: Faker,
    ) -> None:
        """Test domain_search method, validation error case."""
        domain: int = faker.random_int()
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_service(api_key)
        with pytest.raises(ArgumentValidationError):
            HunterService().service.domain_search(domain)


class TestAsyncServiceDomainSearch(object):
    """Class for testing AsyncService domain_search method."""

    @patch('forager_service.config.AsyncService._perform_request', new_callable=AsyncMock)
    def test_adomain_search(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test domain_search method."""
        domain: str = faker.city()
        HunterService().initialize_async_service('api_key')
        mock_request.side_effect = get_query
        received_data = async_to_sync(HunterService().async_service.domain_search)(domain, limit=8)
        url, kwargs_dict = received_data
        param_dict: dict = kwargs_dict.get('param_dict')
        assert url == 'https://api.hunter.io/v2/domain-search'
        assert param_dict['domain'] == domain
        assert param_dict['limit'] == 8
        assert param_dict['api_key'] == 'api_key'
        assert kwargs_dict['raw'] is False


class TestServiceEmailFinder(object):
    """Class for testing Service email_finder method."""

    @patch('forager_service.config.Service._perform_request')
    def test_email_finder(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test email_finder method."""
        domain: str = faker.city()
        full_name: str = faker.last_name()
        HunterService().initialize_service('some_api_key')
        mock_request.side_effect = get_query
        received_data = HunterService().service.email_finder(domain, full_name=full_name)
        param_dict: dict = received_data[1].get('param_dict')
        assert received_data[0] == 'https://api.hunter.io/v2/email-finder'
        assert param_dict['domain'] == domain
        assert param_dict['full_name'] == full_name
        assert param_dict['api_key'] == 'some_api_key'
        assert received_data[1]['raw'] is False


class TestAsyncServiceEmailFinder(object):
    """Class for testing AsyncService email_finder method."""

    @patch('forager_service.config.AsyncService._perform_request', new_callable=AsyncMock)
    def test_aemail_finder(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test aemail_finder method."""
        domain: str = faker.city()
        first_name: str = faker.first_name()
        last_name: str = faker.last_name()
        HunterService().initialize_async_service('some_api_key')
        mock_request.side_effect = get_query
        received_data = async_to_sync(HunterService().async_service.email_finder)(
            domain,
            first_name=first_name,
            last_name=last_name,
        )
        param_dict: dict = received_data[1].get('param_dict')
        assert received_data[0] == 'https://api.hunter.io/v2/email-finder'
        assert param_dict['domain'] == domain and param_dict['first_name'] == first_name
        assert param_dict['last_name'] == last_name
        assert param_dict['api_key'] == 'some_api_key'
        assert received_data[1]['raw'] is False


class TestServiceVerifyEmail(object):
    """Class for testing Service verify_email method."""

    @patch('forager_service.config.Service._perform_request')
    def test_verify_email(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test verify_email method."""
        email: str = faker.email()
        HunterService().initialize_service('api_key')
        mock_request.side_effect = get_query
        received_data = HunterService().service.verify_email(email)
        param_dict: dict = received_data[1].get('param_dict')
        assert received_data[0] == 'https://api.hunter.io/v2/email-verifier'
        assert param_dict['email'] == email
        assert param_dict['api_key'] == 'api_key'
        assert received_data[1]['raw'] is False


class TestAsyncServiceVerifyEmail(object):
    """Class for testing AsyncService verify_email method."""

    @patch('forager_service.config.AsyncService._perform_request', new_callable=AsyncMock)
    def test_averify_email(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test averify_email method."""
        email: str = faker.email()
        HunterService().initialize_async_service('some_api_key')
        mock_request.side_effect = get_query
        rec_data = async_to_sync(HunterService().async_service.verify_email)(email)
        param_dict: dict = rec_data[1].get('param_dict')
        assert rec_data[0] == 'https://api.hunter.io/v2/email-verifier'
        assert param_dict['email'] == email
        assert param_dict['api_key'] == 'some_api_key'
        assert rec_data[1]['raw'] is False


class TestServiceEmailCount(object):
    """Class for testing Service email_count method."""

    @patch('forager_service.config.Service._perform_request')
    def test_email_count(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test email_count method."""
        domain: str = faker.city()
        email_type: str = faker.random_element(elements=('personal', 'generic'))
        HunterService().initialize_service('some_api_key')
        mock_request.side_effect = get_query
        rec_data = HunterService().service.email_count(domain, email_type=email_type)
        param_dict: dict = rec_data[1].get('param_dict')
        assert rec_data[0] == 'https://api.hunter.io/v2/email-count'
        assert param_dict['domain'] == domain
        assert param_dict['type'] == email_type
        assert rec_data[1]['raw'] is False

    @patch('forager_service.config.AsyncService._perform_request', new_callable=AsyncMock)
    def test_async_email_count(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test aemail_finder method."""
        domain: str = faker.city()
        api_key: str = faker.pystr(min_chars=3)
        HunterService().initialize_async_service(api_key)
        mock_request.side_effect = get_query
        received_data = async_to_sync(HunterService().async_service.email_count)(domain)
        url, kwargs_dict = received_data
        assert url == 'https://api.hunter.io/v2/email-count'
        assert kwargs_dict.get('param_dict')['domain'] == domain
        assert kwargs_dict['raw'] is False
