# ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#  Copyright (c) 2018, S.J.M. Steffann. This software is licensed under the BSD
#  3-Clause License. Please see the LICENSE file in the project root directory.
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class Region(models.Model):
    code = models.PositiveIntegerField(_('code'), primary_key=True)
    parent = models.ForeignKey('self', verbose_name=_('parent'), on_delete=models.CASCADE, blank=True, null=True)
    level = models.PositiveSmallIntegerField(_('level'))
    name = models.CharField(_('name'), max_length=100)
    countries = CountryField(_('countries'), multiple=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('region')
        verbose_name_plural = _('regions')
        ordering = ('name',)
