"""Pytest fixtures for tests forager_service module."""
import pytest
from faker import Faker


@pytest.fixture
def get_kwargs(faker: Faker) -> dict:
    """Create kwargs arguments for testing utils create_and_validate_params."""
    kwargs: dict = dict()
    elements: list = faker.random_choices(elements=("domain", "company"))
    for elem in elements:
        kwargs[elem] = faker.city()
    limit: int = faker.random_int(min=3, max=20)
    kwargs["limit"] = limit
    offset: int = faker.random_int()
    kwargs["offset"] = offset
    email_type: str = faker.random_element(elements=("personal", "generic"))
    kwargs["type"] = email_type
    seniority: str = faker.random_element(
        elements=(
            "junior",
            "senior",
            "executive",
            "junior, senior",
            "senior, junior, executive",
        )
    )
    kwargs["seniority"] = seniority
    department: str = ", ".join(
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
    kwargs["department"] = department
    required_field: str = ", ".join(
        faker.random_choices(
            elements=(
                "full_name",
                "position",
                "phone_number",
            )
        )
    )
    kwargs["required_field"] = required_field
    first_name: str = faker.first_name()
    kwargs["first_name"] = first_name
    last_name: str = faker.last_name()
    kwargs["last_name"] = last_name
    full_name: str = f"{faker.first_name()} {faker.last_name()}"
    kwargs["full_name"] = full_name
    max_duration: int = faker.random_int(min=3, max=20)
    kwargs["max_duration"] = max_duration
    email: str = faker.email()
    kwargs["email"] = email
    argument: str = faker.city()
    kwargs["argument"] = argument
    return kwargs
