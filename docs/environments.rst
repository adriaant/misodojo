==================
Environments
==================

When deploying to multiple environments (development, staging, production, etc.), you'll likely want to deploy different configurations.
Each environment/configuration should have its own file in ``misodojo/settings`` and inherit from ``misodojo.settings.base``.

``manage.py`` and ``wsgi.py`` use the ``DJANGO_PROJECT_ENV`` environment variable to detect the current environment and define the settings module as ``misodojo.settings.<DJANGO_PROJECT_ENV>``.
If that environment variable is not defined, an exception is raised ("DJANGO_PROJECT_ENV not defined.").

For example, for local development, you can add the following to your ``~/.profile`` file::

    # Django project environment
    export DJANGO_PROJECT_ENV="local"

You may want to have different ``wsgi.py`` and ``urls.py`` files for different environments as well.
If so, simply follow the directory structure laid out by ``misodojo/settings``, for example::

    wsgi/
      __init__.py
      base.py
      dev.py
      ...

The settings files have examples of how to point Django to these specific environments.
