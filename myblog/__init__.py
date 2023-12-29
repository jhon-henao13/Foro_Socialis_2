from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import os

app = Flask(__name__)

#uploads_dir = os.path.abspath(os.path.join(app.root_path, 'Archivos PDF'))

# uploads_dir = os.path.join(app.root_path, 'myblog\Archivos PDF')
#os.makedirs(uploads_dir, exist_ok=True)

#app.config['UPLOAD_FOLDER'] = uploads_dir


# Cargar las configuraciones
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

# Importar vistas
from myblog.views.auth import auth
app.register_blueprint(auth)

from myblog.views.blog import blog
app.register_blueprint(blog)

with app.app_context():
    db.create_all()

#from myblog.views.blog import blog
#app.register_blueprint(blog, url_prefix='/')
#
#with app.app_context():
#    db.create_all()
