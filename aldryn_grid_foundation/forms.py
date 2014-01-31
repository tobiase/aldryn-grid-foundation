# -*- coding: utf-8 -*-
from django import forms
from aldryn_grid_foundation.models import GridFoundation, GRID_CONFIG, ALDRYN_GRID_FOUNDATION_CHOICES, \
    GridColumnFoundation
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

NUM_COLUMNS = [
    (i, '%s' % i) for i in range(0, GRID_CONFIG['COLUMNS'])
]


class GridPluginForm(forms.ModelForm):
    create = forms.ChoiceField(choices=NUM_COLUMNS, label=_('Create Columns'), help_text=_('Create this number of columns inside'))
    create_size_small = forms.ChoiceField(choices=ALDRYN_GRID_FOUNDATION_CHOICES, label=_('Column size (mobile)'), help_text=('Width of created columns. You can still change the width of the column afterwards.'), required=False)
    create_size_large = forms.ChoiceField(choices=ALDRYN_GRID_FOUNDATION_CHOICES, label=_('Column size'), help_text=('Width of created columns. You can still change the width of the column afterwards.'), required=False)

    class Meta:
        model = GridFoundation
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


class GridColumnPluginForm(forms.ModelForm):
    class Meta:
        model = GridColumnFoundation

    def clean(self):
        cleaned_data = super(GridColumnPluginForm, self).clean()
        if not cleaned_data['size_small'] and not cleaned_data['size_large']:
            raise ValidationError(_("Please provide either a size for mobile and desktop, or both."))
        return cleaned_data
