"""Module for testing CommonValidators."""
import pytest
from faker import Faker

from forager_forward.common.exceptions import ArgumentValidationError
from forager_forward.common.validators import common_validators


class TestValidatorsValidateStr(object):
    """Class for testing common_validators validate_str method."""

    def test_validate_str(self, faker: Faker) -> None:
        """Test validate_str."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: str = faker.pystr(min_chars=3, max_chars=7)
        common_validators.validate_str(key, param_value)

    def test_validate_str_error(self, faker: Faker) -> None:
        """Test validate_str, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: int = faker.random_int()
        with pytest.raises(ArgumentValidationError) as ex_info:
            common_validators.validate_str(key, param_value)
            assert str(ex_info.value) == '{key} has wrong type.'.format(key=key)


class TestValidatorsValidateInt(object):
    """Class for testing common_validators validate_int method."""

    def test_validate_int(self, faker: Faker) -> None:
        """Test validate_int."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: int = faker.random_int()
        common_validators.validate_int(key, param_value)

    def test_validate_int_error(self, faker: Faker) -> None:
        """Test validate_int, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: str = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            common_validators.validate_int(key, param_value)
            assert str(ex_info.value) == '{key} has wrong type.'.format(key=key)


class TestValidatorsValidateEmail(object):
    """Class for testing common_validators validate_email method."""

    def test_validate_email(self, faker: Faker) -> None:
        """Test validate_email."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: str = faker.email()
        common_validators.validate_email(key, param_value)

    def test_validate_email_error(self, faker: Faker) -> None:
        """Test validate_email, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: str = faker.pystr(min_chars=3)
        with pytest.raises(ArgumentValidationError) as ex_info:
            common_validators.validate_email(key, param_value)
            assert str(ex_info.value) == '{key} has invalid value.'.format(key=key)
