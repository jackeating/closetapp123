import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '=_pt)m#meaufd$*$ty@o!v7$fz$$(5m4(e^t!+@(l-zs!^fmd-'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
