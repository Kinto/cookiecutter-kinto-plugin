import unittest
import webtest

import kinto.core
from pyramid.config import Configurator

from {{ cookiecutter.project_slug }} import __version__ as plugin_version


def get_request_class(prefix):

    class PrefixedRequestClass(webtest.app.TestRequest):

        @classmethod
        def blank(cls, path, *args, **kwargs):
            path = '/%s%s' % (prefix, path)
            return webtest.app.TestRequest.blank(path, *args, **kwargs)

    return PrefixedRequestClass


class BaseWebTest(object):
    """Base Web Test to test your cornice service.

    It setups the database before each test and delete it after.
    """

    api_prefix = "v0"

    def __init__(self, *args, **kwargs):
        super(BaseWebTest, self).__init__(*args, **kwargs)
        self.app = self._get_test_app()
        self.headers = {
            'Content-Type': 'application/json',
        }

    def _get_test_app(self, settings=None):
        config = self._get_app_config(settings)
        wsgi_app = config.make_wsgi_app()
        app = webtest.TestApp(wsgi_app)
        app.RequestClass = get_request_class(self.api_prefix)
        return app

    def _get_app_config(self, settings=None):
        config = Configurator(settings=self.get_app_settings(settings))
        kinto.core.initialize(config, version='0.0.1')
        return config


class CapabilityTestView(BaseWebTest, unittest.TestCase):

    def test_portier_capability(self, additional_settings=None):
        resp = self.app.get('/')
        capabilities = resp.json['capabilities']
        self.assertIn('{{ cookiecutter.project_slug.replace('kinto_', '') }}', capabilities)
        expected = {
            "version": plugin_version,
            "url": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}",
            "description": "{{ cookiecutter.project_short_description }}"
        }
        self.assertEqual(expected, capabilities['{{ cookiecutter.project_slug.replace('kinto_', '') }}'])
