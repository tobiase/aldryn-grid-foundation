# -*- coding: utf-8 -*-
from django import forms
from aldryn_grid_foundation.models import GridFoundation, GRID_CONFIG, ALDRYN_GRID_FOUNDATION_CHOICES
from django.utils.translation import ugettext_lazy as _

NUM_COLUMNS = [
    (i, '%s' % i) for i in range(0, GRID_CONFIG['COLUMNS'])
]


class GridPluginForm(forms.ModelForm):
    create = forms.ChoiceField(choices=NUM_COLUMNS, label=_('Create Columns'), help_text=_('Create this number of columns inside'))
    create_size_small = forms.ChoiceField(choices=ALDRYN_GRID_FOUNDATION_CHOICES, label=_('Column size (mobile)'), help_text=('Width of created columns. You can still change the width of the column afterwards.'), required=True)
    create_size_large = forms.ChoiceField(choices=ALDRYN_GRID_FOUNDATION_CHOICES, label=_('Column size'), help_text=('Width of created columns. You can still change the width of the column afterwards.'), required=False)

    class Meta:
        model = GridFoundation
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
