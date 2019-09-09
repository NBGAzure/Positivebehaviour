Pip Freezer
===========

Author:Tim Santor tsantor@xstudios.agency

Overview
========

For the organized developer. Puts packages in their proper place
(base.txt, local.txt, production.txt, test.txt). **Plays nice with
`Django
Cookiecutter <https://github.com/pydanny/cookiecutter-django>`__.**

Installation
============

To install Pip Freezer, simply use pip:

.. code:: bash

    pip install pipfreezer

Usage
-----

Freeze requirements
^^^^^^^^^^^^^^^^^^^

In the root of your project, run:

.. code:: bash

    pipfreezer

..

    **NOTE:** On first run, ``pipfreezer`` will create a config file at
    ``^/.pipfreezer/pipfreezer.cfg``. This contains the rules for where
    pipfreezer will place known requirements. Feel free to edit this to
    your liking.

Install requirements
^^^^^^^^^^^^^^^^^^^^

When installing requirements simply use:

.. code:: bash

    pip install -r requirements/local.txt

..

    **NOTE:** Replace ``local`` with the environment you desire:
    ``local``, ``production`` or ``test``

Documentation
=============

Documentation is available at TODO

Version History
===============

-  **0.1.0** - Initial release

Issues
======

If you experience any issues, please create an
`issue <https://bitbucket.org/tsantor/pip-freezer/issues>`__ on
Bitbucket.


History
=======

All notable changes to this project will be documented in this file.
This project adheres to `Semantic Versioning <http://semver.org/>`__.

0.1.0 (2017-12-04)
------------------

-  First release on PyPI.


