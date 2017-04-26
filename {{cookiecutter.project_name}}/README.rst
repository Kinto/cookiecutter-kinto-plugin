{{ cookiecutter.project_name }}
===============================

|travis| |master-coverage|

.. |travis| image:: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=master
    :target: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}

.. |master-coverage| image::
    https://coveralls.io/repos/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/badge.png?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}


* `Kinto documentation <http://kinto.readthedocs.io/en/latest/>`_
* `Issue tracker <https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/issues>`_


Installation
------------

Install the Python package:

::

    pip install {{cookiecutter.project_slug}}


Include the package in the project configuration:

::

    kinto.includes = {{cookiecutter.project_slug}}



Configuration
-------------

Fill those settings with the values obtained during the application registration:

::

    # {{cookiecutter.project_slug.replace('_', '.')}}.whatever = foobar
