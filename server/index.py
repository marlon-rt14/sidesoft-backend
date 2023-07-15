from app import app
from config import config

if __name__ == '__main__':
    app.config.from_object(config['mode'])
    app.run(port=app.config['PORT'], host=app.config['HOST'])