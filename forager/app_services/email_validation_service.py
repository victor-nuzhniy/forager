"""Service for email validation with result saving to storage."""
from typing import Optional

from forager.common.exceptions import ArgumentValidationError
from forager.common.storage import Storage
from forager.common.validators import validators


class EmailValidationService(object):
    """Class email validation and crud result."""

    _storage: Storage = Storage()

    def create_email_record(self, email: str) -> Optional[bool]:
        """
        Create email record in storage.

        :param email: str Email to create record.
        :return: bool True, if operation was successfull, otherwise False..
        """
        try:
            for validator in validators['email']:
                validator('email', email)
        except ArgumentValidationError:
            self._storage.create(email, False)
            return False
        self._storage.create(email, True)
        return True

    def read_email_record(self, email: str) -> Optional[dict]:
        """
        Read email record from storage.

        :param email: str Email to retrieve info.
        :return: dict Email validation info or None.
        """
        return self._storage.read(email)

    def delete_email_record(self, email: str) -> None:
        """
        Delete email record from storage.

        :param email: str Email to delete.
        :return: None
        """
        self._storage.delete(email)
