import pkg_resources


#: Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__).version


DEFAULT_SETTINGS = {}


def includeme(config):
    settings = config.get_settings()

    defaults = {k: v for k, v in DEFAULT_SETTINGS.items() if k not in settings}
    config.add_settings(defaults)

    config.add_api_capability(
        "{{ cookiecutter.project_slug.replace('kinto_', '') }}",
        version=__version__,
        description="{{ cookiecutter.project_short_description }}",
        url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}")

    # config.scan('{{cookiecutter.project_slug}}.views')
