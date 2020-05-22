import os


#class Baseconfig:
#    """Base Configuration"""
#    TESTING = False
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
#    SECRET_KEY = 'not_precious'


class DevelopmentConfig:
    """Development Configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'not_precious'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig:
    """Test Config"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig:
    """Deployment Config"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
