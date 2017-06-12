# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


class ContentBase(models.Model):
    """
    Base class for models that share content attributes

    The attributes added by this mixin are ``title``, ``description``,
    ``content`` and ``is_visible``.

    Attributes:
        :is_visible: whether the content should be displayed by normal users
        :title: title of the content, at most 192 characters
        :description: most content objects have a description, with an unlimited size
        :content: actual content of the object, with an unlimited size
    """

    # Fields
    is_visible = models.BooleanField(default=True, verbose_name=pgettext_lazy('content', "visible"))
    title = models.CharField(blank=False, max_length=192, verbose_name=_("title"))
    description = models.TextField(blank=True, verbose_name=_("description"))
    content = models.TextField(blank=False, verbose_name=_("content"))

    # Metadata
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """ Save the object to the database """
        super(self.__class__, self).save(*args, **kwargs)
