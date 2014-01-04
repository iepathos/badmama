"""
Settings for Badmama's Badass Django Project Template.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_NAME = os.path.basename(BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-8!u=6bvs-9nhtih-c8wq*pkafjcqbf+podiqve)fm(=7(+(33'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    'sekizai.context_processors.sekizai',
    str(PROJECT_NAME) + ".context_processors.default",
]

### Applications
BASE_APPS = (
	'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Third Party Apps
	'south',
    'sekizai',
    'bootstrap3',
    'rest_framework',
    'registration',
)

PROJECT_APPS = (
	# Enter new project apps here
)

INSTALLED_APPS = BASE_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = str(PROJECT_NAME) + '.urls'

WSGI_APPLICATION = str(PROJECT_NAME) + '.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# MySQL database is served by Vagrant and setup with Berkshelf
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'badmama',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '33.33.33.10',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

APPEND_SLASH = True

### Cookies
SESSION_COOKIE_AGE = 60*60
SESSION_SAVE_EVERY_REQUEST = True

### Registration
# users get automatically logged in after activating their accounts
REGISTRATION_AUTO_LOGIN = True

LOGIN_URL = "/accounts/login"

# where to redirect users to after logging in
LOGIN_REDIRECT_URL = '/'

# where to redirect users to upon logging out
LOGOUT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)



if DEBUG:
    ########## TOOLBAR CONFIGURATION
    # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
    INSTALLED_APPS += (
        'debug_toolbar',
    )

    # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
    INTERNAL_IPS = ('127.0.0.1',)

    # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    ########## END TOOLBAR CONFIGURATION