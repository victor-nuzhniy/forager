"""Module for forager_service utils."""
import pytest
from faker import Faker

from forager_service.exceptions import ArgumentValidationError
from forager_service.services import create_and_validate_params


class TestCreateAdnValidateParams(object):
    """Class for testing create_and_validate_params."""

    def test_create_and_validate_params(self, faker: Faker, get_kwargs: dict) -> None:
        """Test create_and_validate_params."""
        operation_type: str = faker.random_element(
            elements=("email-count", "email-verifier", "email-finder", "domain-search"),
        )
        kwargs: dict = get_kwargs.get(operation_type)
        received_data = create_and_validate_params(operation_type, **kwargs)
        for key, param_value in kwargs.items():
            assert received_data[key] == param_value

    def test_create_and_validate_params_some_empty(self, faker: Faker, get_kwargs: dict) -> None:
        """Test create_and_validate_params."""
        operation_type: str = faker.random_element(elements=("email-count", "email-finder", "domain-search"))
        kwargs: dict = get_kwargs.get(operation_type)
        key = faker.random_element(elements=kwargs.keys())
        if key not in {"domain", "company"}:
            kwargs[key] = None
        received_data = create_and_validate_params(operation_type, **kwargs)
        for key_value in kwargs.items():
            if key_value[1] is None:
                assert key_value[0] not in received_data
            else:
                assert received_data[key_value[0]] == key_value[1]

    def test_create_and_validate_params_error(self, faker: Faker, get_kwargs: dict) -> None:
        """Test create_and_validate_params."""
        operation_type: str = faker.random_element(
            elements=("email-count", "email-verifier", "email-finder", "domain-search"),
        )
        kwargs: dict = get_kwargs.get(operation_type)
        key = faker.random_element(elements=kwargs.keys())
        kwargs[key] = set()
        with pytest.raises(ArgumentValidationError):
            create_and_validate_params(operation_type, **kwargs)

    def test_create_and_validate_par_error_req_arg(
        self,
        faker: Faker,
        get_kwargs: dict,
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

    def test_create_and_validate_par_err_req(self, faker: Faker, get_kwargs: dict) -> None:
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
