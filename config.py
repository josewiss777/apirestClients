#Register imports
from dotenv import load_dotenv
import os

load_dotenv()

#Assign environment variables
user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
port = os.environ['MYSQL_PORT']
database = os.environ['MYSQL_DATABASE']

#Register classes
class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#Configuration, development and production
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}