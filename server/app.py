from flask import Flask, render_template
from flask_cors import CORS

from routes.client.router_client import router_client

app = Flask(__name__)
CORS(app)

# CONFIG
# app.config['SQLALCHEMY_ECHO'] = True

app.register_blueprint(router_client, url_prefix='/')