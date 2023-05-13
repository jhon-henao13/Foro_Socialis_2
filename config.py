class Config:
    DEBUG = True
    TESTING = True

    # Configuracion de base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:estiwar2020@127.0.0.1:3306/foro"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = "dev"
    DEBUG = True
    TESTING = True