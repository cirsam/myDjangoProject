activate_this = 'C:/Users/cirsa/Envs/my_application/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Users/cirsa/Envs/my_application/Lib/site-packages/')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/cirsa/myDjangoProject')
sys.path.append('C:/Users/cirsa/myDjangoProject/myDjangoProject')

os.environ['DJANGO_SETTINGS_MODULE'] = 'myDjangoProject.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myDjangoProject.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()