# coding: utf-8
from datetime import timedelta

from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class CreationBase(models.Model):
    """
    Base class for models with a creation date

    The mixin provides a set of handy methods to manage the status
    of the creation date. By default, the field is not setup to
    have an index defined on it. However, in Django 1.11, you can
    define an index on the field ``creation_date``

    Attributes:
        :creation_date: date of creation of the object
    """

    # Fields
    creation_date = models.DateTimeField(default=now, verbose_name=_("creation"))

    # Metadata
    class Meta:
        abstract = True

    # Getter and properties
    def is_new(self, hours=168):
        """
        Returns whether this instance was created recently

        :param hours: Minimum hours to consider the instance not new anymore.
            Default value is one week (`168`).
        :return: ``True`` if the instance is recent enough
        :rtype: bool

        """
        oldest_date = now() - timedelta(hours=hours)
        return self.creation_date > oldest_date
