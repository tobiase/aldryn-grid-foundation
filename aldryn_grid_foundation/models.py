# -*- coding: utf-8 -*-
from functools import partial

from django.db import models
from django.utils.translation import ugettext_lazy as _, string_concat
from django.conf import settings

from cms.models import CMSPlugin


GRID_CONFIG = {'COLUMNS': 24, 'TOTAL_WIDTH': 960, 'GUTTER': 20}
GRID_CONFIG.update(getattr(settings, 'ALDRYN_GRID_FOUNDATION_CONFIG', {}))


ALDRYN_GRID_FOUNDATION_CHOICES = [
    (i, string_concat(unicode(i), ' ', _('columns'))) for i in range(1, GRID_CONFIG['COLUMNS']+1)
]

ColumnSizeField = partial(
    models.IntegerField,
    default=0,
    choices=ALDRYN_GRID_FOUNDATION_CHOICES,
    null=True,
    blank=True
)


class GridFoundation(CMSPlugin):
    custom_classes = models.CharField(_('custom classes'), max_length=200, blank=True)

    def __unicode__(self):
        return _(u"%s columns") % self.cmsplugin_set.all().count()


class GridColumnFoundation(CMSPlugin):
    size_small = ColumnSizeField(verbose_name=_('size (mobile)'))
    size_medium = ColumnSizeField(verbose_name=_('size (tablet)'))
    size_large = ColumnSizeField(verbose_name=_('size (desktop)'))
    custom_classes = models.CharField(
        verbose_name=_('custom classes'),
        max_length=200,
        blank=True
    )

    def __unicode__(self):
        result = []
        if self.size_small:
            result.append('small-%d' % self.size_small)
        if self.size_medium:
            result.append('medium-%d' % self.size_medium)
        if self.size_large:
            result.append('large-%d' % self.size_large)
        return u' '.join(result)
