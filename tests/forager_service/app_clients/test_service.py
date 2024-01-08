"""Module for testing Client functionality."""
from unittest.mock import MagicMock, patch

import pytest
from faker import Faker

from forager_forward.client_initializer import ClientInitializer
from forager_forward.common.exceptions import ArgumentValidationError
from tests.forager_service.conftest import get_query


class TestClientDomainSearch(object):
    """Class for testing Client domain_search method."""

    @patch('forager_forward.app_clients.client.Client._perform_request')
    def test_domain_search(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test domain_search method."""
        domain: str = faker.city()
        api_key: str = 'some_key'
        ClientInitializer().initialize_client(api_key)
        mock_request.side_effect = get_query
        received_data = ClientInitializer().service.domain_search(domain)
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
        ClientInitializer().initialize_client(api_key)
        with pytest.raises(ArgumentValidationError):
            ClientInitializer().service.domain_search(domain)


class TestClientEmailFinder(object):
    """Class for testing Client email_finder method."""

    @patch('forager_forward.app_clients.client.Client._perform_request')
    def test_email_finder(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test email_finder method."""
        domain: str = faker.city()
        full_name: str = faker.last_name()
        ClientInitializer().initialize_client('some_api_key')
        mock_request.side_effect = get_query
        received_data = ClientInitializer().service.email_finder(domain, full_name=full_name)
        param_dict: dict = received_data[1].get('param_dict')
        assert received_data[0] == 'https://api.hunter.io/v2/email-finder'
        assert param_dict['domain'] == domain
        assert param_dict['full_name'] == full_name
        assert param_dict['api_key'] == 'some_api_key'
        assert received_data[1]['raw'] is False


class TestClientVerifyEmail(object):
    """Class for testing Client verify_email method."""

    @patch('forager_forward.app_clients.client.Client._perform_request')
    def test_verify_email(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test verify_email method."""
        email: str = faker.email()
        ClientInitializer().initialize_client('api_key')
        mock_request.side_effect = get_query
        received_data = ClientInitializer().service.verify_email(email)
        param_dict: dict = received_data[1].get('param_dict')
        assert received_data[0] == 'https://api.hunter.io/v2/email-verifier'
        assert param_dict['email'] == email
        assert param_dict['api_key'] == 'api_key'
        assert received_data[1]['raw'] is False


class TestClientEmailCount(object):
    """Class for testing Client email_count method."""

    @patch('forager_forward.app_clients.client.Client._perform_request')
    def test_email_count(
        self,
        mock_request: MagicMock,
        faker: Faker,
    ) -> None:
        """Test email_count method."""
        domain: str = faker.city()
        email_type: str = faker.random_element(elements=('personal', 'generic'))
        ClientInitializer().initialize_client('some_api_key')
        mock_request.side_effect = get_query
        rec_data = ClientInitializer().service.email_count(domain, email_type=email_type)
        param_dict: dict = rec_data[1].get('param_dict')
        assert rec_data[0] == 'https://api.hunter.io/v2/email-count'
        assert param_dict['domain'] == domain
        assert param_dict['type'] == email_type
        assert rec_data[1]['raw'] is False
