from itertools import groupby

import requests
from flask import Blueprint, render_template, request, redirect, url_for
from utils.connection import sidesoft_api

product = Blueprint('product', __name__)

@product.route('', methods=['POST'])
def get_products():
    try:
        # recuperar los parametros de la peticion
        username = request.form["username"]
        password = request.form["password"]

        # configurar los headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic VEVTVDoxMjM0",
        }

        # realizar la peticion
        response = requests.get(
            sidesoft_api,
            auth=(username, password),
            headers=headers
        )
        
        #convertir la respuesta a json
        data = response.json()
        
        # estraer el total de regitros
        total = data['response']['totalRows']

        products = data['response']['data']
        
        # ordenar y agrupar los productos mediante 'producto'
        products.sort(key=lambda x: x['product'])
        new_products = []
        for key, group in groupby(products, lambda x: x['product']):
            my_group = list(group)
            quantity = 0
            for x in my_group:
                quantity += x['quantityOnHand']
            new_products.append({'product': key, 'rows': my_group, 'quantity': quantity})
            
        # filtrar las unidades de medida que no sean 'UNIDAD'
        products_unit =[product for product in products if product['uOM$_identifier'] != 'UNIDAD']
        
        # ordenar los productos por el stock de mayor a menor
        products.sort(key=lambda x: x['quantityOnHand'], reverse=True)
        sorted_products = products[:10]
        
        # retornar la vista
        return render_template("products.html", total=total, new_products=new_products, products_unit=products_unit, sorted_products=sorted_products)
    except Exception as e:
        # lanzar un error
        return 'Error: ' + str(e)

