"""Module for forager_service utils."""
import pytest
from faker import Faker

from forager_service.exceptions import ArgumentValidationError
from forager_service.utils import create_and_validate_params, validate_storage_key


class TestCreateAdnValidateParams:
    """Class for testing create_and_validate_params."""

    def test_create_and_validate_params(self, faker: Faker, get_kwargs: dict) -> None:
        """Test create_and_validate_params."""
        kwargs: dict = get_kwargs
        operation_type: str = faker.random_element(
            elements=("email-count", "email_finder", "domain_search")
        )
        result = create_and_validate_params(operation_type, **kwargs)
        for key, value in kwargs.items():
            assert result[key] == value

    def test_create_and_validate_params_some_empty(
        self, faker: Faker, get_kwargs: dict
    ) -> None:
        """Test create_and_validate_params."""
        kwargs: dict = get_kwargs
        number = faker.random_int(max=len(kwargs) - 1)
        for i, key in enumerate(kwargs):
            if i == number or i == number - 2:
                kwargs[key] = None
        operation_type: str = faker.random_element(
            elements=("email-count", "email_finder", "domain_search")
        )
        result = create_and_validate_params(operation_type, **kwargs)
        for key, value in kwargs.items():
            if value is None:
                assert key not in result
            else:
                assert result[key] == value

    def test_create_and_validate_params_error(
        self, faker: Faker, get_kwargs: dict
    ) -> None:
        """Test create_and_validate_params."""
        kwargs: dict = get_kwargs
        number = faker.random_int(max=len(kwargs) - 1)
        for i, key in enumerate(kwargs):
            if i == number:
                kwargs[key] = set()
        operation_type: str = faker.random_element(
            elements=("email-count", "email_finder", "domain_search")
        )
        with pytest.raises(ArgumentValidationError):
            create_and_validate_params(operation_type, **kwargs)

    def test_create_and_validate_params_error_required_arguments_email_finder(
        self, faker: Faker, get_kwargs: dict
    ) -> None:
        """Test create_and_validate_params."""
        kwargs: dict = get_kwargs
        elements = faker.random_element(
            elements=[("full_name", "first_name"), ("full_name", "last_name")]
        )
        for elem in elements:
            if kwargs.get(elem):
                kwargs[elem] = None
        operation_type: str = "email-finder"
        with pytest.raises(ArgumentValidationError):
            create_and_validate_params(operation_type, **kwargs)

    def test_create_and_validate_params_error_required_arguments(
        self, faker: Faker, get_kwargs: dict
    ) -> None:
        """Test create_and_validate_params."""
        kwargs: dict = get_kwargs
        elements = ("company", "domain")
        for elem in elements:
            if kwargs.get(elem) is not None:
                kwargs[elem] = None
        operation_type: str = faker.random_element(
            elements=("email-count", "email-finder", "domain-search")
        )
        with pytest.raises(ArgumentValidationError):
            create_and_validate_params(operation_type, **kwargs)


class TestValidateStorageKey:
    """Class for testing validate_storage_key method."""

    def test_validate_storage_key(self, faker: Faker) -> None:
        """Test validate_storage_key."""
        argument: str = faker.pystr(min_chars=3, max_chars=10)
        validate_storage_key(argument)

    def test_validate_storage_key_error(self, faker: Faker) -> None:
        """Test validate_storage_key, error case."""
        argument: int = faker.random_int()
        with pytest.raises(ArgumentValidationError) as ex_info:
            validate_storage_key(argument)
        assert str(ex_info.value) == "argument has wrong type."
