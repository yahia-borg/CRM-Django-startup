from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your-production-domain.com']

# Security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

DATABASES['default'].update({
    'HOST': 'your-production-db-host',
    'USER': 'your-production-db-user',
    'PASSWORD': 'your-production-db-password',
})