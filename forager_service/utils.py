"""Utilities for Forager project."""
from __future__ import annotations

from forager_service.validators import VALIDATORS, validate_arguments


def create_and_validate_params(operation_type: str, **kwargs) -> dict:
    """
    Add params from keyword arguments.

    :param operation_type: str Name of request operation.
    :param kwargs: dict Key word arguments for particular operation.
    :return: dict Params for request.
    """
    validate_arguments(operation_type, kwargs)
    params: dict = dict()
    for key, value in kwargs.items():
        if value is not None:
            for validator in VALIDATORS.get(key):
                validator(key, value)
            params[key] = value
    for validator in VALIDATORS.get("required_arguments"):
        validator(operation_type, params)
    return params
