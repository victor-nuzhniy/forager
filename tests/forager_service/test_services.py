"""Module for forager_service utils."""
import pytest
from faker import Faker

from forager_service.exceptions import ArgumentValidationError
from forager_service.services import create_and_validate_params


class TestCreateAdnValidateParams:
    """Class for testing create_and_validate_params."""

    def test_create_and_validate_params(self, faker: Faker, get_kwargs: dict) -> None:
        """Test create_and_validate_params."""
        kwargs_dict: dict = get_kwargs
        operation_type: str = faker.random_element(
            elements=("email-count", "email-verifier", "email-finder", "domain-search")
        )
        kwargs: dict = kwargs_dict.get(operation_type)
        result = create_and_validate_params(operation_type, **kwargs)
        for key, value in kwargs.items():
            assert result[key] == value

    def test_create_and_validate_params_some_empty(self, faker: Faker, get_kwargs: dict) -> None:
        """Test create_and_validate_params."""
        kwargs_dict: dict = get_kwargs
        operation_type: str = faker.random_element(elements=("email-count", "email-finder", "domain-search"))
        kwargs: dict = kwargs_dict.get(operation_type)
        number = faker.random_int(max=len(kwargs) - 1)
        for i, key in enumerate(kwargs):
            if i == number and key not in {"domain", "company"}:
                kwargs[key] = None
        result = create_and_validate_params(operation_type, **kwargs)
        for key, value in kwargs.items():
            if value is None:
                assert key not in result
            else:
                assert result[key] == value

    def test_create_and_validate_params_error(self, faker: Faker, get_kwargs: dict) -> None:
        """Test create_and_validate_params."""
        kwargs_dict: dict = get_kwargs
        operation_type: str = faker.random_element(
            elements=("email-count", "email-verifier", "email-finder", "domain-search")
        )
        kwargs: dict = kwargs_dict.get(operation_type)
        number = faker.random_int(max=len(kwargs) - 1)
        for i, key in enumerate(kwargs):
            if i == number:
                kwargs[key] = set()
        with pytest.raises(ArgumentValidationError):
            create_and_validate_params(operation_type, **kwargs)

    def test_create_and_validate_params_error_required_arguments_email_finder(
        self, faker: Faker, get_kwargs: dict
    ) -> None:
        """Test create_and_validate_params."""
        kwargs_dict: dict = get_kwargs
        operation_type: str = "email-finder"
        kwargs: dict = kwargs_dict.get(operation_type)
        elements = faker.random_element(elements=[("full_name", "first_name"), ("full_name", "last_name")])
        for elem in elements:
            if kwargs.get(elem):
                kwargs[elem] = None
        with pytest.raises(ArgumentValidationError):
            create_and_validate_params(operation_type, **kwargs)

    def test_create_and_validate_params_error_required_arguments(self, faker: Faker, get_kwargs: dict) -> None:
        """Test create_and_validate_params."""
        kwargs_dict: dict = get_kwargs
        operation_type: str = faker.random_element(elements=("email-count", "email-finder", "domain-search"))
        kwargs: dict = kwargs_dict.get(operation_type)
        elements = ("company", "domain")
        for elem in elements:
            if kwargs.get(elem) is not None:
                kwargs[elem] = None
        with pytest.raises(ArgumentValidationError):
            create_and_validate_params(operation_type, **kwargs)
