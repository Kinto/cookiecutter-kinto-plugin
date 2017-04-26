{{ cookiecutter.project_name }}
===============================

|travis| |master-coverage|

.. |travis| image:: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.svg?branch=master
    :target: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}

.. |master-coverage| image::
    https://coveralls.io/repos/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/badge.png?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}

{{ cookiecutter.project_short_description }}

* `Kinto documentation <http://kinto.readthedocs.io/en/latest/>`_
* `Issue tracker <https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/issues>`_


Installation
------------

Install the Python package:

::

    pip install {{cookiecutter.project_name}}


Include the package in the project configuration:

::

    kinto.includes = {{cookiecutter.project_slug}}



Configuration
-------------

Fill those settings with the values obtained during the application registration:

::

    # {{cookiecutter.project_slug.replace('_', '.')}}.whatever = foobar
