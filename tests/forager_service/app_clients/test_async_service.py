"""Module for testing AsyncClient functionality."""
from unittest.mock import AsyncMock, patch

from asgiref.sync import async_to_sync
from faker import Faker

from forager.client_initializer import ClientInitializer
from tests.forager_service.conftest import get_query


class TestAsyncClientDomainSearch(object):
    """Class for testing AsyncClient domain_search method."""

    @patch('forager.app_clients.async_client.AsyncClient._perform_request', new_callable=AsyncMock)
    def test_adomain_search(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test domain_search method."""
        domain: str = faker.city()
        ClientInitializer().initialize_async_client('api_key')
        mock_request.side_effect = get_query
        received_data = async_to_sync(ClientInitializer().async_service.domain_search)(domain, limit=8)
        url, kwargs_dict = received_data
        param_dict: dict = kwargs_dict.get('param_dict')
        assert url == 'https://api.hunter.io/v2/domain-search'
        assert param_dict['domain'] == domain
        assert param_dict['limit'] == 8
        assert param_dict['api_key'] == 'api_key'
        assert kwargs_dict['raw'] is False


class TestAsyncClientEmailFinder(object):
    """Class for testing AsyncClient email_finder method."""

    @patch('forager.app_clients.async_client.AsyncClient._perform_request', new_callable=AsyncMock)
    def test_aemail_finder(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test aemail_finder method."""
        domain: str = faker.city()
        first_name: str = faker.first_name()
        last_name: str = faker.last_name()
        ClientInitializer().initialize_async_client('some_api_key')
        mock_request.side_effect = get_query
        received_data = async_to_sync(ClientInitializer().async_service.email_finder)(
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


class TestAsyncClientVerifyEmail(object):
    """Class for testing AsyncClient verify_email method."""

    @patch('forager.app_clients.async_client.AsyncClient._perform_request', new_callable=AsyncMock)
    def test_averify_email(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test averify_email method."""
        email: str = faker.email()
        ClientInitializer().initialize_async_client('some_api_key')
        mock_request.side_effect = get_query
        rec_data = async_to_sync(ClientInitializer().async_service.verify_email)(email)
        param_dict: dict = rec_data[1].get('param_dict')
        assert rec_data[0] == 'https://api.hunter.io/v2/email-verifier'
        assert param_dict['email'] == email
        assert param_dict['api_key'] == 'some_api_key'
        assert rec_data[1]['raw'] is False


class TestAsyncClientEmailCount(object):
    """Class for testing AsyncClient email_count method."""

    @patch('forager.app_clients.async_client.AsyncClient._perform_request', new_callable=AsyncMock)
    def test_async_email_count(
        self,
        mock_request: AsyncMock,
        faker: Faker,
    ) -> None:
        """Test aemail_finder method."""
        domain: str = faker.city()
        api_key: str = faker.pystr(min_chars=3)
        ClientInitializer().initialize_async_client(api_key)
        mock_request.side_effect = get_query
        received_data = async_to_sync(ClientInitializer().async_service.email_count)(domain)
        url, kwargs_dict = received_data
        assert url == 'https://api.hunter.io/v2/email-count'
        assert kwargs_dict.get('param_dict')['domain'] == domain
        assert kwargs_dict['raw'] is False
