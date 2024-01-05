"""Constants for Forager project."""
from src.validators import Validators

SERVICES_KWARGS = {
    "domain_search": {
        "domain",
        "company",
        "limit",
        "offset",
        "email_type",
        "seniority",
        "department",
        "required_fields",
    },
}

VALIDATORS = {
    "operation": (Validators.validate_kwargs_list,),
    "required_arguments": (Validators.validate_required_arguments,),
    "domain": (Validators.validate_str,),
    "company": (Validators.validate_str,),
    "limit": (Validators.validate_int,),
    "offset": (Validators.validate_int,),
    "email_type": (Validators.validate_str, Validators.validate_str),
    "seniority": (Validators.validate_str, Validators.validate_seniority),
    "department": (Validators.validate_str, Validators.validate_department),
    "required_field": (Validators.validate_str, Validators.validate_required_field),
}
