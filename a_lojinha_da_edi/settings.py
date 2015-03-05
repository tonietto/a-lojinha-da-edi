"""
Django settings for a_lojinha_da_edi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nz06q+k(&jxd8s@i@*0-0vp_t$lo57dh4lu639m5tz2_&2ymca'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

if DEBUG:
    ALLOWED_HOSTS = ['localhost']

else:
    ALLOWED_HOSTS = ['localhost', '.alojinhadaedi.com.br']


# Application definition

INSTALLED_APPS = (
    'grappelli_menu',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'blog',
    'catalogo',
    'cliente',
    'financeiro',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'a_lojinha_da_edi.urls'

WSGI_APPLICATION = 'a_lojinha_da_edi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'mysql.connector.django',
            'NAME': 'edi_database',
            'USER': 'edi_admin',
            'PASSWORD': 'K.P;AnnVzRpK4Y:Zz&X7HkF\Q@D/A[dNAX@2eAJSaKt6335PBacon',
            'HOST': '192.185.216.81',
            'PORT': '3306',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'Brazil/East'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

PROJECT_DIR = os.path.dirname(__file__)

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = (STATIC_URL,)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",  # Grappelli
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",  # Grappelli
)

# Grappelli Settings
GRAPPELLI_ADMIN_TITLE = 'Admin'
GRAPPELLI_INDEX_DASHBOARD = 'a_lojinha_da_edi.dashboard.CustomIndexDashboard'

# Heroku
if DEBUG is False:
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']

    # Static asset configuration
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
