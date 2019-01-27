import os
import sys	
sys.path.append('/home/web/www/django/pcl/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
