from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def number(password):
    if not any(map(str.isdigit, password)):
        raise ValidationError(
            _("your password must contain at least 1 digit."),
            code="password_no_number",
        )


def lowercase(password):
    if not any(map(str.islower, password)):
        raise ValidationError(
            _("your password must contain at least 1 lowercase letter."),
            code="password_no_lowercase",
        )


def uppercase(password):
    if not any(map(str.isupper, password)):
        raise ValidationError(
            _("your password must contain at least 1 uppercase letter."),
            code="password_no_uppercase",
        )


def symbol(password):
    special_characters = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    if not any(char in special_characters for char in password):
        raise ValidationError(
            _("your password must contain at least 1 special character."),
            code="password_no_symbol",
        )


def length(password):
    if len(password) < 8:
        raise ValidationError(
            _("your password must be at least 8 characters long."),
            code="password_length"
        )
