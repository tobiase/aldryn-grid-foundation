# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from aldryn_grid_foundation.forms import GridPluginForm
from aldryn_grid_foundation.models import GridFoundation, GridColumnFoundation, GRID_CONFIG


class GridFoundationPlugin(CMSPluginBase):
    model = GridFoundation
    name = _('Multi Columns (grid)')
    module = _('Multi Columns')
    render_template = 'aldryn_grid_foundation/grid.html'
    allow_children = True
    child_classes = ['GridColumnFoundationPlugin']
    form = GridPluginForm

    def render(self, context, instance, placeholder):
        context.update({
            'grid': instance,
            'placeholder': placeholder,
            'GRID_SIZE': GRID_CONFIG['COLUMNS'],
        })
        return context

    def save_model(self, request, obj, form, change):
        response = super(GridFoundationPlugin, self).save_model(request, obj, form, change)
        if not change:
            for x in xrange(int(form.cleaned_data['create'])):
                col = GridColumnFoundation(
                    parent=obj,
                    placeholder=obj.placeholder,
                    language=obj.language,
                    size_large=form.cleaned_data['create_size_large'],
                    size_small=form.cleaned_data.get('create_size_small', None),
                    position=CMSPlugin.objects.filter(parent=obj).count(),
                    plugin_type=GridColumnFoundationPlugin.__name__,
                )
                col.save()
        return response


class GridColumnFoundationPlugin(CMSPluginBase):
    model = GridColumnFoundation
    name = _('Grid Column')
    module = _('Multi Columns')
    render_template = 'aldryn_grid_foundation/column.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'column': instance,
            'placeholder': placeholder,
        })
        if 'width' in context:
            context['width'] = context['width'] / GRID_CONFIG['COLUMNS'] * int(instance.size_large) - GRID_CONFIG['GUTTER'] / 2
        return context

plugin_pool.register_plugin(GridFoundationPlugin)
plugin_pool.register_plugin(GridColumnFoundationPlugin)
