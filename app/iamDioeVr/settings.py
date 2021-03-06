"""
Django settings for iamDioeVr project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import random, string

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#####################################################################################################################
# Umgebungsvariablen:																								#
#####################################################################################################################
# IAMDIOEVR_DEBUG = "False"										(Default: "True")									#
# IAMDIOEVR_SECRET_KEY = Benutze: https://www.miniwebtool.com/django-secret-key-generator/							#
# IAMDIOEVR_STATIC_ROOT = "/var/www/example.com/static/"		(Default: None)										#
# IAMDIOEVR_STATIC_URL = "/static/"								(Default: "/static/")								#
# IAMDIOEVR_MEDIA_URL = "https://iamdioevr.dioe.at/media/"		(Default: "https://iamdioevr.dioe.at/media/")		#
# Datenbank:																										#
# IAMDIOEVR_DB="django.db.backends.postgresql"					(Default: "django.db.backends.sqlite3")				#
# IAMDIOEVR_DB_NAME="PersonenDB"								(Default: os.path.join(BASE_DIR, 'db.sqlite3'))		#
# IAMDIOEVR_DB_USER="user"										(Default: None)										#
# IAMDIOEVR_DB_PASSWORD="passwort"								(Default: None)										#
# IAMDIOEVR_DB_HOST="postgresql://localhost"					(Default: None)										#
# IAMDIOEVR_DB_PORT="5433"										(Default: None)										#
#####################################################################################################################

LOGIN_URL = 'iamdioevr_login'
LOGOUT_URL = 'iamdioevr_logout'
LOGIN_REDIRECT_URL = 'evaluation:start'
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yueqlcc54o8+eskilg2=n=#n^i)8o@z_fi7j@$le61xi%2u75z'

# SECURITY WARNING: don't run with debug turned on in production!
if 'IAMDIOEVR_DEBUG' in os.environ and (os.environ['IAMDIOEVR_DEBUG'] == 'False' or os.environ['IAMDIOEVR_DEBUG'] is False):
	DEBUG = False
else:
	DEBUG = True

ALLOWED_HOSTS = []

ALLOWED_SETTINGS_IN_TEMPLATES = ("CACH_RANDOM")

CACH_RANDOM = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for i in range(8))

# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'webpack_loader',
	'crispy_forms',
	'vr',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'iamDioeVr.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'iamDioeVr', 'templates'), os.path.join(BASE_DIR, 'vr', 'templates'), os.path.join(BASE_DIR, 'evaluation', 'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'iamDioeVr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Umgebungsvariablen:
if 'IAMDIOEVR_SECRET_KEY' in os.environ:
	SECRET_KEY = os.environ['IAMDIOEVR_SECRET_KEY']

if 'IAMDIOEVR_DB' in os.environ and os.environ['IAMDIOEVR_DB']:
	DATABASES['default']['ENGINE'] = os.environ['IAMDIOEVR_DB']
	if 'IAMDIOEVR_DB_NAME' in os.environ:
		DATABASES['default']['DBNAME'] = os.environ['IAMDIOEVR_DB_NAME']
		DATABASES['default']['NAME'] = os.environ['IAMDIOEVR_DB_NAME']
	if 'IAMDIOEVR_DB_USER' in os.environ:
		DATABASES['default']['USER'] = os.environ['IAMDIOEVR_DB_USER']
	if 'IAMDIOEVR_DB_PASSWORD' in os.environ:
		DATABASES['default']['PASSWORD'] = os.environ['IAMDIOEVR_DB_PASSWORD']
	if 'IAMDIOEVR_DB_HOST' in os.environ:
		DATABASES['default']['HOST'] = os.environ['IAMDIOEVR_DB_HOST']
	if 'IAMDIOEVR_DB_PORT' in os.environ:
		DATABASES['default']['PORT'] = os.environ['IAMDIOEVR_DB_PORT']

# print(DATABASES)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'de-DE'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False
USE_THOUSAND_SEPARATOR = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Umgebungsvariablen:
if 'IAMDIOEVR_STATIC_ROOT' in os.environ and os.environ['IAMDIOEVR_STATIC_ROOT']:
	STATIC_ROOT = os.environ['IAMDIOEVR_STATIC_ROOT']
if 'IAMDIOEVR_STATIC_URL' in os.environ and os.environ['IAMDIOEVR_STATIC_URL']:
	STATIC_URL = os.environ['IAMDIOEVR_STATIC_URL']

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'iamDioeVr', 'static'),
	os.path.join(BASE_DIR, 'vr', 'static'),
	os.path.join(BASE_DIR, 'evaluation', 'static'),
	os.path.abspath(os.path.join(BASE_DIR, os.pardir, 'webpack_src', 'vr', 'dist')),
)

WEBPACK_LOADER = {
	'VR': {
		'STATS_FILE': os.path.abspath(os.path.join(BASE_DIR, os.pardir, 'webpack_src', 'vr', 'webpack-stats.json')),
	}
}

MEDIA_URL = "https://iamdioevr.dioe.at/media/"
MEDIA_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir, os.pardir, 'persistent', 'media'))

if 'IAMDIOEVR_MEDIA_URL' in os.environ and os.environ['IAMDIOEVR_MEDIA_URL']:
	MEDIA_URL = os.environ['IAMDIOEVR_MEDIA_URL']
