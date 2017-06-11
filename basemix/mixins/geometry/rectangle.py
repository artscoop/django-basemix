# coding: utf-8
from django.db import models
from django.utils.translation import pgettext_lazy


class DimensionBase(models.Model):
    """
    Base class for models with a representation of a rectangle

    Classes inheriting from this base model must add two
    fields named ``width`` and ``height`` that must resolve to
    a type than can be parts of arithmetic operations.

    Two model mixins :class:`.DimensionIntBase` and
    :class:`.DimensionFloatBase` already exist for our basic needs.

    """

    # Meta
    class Meta:
        abstract = True

    # Getter and properties
    def get_area(self):
        """
        Gets the area of the rectangle

        :return: Product of the width and height of the rectangle
        :rtype: int or float
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Gets the perimeter of the rectangle

        :return: Twice the sum of height and width
        :rtype: int or float
        """
        return 2 * (self.width + self.height)

    def is_segment(self):
        """
        Returns if the rectangle is actually a segment, but not a point

        :return: True if only one of width and height is zero
        :rtype: bool
        """
        return (self.width == 0) != (self.height == 0)

    def is_point(self):
        """
        Returns if the rectangle is actually a point

        :return: True if width and height are zero
        :rtype: bool
        """
        return not (self.width != 0 or self.height != 0)

    # Setter and Actions
    def set_dimension(self, width, height):
        """
        Sets the dimensions of the rectangle

        :param width: width of the rectangle
        :type width: int or float
        :param height: height of the rectangle
        :type height: int or float
        :return: True if changed, False otherwise
        """
        if width != self.width or height != self.height:
            self.width = width
            self.height = height
            return True
        return False


class DimensionIntBase(DimensionBase):
    """
    Base class for models with a representation of rectangle dimensions

    The model allows for representation of integer dimensions and
    contains two ``PositiveIntegerField`` named ``width`` and ``height``.
    """

    # Fields
    width = models.PositiveIntegerField(default=0, verbose_name=pgettext_lazy('dimension', "width"))
    height = models.PositiveIntegerField(default=0, verbose_name=pgettext_lazy('dimension', "height"))

    # Meta
    class Meta:
        abstract = True


class DimensionFloatBase(DimensionBase):
    """
    Base class for models with a representation of rectangle dimensions

    The model allows for representation of floating point dimensions and
    contains two ``FloatField`` named ``width`` and ``height``.
    """

    # Fields
    width = models.FloatField(default=0.0, verbose_name=pgettext_lazy('dimension', "width"))
    height = models.FloatField(default=0.0, verbose_name=pgettext_lazy('dimension', "height"))

    # Meta
    class Meta:
        abstract = True
