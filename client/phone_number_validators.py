from django.core.exceptions import ValidationError
from phonenumber_field.phonenumber import to_python
from phonenumbers.phonenumberutil import is_possible_number
from enum import Enum


class NumberErrorCode(Enum):
    INVALID = "invalid"


def validate_possible_number(phone, country=None):
    phone_number = to_python(phone, country)
    if (
            phone_number
            and not is_possible_number(phone_number)
            or not phone_number.is_valid()
    ):
        raise ValidationError(
            "The phone number entered is not valid.", code=NumberErrorCode.INVALID
        )
    return phone_number
