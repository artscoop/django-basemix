# coding: utf-8
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PriorityBase(models.Model):
    """
    Base class for models that can be ordered by priority

    The mixin adds a new field named ``priority``, which is an
    integer between `0` and `100` (enforced by field type and a
    validator)

    Contrary to the UNIX nonsense where a high nice priority is -20
    and a low nice priority is 19, we use the intuitive notion of
    priority here: a high number is akin to a high priority.

    Attributes:
        :priority: priority of the object as an integer, ``0..100``
    """

    # Fields
    priority = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)], verbose_name=_("priority"))

    # Metadata
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """ Save the object to the database """
        super(self.__class__, self).save(*args, **kwargs)
