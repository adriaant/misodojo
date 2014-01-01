# misodojo

## Intro

This is a Django project that I use for my own personal site. It's really more like a
playground. It has a simple Blog model that uses the 3rd party Taggit package. It also
uses the flatpages contrib module for personal pages. 

For deployment, I use gunicorn with nginx. 


## Quickstart

To bootstrap the project:

1. define the `DJANGO_PROJECT_ENV` environment variable (values: local, dev, uat, prod)
2. create the virtual environment and activate it
3. install third-party packages and this project package
4. create the `secrets.py` file
5. create the database and the tables for all `INSTALLED_APPS`, and create a superuser

```
echo -e '\n# Django project environment\nexport DJANGO_PROJECT_ENV="local"' >> ~/.profile
source ~/.profile

cd /path/to/virtualenvs
virtualenv misodojo
source misodojo/bin/activate

cd /path/to/misodojo/repository

pip install -r requirements/${DJANGO_PROJECT_ENV}.txt
pip install -e .

mv misodojo/settings/secrets.py.example misodojo/settings/secrets.py 

manage.py syncdb --migrate
manage.py createsuperuser
```


## Documentation

Developer documentation is available in [Sphinx](http://sphinx-doc.org/) format in the docs directory.

Initial installation instructions (including how to build the documentation as HTML) can be found in docs/install.rst.


## Management commands

### Static files 

```
collectstatic -l
```

### Database

```
syncdb --migrate
dumpdata --indent=2 <app_name> > <fixture_name>.json
loaddata <fixture_name>
```

### South

```
schemamigration <app_name> --initial
schemamigration <app_name> --auto
migrate <app_name>
```

[South command reference](http://south.readthedocs.org/en/latest/commands.html)

### Diagrams

```
graph_models -a > all_models.dot
graph_models -o <app_name>-models.png <app_name>
```

[Django-Extensions command reference](http://pythonhosted.org/django-extensions/graph_models.html)
