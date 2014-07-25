# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import (
    GridFoundation,
    GRID_CONFIG,
    ALDRYN_GRID_FOUNDATION_CHOICES,
    GridColumnFoundation
)


NUM_COLUMNS = [
    (i, '%s' % i) for i in range(0, GRID_CONFIG['COLUMNS'])
]


class GridPluginForm(forms.ModelForm):
    create = forms.ChoiceField(
        choices=NUM_COLUMNS,
        label=_('Create Columns'),
        help_text=_('Create this number of columns inside')
    )
    create_size_small = forms.ChoiceField(
        choices=ALDRYN_GRID_FOUNDATION_CHOICES,
        label=_('Column size (mobile)'),
        help_text=('Width of created columns. You can still change the width of the column afterwards.'),
        required=False
    )
    create_size_medium = forms.ChoiceField(
        choices=ALDRYN_GRID_FOUNDATION_CHOICES,
        label=_('Column size (tablet)'),
        help_text=('Width of created columns. You can still change the width of the column afterwards.'),
        required=False
    )
    create_size_large = forms.ChoiceField(
        choices=ALDRYN_GRID_FOUNDATION_CHOICES,
        label=_('Column size'),
        help_text=('Width of created columns. You can still change the width of the column afterwards.'),
        required=False
    )

    class Meta:
        model = GridFoundation
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


class GridColumnPluginForm(forms.ModelForm):

    class Meta:
        model = GridColumnFoundation

    def clean(self):
        data = super(GridColumnPluginForm, self).clean()
        sizes = [
            data['size_small'],
            data['size_medium'],
            data['size_large'],
        ]
        if not any(sizes):
            raise ValidationError(_("Please provide either a size for mobile, tablet or desktop, or all."))
        return data
