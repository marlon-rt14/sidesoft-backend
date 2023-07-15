from app import app
from config import  DevelopmentConfig

if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)
    app.run(port=app.config['PORT'], host=app.config['HOST'])