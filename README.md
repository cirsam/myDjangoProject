# myDjangoProject

Exams application with Django
=======
Exams App with Django


##Update your wsgi.py file with the content below

	activate_this = 'C:/path/to/your/environment/Scripts/activate_this.py'
	# execfile(activate_this, dict(__file__=activate_this))
	exec(open(activate_this).read(),dict(__file__=activate_this))

	import os
	import sys
	import site

	# Add the site-packages of the chosen virtualenv to work with
	site.addsitedir('C:/path/to/your/environment/Lib/site-packages/')




	# Add the app's directory to the PYTHONPATH
	sys.path.append('C:/path/to/your/myDjangoProject')
	sys.path.append('C:/path/to/your/myDjangoProject/myDjangoProject')

	os.environ['DJANGO_SETTINGS_MODULE'] = 'myDjangoProject.settings'
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myDjangoProject.settings")

	from django.core.wsgi import get_wsgi_application
	application = get_wsgi_application()







## Update your http-vhosts.conf with the content below
	# Virtual Hosts
	#
	# Required modules: mod_log_config

	# If you want to maintain multiple domains/hostnames on your
	# machine you can setup VirtualHost containers for them. Most configurations
	# use only name-based virtual hosts so the server doesn't need to worry about
	# IP addresses. This is indicated by the asterisks in the directives below.
	#
	# Please see the documentation at 
	# <URL:http://httpd.apache.org/docs/2.4/vhosts/>
	# for further details before you try to setup virtual hosts.
	#
	# You may use the command line option '-S' to verify your virtual host
	# configuration.

	#
	# VirtualHost example:
	# Almost any Apache directive may go into a VirtualHost container.
	# The first VirtualHost section is used for all requests that do not
	# match a ServerName or ServerAlias in any <VirtualHost> block.
	#



	# virtual SupervisionTool
	<VirtualHost *:80>
		ServerName localhost 
		WSGIPassAuthorization On
		ErrorLog "logs/my_application.error.log"
		CustomLog "logs/my_application.access.log" combined
		
		#To force preloading, you can use on Linux:
		#WSGIScriptAlias / /some/path/wsgi.py process-group=xxx application-group=%{GLOBAL}
		#and on Windows:
		#WSGIScriptAlias / /some/path/wsgi.py application-group=%{GLOBAL}
		
		
		WSGIScriptAlias /  "C:\path\to\your\myDjangoProject\myDjangoProject\wsgi_windows.py" application-group=%{GLOBAL}
		<Directory "C:\path\to\your\myDjangoProject\myDjangoProject">
			<Files wsgi_windows.py>
				Require all granted
			</Files>
		</Directory>

		Alias /static "C:/path/to/your/myDjangoProject/static"
		<Directory "C:/path/to/your/myDjangoProject/static">
			Require all granted
		</Directory>  
	</VirtualHost>
	# end virtual SupervisionTool



