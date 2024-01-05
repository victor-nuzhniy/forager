"""Utilities for Forager project."""
from __future__ import annotations

from src.constants import VALIDATORS


def create_and_validate_params(operation_type: str, **kwargs) -> dict:
    """
    Add params from keyword arguments.

    :param operation_type: str Name of request operation.
    :param kwargs: dict Key word arguments for particular operation.
    :return: dict Params for request.
    """
    VALIDATORS.get("operation")(operation_type, kwargs)
    params: dict = dict()
    for key, value in kwargs.items():
        for validator in VALIDATORS.get(key):
            validator(key, value)
        params[key] = value
    VALIDATORS.get("required_arguments")(operation_type, params)
    return params