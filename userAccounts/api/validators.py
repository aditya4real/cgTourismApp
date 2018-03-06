from __future__ import unicode_literals
from django.core.exceptions import ValidationError as ve1
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.phonenumber import to_python
from django.db import DataError
from rest_framework.compat import unicode_to_repr
from rest_framework.exceptions import ValidationError as ve2
from rest_framework.utils.representation import smart_repr

def qs_exists(queryset):
    try:
        return queryset.exists()
    except (TypeError, ValueError, DataError):
        return False


def qs_filter(queryset, **kwargs):
    try:
        return queryset.filter(**kwargs)
    except (TypeError, ValueError, DataError):
        return queryset.none()

class PhoneNumberValidator(object):
    """
    Validator that corresponds to `unique=True` on a model field.
    Should be applied to an individual field on the serializer.
    """
    message = _('This field must be unique.')

    def __init__(self, queryset, message=None, lookup='exact'):
        self.queryset = queryset
        self.serializer_field = None
        self.message = message or self.message
        self.lookup = lookup

    def set_context(self, serializer_field):
        """
        This hook is called by the serializer instance,
        prior to the validation call being made.
        """
        # Determine the underlying model field name. This may not be the
        # same as the serializer field name if `source=<>` is set.
        self.field_name = serializer_field.source_attrs[-1]
        # Determine the existing instance, if this is an update operation.
        self.instance = getattr(serializer_field.parent, 'instance', None)

    def filter_queryset(self, value, queryset):
        """
        Filter the queryset to all instances matching the given attribute.
        """
        filter_kwargs = {'%s__%s' % (self.field_name, self.lookup): value}
        return qs_filter(queryset, **filter_kwargs)

    def exclude_current_instance(self, queryset):
        """
        If an instance is being updated, then do not include
        that instance itself as a uniqueness conflict.
        """
        if self.instance is not None:
            return queryset.exclude(pk=self.instance.pk)
        return queryset

    def __call__(self, value):
        queryset = self.queryset
        queryset = self.filter_queryset(value, queryset)
        queryset = self.exclude_current_instance(queryset)
        if qs_exists(queryset):
            raise ve2(self.message, code='unique')
        phone_number = to_python(value)
        if phone_number and not phone_number.is_valid():
            raise ve1(
                _('The phone number entered is not valid.'),
                code='invalid_phone_number')

    def __repr__(self):
        return unicode_to_repr('<%s(queryset=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.queryset)
        ))
    
    