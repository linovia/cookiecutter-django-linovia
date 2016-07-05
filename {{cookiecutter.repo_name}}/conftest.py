import os.path
from copy import copy


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def pytest_configure(config):
    from django.conf import settings
    if not settings.configured:
        from {{cookiecutter.project_name}} import settings as {{cookiecutter.project_name}}_settings
        default = copy({{cookiecutter.project_name}}_settings.__dict__)
        default.update({
            'DATABASE_ENGINE': 'sqlite3',
            'DATABASES': {
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3',
                    'TEST_NAME': ':memory:',
                },
            },
            'DATABASE_NAME': ':memory:',
            'TEST_DATABASE_NAME': ':memory:',
        },)
        settings.configure(**default)
