"""Module for testing forager_service validators."""
import pytest
from faker import Faker

from forager_service.exceptions import ArgumentValidationError
from forager_service.validators import kwargs_validators, special_validators


class TestValidatorsValidateEmailType(object):
    """Class for testing kwargs_validators validate_email_type method."""

    def test_validate_email_type(self, faker: Faker) -> None:
        """Test validate_email_type."""
        key: str = faker.pystr(min_chars=3, max_chars=8)
        param_value: str = faker.random_element(elements=("personal", "generic"))
        kwargs_validators.validate_email_type(key, param_value)

    def test_validate_email_type_error(self, faker: Faker) -> None:
        """Test validate_email_type, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=6)
        param_value: str = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            kwargs_validators.validate_email_type(key, param_value)
            assert str(ex_info.value) == "{key} has wrong value.".format(key=key)


class TestValidatorsValidateSeniority(object):
    """Class for testing kwargs_validators validate_seniority method."""

    def test_validate_seniority(self, faker: Faker) -> None:
        """Test validate_seniority."""
        key: str = faker.pystr(min_chars=3, max_chars=8)
        param_value: str = faker.random_element(
            elements=(
                "junior",
                "senior",
                "executive",
                "junior, senior",
                "senior, junior, executive",
            ),
        )
        kwargs_validators.validate_seniority(key, param_value)

    def test_validate_seniority_error(self, faker: Faker) -> None:
        """Test validate_seniority, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: str = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            kwargs_validators.validate_seniority(key, param_value)
            assert str(ex_info.value) == "{key} has wrong value.".format(key=key)


class TestValidatorsValidateDepartment(object):
    """Class for testing kwargs_validators validate_department method."""

    def test_validate_department(self, faker: Faker) -> None:
        """Test validate_department."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: str = ", ".join(
            faker.random_choices(
                elements=(
                    "executive",
                    "it",
                    "finance",
                    "management",
                    "sales",
                    "legal",
                    "support",
                    "hr",
                    "marketing",
                    "communication",
                ),
            ),
        )
        kwargs_validators.validate_department(key, param_value)

    def test_validate_department_error(self, faker: Faker) -> None:
        """Test validate_department, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: str = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            kwargs_validators.validate_department(key, param_value)
            assert str(ex_info.value) == "{key} has wrong value.".format(key=key)


class TestValidatorsValidateRequiredField(object):
    """Class for testing kwargs_validators validate_required_field method."""

    def test_validate_required_field(self, faker: Faker) -> None:
        """Test validate_required_field."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: str = ", ".join(
            faker.random_choices(
                elements=(
                    "full_name",
                    "position",
                    "phone_number",
                ),
            ),
        )
        kwargs_validators.validate_required_field(key, param_value)

    def test_validate_required_field_error(self, faker: Faker) -> None:
        """Test validate_required_field, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        param_value: str = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            kwargs_validators.validate_required_field(key, param_value)
            assert str(ex_info.value) == "{key} has wrong value.".format(key=key)


class TestValidatorsValidateMaxDuration(object):
    """Class for testing kwargs_validators validate_max_duration method."""

    def test_validate_max_duration(self, faker: Faker) -> None:
        """Test validate_max_duration."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        high_limit: int = 20
        param_value: int = faker.random_int(min=3, max=high_limit)
        kwargs_validators.validate_max_duration(key, param_value)

    def test_validate_max_duration_error(self, faker: Faker) -> None:
        """Test validate_max_duration, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        low_limit: int = 21
        param_value: int = faker.random_int(min=low_limit, max=1000)
        with pytest.raises(ArgumentValidationError) as ex_info:
            kwargs_validators.validate_max_duration(key, param_value)
            assert str(ex_info.value) == "{key} should be in range from 3 to 20.".format(key=key)


class TestValidatorsValidateRequiredArguments(object):
    """Class for testing special_validators validate_required_arguments method."""

    def test_validate_required_arguments(self, faker: Faker) -> None:
        """Test validate_required_arguments."""
        param_dict: dict = {}
        key: str = faker.random_element(elements=("domain-search", "email-finder", "email-count"))
        for element in faker.random_choices(elements=("domain", "company")):
            param_dict[element] = faker.city()
        if key == "email-finder":
            elements = faker.random_element(elements=[("full_name",), ("first_name", "last_name")])
            for elem in elements:
                param_dict[elem] = faker.city()
        special_validators.validate_required_arguments(key, param_dict)

    def test_validate_required_arguments_error(self, faker: Faker) -> None:
        """Test validate_required_arguments, error case."""
        param_dict: dict = {}
        key: str = faker.random_element(elements=("domain-search", "email-finder", "email-count"))
        with pytest.raises(ArgumentValidationError) as ex_info:
            special_validators.validate_required_arguments(key, param_dict)
            assert str(ex_info.value) == "For {key} operation should be defined domain or company".format(key=key)


class TestValidateEmailFinderRequiredArgument(object):
    """Class for testing special_validators validate_email_finder_required_argument method."""

    def test_validate_email_finder_required_argument(self, faker: Faker) -> None:
        """Test validate_email_finder_required_argument."""
        param_dict: dict = {}
        key: str = "email-finder"
        elements = faker.random_element(elements=[("full_name",), ("first_name", "last_name")])
        for elem in elements:
            param_dict[elem] = faker.city()
        special_validators.validate_email_finder_required_argument(key, param_dict)

    def test_validate_required_arg_err_email_finder(self, faker: Faker) -> None:
        """Test validate_email_finder_required_argument."""
        param_dict: dict = {}
        key: str = "email-finder"
        param_dict[faker.random_element(elements=("first_name", "last_name", "11"))] = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            special_validators.validate_email_finder_required_argument(key, param_dict)
            assert str(ex_info.value) == "At least first_name and last_name or full_name should be in param_dict."
