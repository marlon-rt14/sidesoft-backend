from dotenv import load_dotenv
from os import environ, path

path_to_dotenv = path.join('\\'.join(path.dirname(__file__).split('\\')[:-1]), '.env')
load_dotenv(dotenv_path=path_to_dotenv)

class Config():
    SECRET_KEY = environ.get("SECRET_KEY")
    
class DevelopmentConfig(Config):
    DEBUG = True
    PORT = environ.get('SERVER_PORT')
    HOST = '0.0.0.0'

class ProductionConfig(Config):
    PORT = environ.get('SERVER_PORT')
    HOST = '0.0.0.0'

config = {
    'mode': DevelopmentConfig if environ.get("DEBUG") == "True" else ProductionConfig
}