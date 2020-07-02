"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import os 
import sys 
sys.path.append(os.path.dirname(__file__) + '/..') 

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings' 

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# #################################################
 
sys.path.append('C:/Apache24/htdocs/<PROJECT-ROOT-DIRECTORY>')