Setup
-----

```
virtualenv new_virtual_env_name
source new_virtual_env_name/bin/activate
pip install -r requirements.txt
```

Testing
-------

```
export TEAMTEMP_SECRET_KEY=`python -c 'import uuid; print uuid.uuid4()'`
export DJANGO_SETTINGS_MODULE=teamtemp.settings
export DATABASE_URL=sqlite:///`pwd`/teamtemp.sqlite
python manage.py test
```

Coverage
-------

```
coverage run manage.py test
coverage report -m
```

Build Health
-----------
[![Build Status](https://travis-ci.org/travisjwarren/teamtemp.svg)](https://travis-ci.org/travisjwarren/teamtemp)
[![Coverage Status](https://coveralls.io/repos/travisjwarren/teamtemp/badge.png)](https://coveralls.io/r/travisjwarren/teamtemp)
