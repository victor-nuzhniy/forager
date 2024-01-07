"""Pytest fixtures for tests forager_service module."""
from typing import Any

import pytest
from faker import Faker


@pytest.fixture
def get_kwargs(faker: Faker) -> dict:
    """Create kwargs arguments for testing utils create_and_validate_params."""
    domain_search_dict: dict = {}
    email_finder_dict: dict = {}
    email_count_dict: dict = {}
    for elem in faker.random_choices(elements=('domain', 'company')):
        domain_search_dict[elem] = faker.city()
        email_finder_dict[elem] = faker.city()
        email_count_dict[elem] = faker.city()
    domain_search_dict['limit'] = faker.random_int(min=3)
    domain_search_dict['offset'] = faker.random_int()
    domain_search_dict['type'] = faker.random_element(elements=('personal', 'generic'))
    email_count_dict['type'] = domain_search_dict['type']
    domain_search_dict['seniority'] = faker.random_element(
        elements=(
            'junior',
            'senior',
            'executive',
            'junior, senior',
            'senior, junior, executive',
        ),
    )
    domain_search_dict['department'] = ', '.join(
        faker.random_choices(
            elements=(
                'executive',
                'it',
                'finance',
                'management',
                'sales',
                'legal',
                'support',
                'hr',
                'marketing',
                'communication',
            ),
        ),
    )
    domain_search_dict['required_field'] = ', '.join(
        faker.random_choices(
            elements=(
                'full_name',
                'position',
                'phone_number',
            ),
        ),
    )
    email_finder_dict['first_name'] = faker.first_name()
    email_finder_dict['last_name'] = faker.last_name()
    email_finder_dict['full_name'] = faker.last_name()
    high_limit: int = 20
    email_finder_dict['max_duration'] = faker.random_int(min=3, max=high_limit)
    return {
        'domain-search': domain_search_dict,
        'email-finder': email_finder_dict,
        'email-verifier': {'email': faker.email()},
        'email-count': email_count_dict,
    }


def get_query(some_variable: Any, **kwargs: Any) -> tuple:
    """Return given arguments."""
    return some_variable, kwargs
