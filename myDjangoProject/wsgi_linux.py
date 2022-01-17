# =====================
# wsgi.py file begin 

import os, sys
# add the my_application project path into the sys.path
sys.path.append('/var/www/my_application/my_application')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/tigersvault/env/lib/python3.8/site-packages/')

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_application.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# wsgi.py file end
# ===================