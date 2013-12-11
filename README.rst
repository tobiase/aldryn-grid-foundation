Aldryn Grid (Foundation)
====================

A Multi Column Plugin for Aldryn based on the Foundation grid system.


Installation
------------

# TODO

This plugin requires `django CMS` 2.4 or higher to be properly installed.

* In your projects `virtualenv`_, run ``pip install aldryn-grid-foundation``.
* Add ``'aldryn_grid_foundation'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate aldryn_grid_foundation``.


Configure your grid
-------------------

You can configure your grid using three numbers: total width of grid, number of
columns, and width of the gutter in between each column::

    ALDRYN_GRID_FOUNDATION_CONFIG = {
        'COLUMNS': 24,
        'TOTAL_WIDTH': 960,
        'GUTTER': 20,
    }

The above example is the default, which, incidentally, matches the widely used foundation grid.

Usage
-----

.. _virtualenv: http://www.virtualenv.org/en/latest/
