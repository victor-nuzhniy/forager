"""Constants for forager_service package."""


OPERATIONS_ARGUMENTS = {
    "domain-search": {"domain", "company", "limit", "offset", "type", "seniority", "department", "required_field"},
    "email-finder": {"domain", "company", "first_name", "last_name", "full_name", "max_duration"},
    "email-verifier": {"email"},
    "email-count": {"domain", "company", "type"},
}
