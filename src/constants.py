"""Constants for Forager project."""
from src.validators import Validators

VALIDATORS = {
    "required_arguments": (Validators.validate_required_arguments,),
    "domain": (Validators.validate_str,),
    "company": (Validators.validate_str,),
    "limit": (Validators.validate_int,),
    "offset": (Validators.validate_int,),
    "email_type": (Validators.validate_str, Validators.validate_str),
    "seniority": (Validators.validate_str, Validators.validate_seniority),
    "department": (Validators.validate_str, Validators.validate_department),
    "required_field": (Validators.validate_str, Validators.validate_required_field),
    "first_name": (Validators.validate_str,),
    "last_name": (Validators.validate_str,),
    "full_name": (Validators.validate_str,),
    "max_duration": (Validators.validate_int, Validators.validate_max_duration),
}
