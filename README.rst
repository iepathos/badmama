Badmama's Badass Django Project Template
========================================

Development Setup
=================

- ``mkproject badmama``
- ``pip install django``
- ``django-admin.py startproject --template=https://github.com/iepathos/badmama/archive/master.zip --extension=py,rst,html new_project``
- ``cd new_project``
- ``pip install -r requirements.txt``

- ``berks install``
- ``vagrant plugin install vagrant-berkshelf``
- ``vagrant up``

- ``./manage.py syncdb``
- ``./manage.py runserver``


Vagrantfile is not being ran through the templating, so {{ project_name }} isn't working.  The default MySQL database is named badmama and the host will be to badmama.


Technology Behind Badmama
=========================

- Python
- Django 1.6.1
- Django REST Framework
- South
- Django-Sekizai
- Django-Registration

- MySQL

- Berkshelf
- Chef
- Vagrant

- Javascript
- JQuery
- Underscore
- Backbone
- ICanHaz (Moustache)
- Bootstrap 3
