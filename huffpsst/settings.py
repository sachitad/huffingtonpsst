# -*- coding: utf-8 -*-
import os
import dj_database_url
from django.utils.http import http_date
import time
import sys

boolean = lambda value: bool(value)
local_path = lambda path: os.path.join(os.path.dirname(__file__), path)
project_path = lambda path: os.path.join(os.path.dirname(__file__), '..', path)

ENVIRONMENT = os.environ.get("ENVIRONMENT","DEV")

def ensure_dir(path):
    if not os.path.exists(path): os.makedirs(path)



DEBUG = boolean(os.environ.get('DJ_DEBUG', True))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Asim Hussain', 'jawache@gmail.com'),
)

ALLOWED_HOSTS = ["*"]

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(default='postgres://huffpsst:huffpsst@localhost/huffpsst')
}

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_HOST_USER = os.environ.get('MANDRILL_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('MANDRILL_APIKEY')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
MANDRILL_API_KEY = os.environ.get('MANDRILL_APIKEY')
TEMPLATED_EMAIL_TEMPLATE_DIR = ''
TEMPLATED_EMAIL_FILE_EXTENSION = 'email'

if ENVIRONMENT == "DEV":
    DEFAULT_FROM_EMAIL = 'HuffPsst - DEV <hello-dev@huffpsst.com>'
    STUDYHALL_SUPPORT_MAIL = 'HuffPsst Support - DEV <support-dev@huffpsst.com>'
    SERVER_EMAIL = "hello-dev@huffpsst.com"
elif ENVIRONMENT == "QA":
    DEFAULT_FROM_EMAIL = 'HuffPsst QA <hello-qa@huffpsst.com>'
    STUDYHALL_SUPPORT_MAIL = 'HuffPsst Support - QA <support-qa@huffpsst.com>'
    SERVER_EMAIL = "hello-qa@huffpsst.com"
elif ENVIRONMENT == "PROD":
    DEFAULT_FROM_EMAIL = 'HuffPsst <hello@huffpsst.com>'
    SERVER_EMAIL = "hello@huffpsst.com"
    STUDYHALL_SUPPORT_MAIL = 'HuffPsst Support <support@huffpsst.com>'


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', project_path('media/'))
ensure_dir(MEDIA_ROOT)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.environ.get('STATIC_ROOT', project_path('static/'))
ensure_dir(STATIC_ROOT)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
# Additional locations of static files
STATICFILES_DIRS = [
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l^=ixa%9fjzx*byb--nuzj0x7vkw(m6_*70*4hpnz4wfty4w68'

# List of callables that know how to import templates from various sources.
if not DEBUG:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
else:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

MIDDLEWARE_CLASSES = (
    # 'huffpsst.middleware.BasicAuthMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    # Wagtail middlewares
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

BASICAUTH_USERNAME = 'huffpsst'
BASICAUTH_PASSWORD = 'awesome'


ROOT_URLCONF = 'huffpsst.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'huffpsst.wsgi.application'

TEMPLATE_DIRS = (
    project_path('templates/')
)



from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages",
    "huffpsst.context_processor.template_settings",
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'sorl.thumbnail',
    'django_markdown',
    'django_gravatar',
    'annoying',
    'django_extensions',
    'raven.contrib.django.raven_compat',
    'crispy_forms',
    'storages',
    'bootstrap_pagination',
    'south',
    'compressor',
    'taggit',
    'modelcluster',
    'django.contrib.admin',

    'gunicorn',
    'huffpsst',

    #Wagtail
    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',

    #Local Apps
    'category',
    'author',
    'article',
    'comment',
    'advert',
    'video',
    'homepage',

]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Auth settings
LOGIN_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

# This is set by cloudflare and heroku so we know the original reqeust was a secure one
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
if DEBUG:
    SSL_URLS = ()
else:
    SSL_URLS = (
        r".*",
    )

REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
if DEBUG:
    handlers = ['console']
else:
    handlers = ['heroku']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(module)s :: %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'heroku': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'huffpsst': {
            'handlers': handlers,
            'level': 'DEBUG',
            'propagate': True,
        },
        'root': {
            'handlers': handlers,
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}



#
# AWS
#
AWS_STORAGE_BUCKET_NAME = "huffpsst-media"
AWS_URL = "http://s3.amazonaws.com/"
AWS_IS_GZIPPED = True
AWS_S3_FILE_OVERWRITE = True
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Expires': http_date(time.time() + 31536000),  # Cache for 1 year
    'Cache-Control': ':public, max-age=31536000',  # Cache for 1 year
}
AWS_S3_SECURE_URLS = True


if not DEBUG:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

if ENVIRONMENT == "QA":
    AWS_STORAGE_BUCKET_NAME = "huffpsst-media-qa"
    MEDIA_URL = "http://huffpsst-media-qa.s3.amazonaws.com/"
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
elif ENVIRONMENT == "PROD":
    AWS_STORAGE_BUCKET_NAME = "huffpsst-prod"
    DEFAULT_FILE_STORAGE = "herokuify.storage.S3MediaStorage"
    MEDIA_URL = "https://{0}.s3.amazonaws.com/media/".format(AWS_STORAGE_BUCKET_NAME)

    STATICFILES_STORAGE = "herokuify.storage.CachedS3StaticStorage"
    STATIC_URL = "https://{0}.s3.amazonaws.com/static/".format(AWS_STORAGE_BUCKET_NAME)

    COMPRESS_STORAGE = "herokuify.storage.CachedS3StaticStorage"
    COMPRESS_OFFLINE = True
    COMPRESS_ENABLED = True

COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter"
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# AUTH_PROFILE_MODULE = 'huffpsst.UserProfile'
# AUTH_USER_MODEL = 'huffpsst.CustomUser'



AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)


def get_cache():
    import os

    try:
        os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHEDCLOUD_SERVERS'].replace(',', ';')
        os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHEDCLOUD_USERNAME']
        os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHEDCLOUD_PASSWORD']
        return {
            'default': {
                'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
                'TIMEOUT': 1000,
            }
        }
    except:
        return {
            'default': {
                'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            }
        }


CACHES = get_cache()

# Wagtail configuration
WAGTAIL_SITE_NAME = 'Huffpsst'

LAMPOON = 'http://harvardlampoon.com/'