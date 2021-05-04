"""
Django settings for _banyanvideos_root project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url
from os.path import join,dirname

from dotenv import load_dotenv
load_dotenv(verbose=True)

SECRET_KEY = os.getenv("SECRET_KEY")

STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY")
STRIPE_PRIVATE_KEY = os.getenv("STRIPE_PRIVATE_KEY")

"""
BANYAN - VIDEOS - CORP.
CUSTOM APPLICATION CONFIGURATION.

MAINTENANCE ; maintenace mode available... staff only
BANYAN_VIDEOS_CORP_EMAIL_BOX ; Email box used by banyan videos
SALES_DEPARTMENT_EMAIL ; Email that gets a copy of sales transaction & contacts
FREE_SHIPPING_THRESHOLD ; free shipping activated at this value
"""
PRODUCTION = os.getenv("PRODUCTION")


#Set CMS link for local deployment
MAINTENANCE='http://localhost:8000/admin'

#Set CMS for heroku install
if PRODUCTION =='True':
    MAINTENANCE = os.getenv("MAINTENANCE")




BANYAN_VIDEOS_CORP_EMAIL_BOX=os.getenv("BVC_EMAIL_BOX")
SALES_DEPARTMENT_EMAIL=os.getenv("SALES_DEPT")
FREE_SHIPPING_THRESHOLD=os.getenv("FREE_SHIPPING_THRESHOLD")




DISABLE_COLLECTSTATIC=0

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!@+@
DEBUG = True


ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  
      # Apps for banyan-videos-corp
    'home',
    'search_results',
    'about',
    'logout',
    'members',
    'shopping_cart',
    'login_register',
    'contact',
    'my_account',
    'delete_from_shopping_cart',
  
    # The following apps are required for allauth:
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
  
    'checkout',
    'login_success',
    'charge',
    'contact_sent',
    'error_page',

]

MIDDLEWARE = [
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = '_banyanvideos_root.urls'

AUTHENTICATION_BACKENDS = [
   
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        
        'DIRS': [str(os.path.join(BASE_DIR, 'templates'))],
        
        'APP_DIRS': True,
        
        'OPTIONS': {
            'context_processors': [
                
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_app.wsgi.application'

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD='username_email'

ACCOUNT_EMAIL_REQUIRED=True

ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True

ACCOUNT_USERNAME_MIN_LENGTH = 4

LOGIN_URL = '/account/login/'

LOGIN_REDIRECT_URL ='login_success'

WSGI_APPLICATION = '_banyanvideos_root.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CHECK If IN PRODUCTION & SWITCH DATABASE TO (POSTGRES!!)

if PRODUCTION == True:
     
    DBKEY = os.getenv("DBKEY")

    DATABASES = {
    
        'default':dj_database_url.parse(DBKEY)
        
     
    }
 
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=600)

DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]







BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATIC_URL = '/static/'





# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'),)





# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'




"""
EMAIL SYSTEM CONFIGURATION
"""

# EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST_USER='cofoedu_banyan@hotmail.com'
# EMAIL_HOST = 'smtp.office365.com'
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_PASSWORD='Alexkid1b'

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST = 'in-v3.mailjet.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
 


 










# Static Files
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    
    os.path.join(BASE_DIR,"static"),
   

]

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),) # new


# STATIC_ROOT = (BASE_DIR.join('staticfiles'))

STATIC_ROOT = '_CLIENTS\BANYAN_VIDEOS-CORP-C\_BANYANVIDEOS_ROOT'



''' Engine used during collectstatic. default = django.contrib.staticfiles.storage.StaticFilesStorage.'''
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # however using whitenoise engine because of Heroku


















# Media Files
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CRISPY_TEMPLATE_PACK ='bootstrap4'
