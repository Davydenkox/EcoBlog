from .base import*
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}

SECRET_KEY = 'django-insecure-n7m_@+f0vj!@o))rfpc#bg#1*p4t1e185ud(6@2ei$_&k-i=in'