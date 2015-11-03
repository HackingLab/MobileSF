"""
Django settings for MobSF project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,platform
import java
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '#r$=rg*lit&!4nukg++@%k+n9#6fhkv_*a6)2t$n1b=*wpvptl'
SECRET_KEY = '#r$=rg*lit&!4nukg++@%k+n9#1fhka_*a6)2t$n1b=*wpvptl'

# SECURITY WARNING: don't run with debug turned on in production!
# ^ This is fine Do not turn it off untill MobSF framework moves from Beta to Stable
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'StaticAnalyzer',
    'DynamicAnalyzer',
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

ROOT_URLCONF = 'MobSF.urls'

WSGI_APPLICATION = 'MobSF.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

MEDIA_URL = '/uploads/'


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates'),
    )

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

#CUSTOM SETTINGS - DO NOT EDIT ANYTHING ABOVE THIS
#=================================================
DECOMPILER = "jd-core" 

#Two Decompilers are available 
#1. jd-core
#2. cfr
 
if platform.system()=="Windows":
    JAVA_PATH=java.FindJava()
    #JAVA_PATH='C:/Program Files/Java/jdk1.7.0_17/bin/'  # Use "/" instead of "\" for the path and the path should end with a "/".
    VBOX='C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' #Path to VBoxManage.exe
elif platform.system()=="Darwin":
    JAVA_PATH=java.FindJava()
    #OSX IS /Applications/VirtualBox.app/Contents/MacOS/VBoxManage
    VBOX='/Applications/VirtualBox.app/Contents/MacOS/VBoxManage'
else:
    #For OSX and Linux
    #JAVA_PATH='/usr/bin/'
    JAVA_PATH=java.FindJava()
    VBOX='/usr/bin/VBoxManage'

#VM SETTINGS
#VBoxManage showhdinfo "MobSF_VM_0.1-disk3.vdi"

#VM UUID
UUID='7098d4eb-bc7a-4913-8469-5e8b90d883ca'
#Snapshot UUID
SUUID='7dd7a070-ce68-4654-b55c-5dacdfbb764c'
#VM/Device IP
VM_IP='192.168.99.100'

#PROXY SETTINGS
PROXY_IP='192.168.99.1' #Host/Server/Proxy IP
PORT='1337' #Proxy Port
