"""Module for testing forager_service validators."""
import pytest
from faker import Faker

from forager_service.exceptions import ArgumentValidationError
from forager_service.validators import Validators


class TestValidatorsValidateStr:
    """Class for testing Validators validate_str method."""

    def test_validate_str(self, faker: Faker) -> None:
        """Test validate_str."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = faker.pystr(min_chars=3, max_chars=7)
        Validators.validate_str(key, value)

    def test_validate_str_error(self, faker: Faker) -> None:
        """Test validate_str, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: int = faker.random_int()
        with pytest.raises(ArgumentValidationError) as ex_info:
            Validators.validate_str(key, value)
        assert str(ex_info.value) == f"{key} has wrong type."


class TestValidatorsValidateInt:
    """Class for testing Validators validate_int method."""

    def test_validate_int(self, faker: Faker) -> None:
        """Test validate_int."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: int = faker.random_int()
        Validators.validate_int(key, value)

    def test_validate_int_error(self, faker: Faker) -> None:
        """Test validate_int, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            Validators.validate_int(key, value)
        assert str(ex_info.value) == f"{key} has wrong type."


class TestValidatorsValidateEmailType:
    """Class for testing Validators validate_email_type method."""

    def test_validate_email_type(self, faker: Faker) -> None:
        """Test validate_email_type."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = faker.random_element(elements=("personal", "generic"))
        Validators.validate_email_type(key, value)

    def test_validate_email_type_error(self, faker: Faker) -> None:
        """Test validate_email_type, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            Validators.validate_email_type(key, value)
        assert str(ex_info.value) == f"{key} has wrong value."


class TestValidatorsValidateSeniority:
    """Class for testing Validators validate_seniority method."""

    def test_validate_seniority(self, faker: Faker) -> None:
        """Test validate_seniority."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = faker.random_element(
            elements=(
                "junior",
                "senior",
                "executive",
                "junior, senior",
                "senior, junior, executive",
            )
        )
        Validators.validate_seniority(key, value)

    def test_validate_seniority_error(self, faker: Faker) -> None:
        """Test validate_seniority, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            Validators.validate_seniority(key, value)
        assert str(ex_info.value) == f"{key} has wrong value."


class TestValidatorsValidateDepartment:
    """Class for testing Validators validate_department method."""

    def test_validate_department(self, faker: Faker) -> None:
        """Test validate_department."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = ", ".join(
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
                )
            )
        )
        Validators.validate_department(key, value)

    def test_validate_department_error(self, faker: Faker) -> None:
        """Test validate_department, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            Validators.validate_department(key, value)
        assert str(ex_info.value) == f"{key} has wrong value."


class TestValidatorsValidateRequiredField:
    """Class for testing Validators validate_required_field method."""

    def test_validate_required_field(self, faker: Faker) -> None:
        """Test validate_required_field."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = ", ".join(
            faker.random_choices(
                elements=(
                    "full_name",
                    "position",
                    "phone_number",
                )
            )
        )
        Validators.validate_required_field(key, value)

    def test_validate_required_field_error(self, faker: Faker) -> None:
        """Test validate_required_field, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            Validators.validate_required_field(key, value)
        assert str(ex_info.value) == f"{key} has wrong value."


class TestValidatorsValidateMaxDuration:
    """Class for testing Validators validate_max_duration method."""

    def test_validate_max_duration(self, faker: Faker) -> None:
        """Test validate_max_duration."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: int = faker.random_int(min=3, max=20)
        Validators.validate_max_duration(key, value)

    def test_validate_max_duration_error(self, faker: Faker) -> None:
        """Test validate_max_duration, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: int = faker.random_int(min=21)
        with pytest.raises(ArgumentValidationError) as ex_info:
            Validators.validate_max_duration(key, value)
        assert str(ex_info.value) == f"{key} should be in range from 3 to 20."


class TestValidatorsValidateEmail:
    """Class for testing Validators validate_email method."""

    def test_validate_email(self, faker: Faker) -> None:
        """Test validate_email."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = faker.email()
        Validators.validate_email(key, value)

    def test_validate_email_error(self, faker: Faker) -> None:
        """Test validate_email, error case."""
        key: str = faker.pystr(min_chars=3, max_chars=7)
        value: str = faker.pystr(min_chars=3)
        with pytest.raises(ArgumentValidationError) as ex_info:
            Validators.validate_email(key, value)
        assert str(ex_info.value) == f"{key} has invalid value."


class TestValidatorsValidateRequiredArguments:
    """Class for testing Validators validate_required_arguments method."""

    def test_validate_required_arguments(self, faker: Faker) -> None:
        """Test validate_required_arguments."""
        params: dict = dict()
        key: str = faker.random_element(
            elements=("domain-search", "email-finder", "email-count")
        )
        for elem in faker.random_choices(elements=("domain", "company")):
            params[elem] = faker.city()
        if key == "email-finder":
            elements = faker.random_element(
                elements=[("full_name",), ("first_name", "last_name")]
            )
            for elem in elements:
                params[elem] = faker.city()
        Validators.validate_required_arguments(key, params)

    def test_validate_required_arguments_error(self, faker: Faker) -> None:
        """Test validate_required_arguments, error case."""
        params: dict = dict()
        key: str = faker.random_element(
            elements=("domain-search", "email-finder", "email-count")
        )
        with pytest.raises(ArgumentValidationError) as ex_info:
            Validators.validate_required_arguments(key, params)
        assert (
            str(ex_info.value)
            == f"For {key} operation should be defined domain or company"
        )

    def test_validate_required_arguments_error_email_finder(self, faker: Faker) -> None:
        """Test validate_required_arguments."""
        params: dict = dict()
        key: str = "email-finder"
        for elem in faker.random_choices(elements=("domain", "company")):
            params[elem] = faker.city()
        params[
            faker.random_element(elements=("first_name", "last_name", "11"))
        ] = faker.city()
        with pytest.raises(ArgumentValidationError) as ex_info:
            Validators.validate_required_arguments(key, params)
        assert (
            str(ex_info.value) == "At least first_name and last_name or full_name "
            "should be in params."
        )
