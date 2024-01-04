"""Validators for arguments."""

from src.constants import SERVICES_KWARGS
from src.exceptions import ArgumentValidationError


class Validators:
    """Class with method for kwargs validations."""

    @staticmethod
    def validate_kwargs_list(key: str, values_dict: dict) -> None:
        """Validate kwargs list."""
        kwargs_set: set = SERVICES_KWARGS.get(key)
        for k in values_dict:
            if k not in kwargs_set:
                raise ArgumentValidationError(
                    f"{k} not in allowed arguments list for {key} operation."
                )

    @staticmethod
    def validate_str(key: str, value: str) -> None:
        """Validate value is str type."""
        if not isinstance(value, str):
            raise ArgumentValidationError(f"{key} has wrong type.")

    @staticmethod
    def validate_int(key: str, value: int) -> None:
        """Validate value is int type."""
        if not isinstance(value, int):
            raise ArgumentValidationError(f"{key} has wrong type.")

    @staticmethod
    def validate_email_type(key: str, value: str) -> None:
        """Validate email type."""
        if value not in {"personal", "generic"}:
            raise ArgumentValidationError(f"{key} has wrong value.")

    @staticmethod
    def validate_seniority(key: str, value: str) -> None:
        """Validate seniority kwarg."""
        value_list: list = value.split(", ")
        for elem in value_list:
            if elem not in {"junior", "senior", "executive"}:
                raise ArgumentValidationError(f"{key} has wrong value.")

    @staticmethod
    def validate_department(key: str, value: str) -> None:
        """Validate department value."""
        value_list: list = value.split(", ")
        for elem in value_list:
            if elem not in {
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
            }:
                raise ArgumentValidationError(f"{key} has wrong value.")

    @staticmethod
    def validate_required_field(key: str, value: str) -> None:
        """Validate required field argument."""
        value_list: list = value.split(", ")
        for elem in value_list:
            if elem not in {"full_name", "position", "phone_number"}:
                raise ArgumentValidationError(f"{key} has wrong value.")

    @staticmethod
    def validate_raw(key: str, value: bool) -> None:
        """Validate raw argument."""
        if not isinstance(value, bool):
            raise ArgumentValidationError(f"{key} is wrong type.")
