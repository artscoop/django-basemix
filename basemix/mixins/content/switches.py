# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Visible(models.Model):
    """
    Base class for models with a visibility field

    This mixin adds one field named ``is_visible``

    Attributes:
        :is_visible: visibility of the item. Non-nullable
    """

    # Fields
    is_visible = models.BooleanField(default=True, verbose_name=_("visibility"))

    # Metadata
    class Meta:
        abstract = True


class Active(models.Model):
    """
    Base class for models that can be enabled/disabled

    This mixin adds one field named ``is_active``

    Attributes:
        :is_active: defines whether the item is active or not. Non-nullable
    """

    # Fields
    is_active = models.BooleanField(default=True, verbose_name=_("activity"))

    # Metadata
    class Meta:
        abstract = True
