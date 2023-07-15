from flask import Blueprint, render_template

router_client = Blueprint("router", __name__)

from .auth import auth
from .product import product

@router_client.route('', methods=['GET'])
def index():
    return render_template('index.html')

router_client.register_blueprint(auth, url_prefix="/auth")
router_client.register_blueprint(product, url_prefix="/products")