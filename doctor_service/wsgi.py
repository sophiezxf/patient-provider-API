"""
WSGI config

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see:
http://flask.pocoo.org/docs/deploying/mod_wsgi/
http://bucksnort.pennington.net/blog/post/deploy-flask-mod_wsgi_virtenv/
"""

activate_this = 'doctor_service/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import os

app_dir = os.path.relpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, app_dir)

from doctor_service import app, settings

env = os.environ.get('APP_ENVIRONMENT', 'development')
if env.lower() == 'production':
    config = settings.Production()
else:
    config = settings.Development()

application = app.create_app(config=config)
