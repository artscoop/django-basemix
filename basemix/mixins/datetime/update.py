# coding: utf-8
from datetime import timedelta

from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class UpdateBase(models.Model):
    """
    Base class for models with an update date

    The mixin provides a set of handy methods to manage the status
    of the update time. By default, the field is not setup to
    have an index defined on it. However, in Django 1.11, you can
    define an index on the field ``update_date``
    """

    # Fields
    update_date = models.DateTimeField(auto_now=True, verbose_name=_("update time"))

    # Metadata
    class Meta:
        abstract = True

    # Getter and properties
    def is_updated_recently(self, hours=168):
        """
        Returns whether this instance was updated recently

        :param hours: Minimum hours to consider the instance not fresh anymore.
            Default value is one week (`168`).
        :return: ``True`` if the instance update time is recent enough
        :rtype: bool
        """
        oldest_date = now() - timedelta(hours=hours)
        return self.update_date > oldest_date
