import os, logging

DEBUG            = True
BASE_DIR         = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY       = 'bodx2e0t&nhpb-*_39(iyymj1gphsel#k1k#-%+bxj9u6dridv'
APPEND_SLASH     = False

ALLOWED_HOSTS    = ['*']

ROOT_URLCONF     = 'related_ids_test.urls'
WSGI_APPLICATION = 'related_ids_test.wsgi.application'

STATIC_URL       = '/static/'
STATIC_ROOT      = os.path.join(BASE_DIR, 'static')

USE_TZ           = True
USE_I18N         = True
USE_L10N         = True
TIME_ZONE        = 'UTC'
LANGUAGE_CODE    = 'en-us'

INSTALLED_APPS = [
  'related_ids_test',

  'dynamic_rest',
  'rest_framework',

  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
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

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

REST_FRAMEWORK = {
  'DEFAULT_PARSER_CLASSES': (
    'rest_framework.parsers.JSONParser',),
  'DEFAULT_RENDERER_CLASSES': (
    'rest_framework.renderers.JSONRenderer',),
}

DYNAMIC_REST = {
  'ENABLE_BROWSABLE_API': False,
  'ENABLE_LINKS':         False,
  'DEFER_MANY_RELATIONS': True
}
