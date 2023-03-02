from flask import Flask, Response, request
from json import dumps
from os.path import join
from werkzeug.utils import secure_filename

NEXT_ID = 0


class Product(dict):
    def __init__(self, name=None, description=None, icon_name=None):
        global NEXT_ID
        super().__init__(name=name, description=description, icon_name=icon_name)
        self.id = NEXT_ID
        self.name = name
        self.description = description
        self.icon_path = icon_name
        NEXT_ID += 1

    def update(self, name=None, description=None, icon_name=None):
        if name is not None:
            self['name'] = name
            self.name = name
        if description is not None:
            self['description'] = description
            self.description = description
        if icon_name is not None:
            self['icon_name'] = icon_name
            self.icon_path = icon_name


def save_icon(icon):
    if icon is None:
        return None
    icon_name = secure_filename(icon.filename)
    if icon_name == '':
        return None
    icon.save(join(app.config['UPLOAD_FOLDER'], secure_filename(icon_name)))
    return icon_name


products = dict()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './icons'


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return dumps(products)
    elif request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        icon = request.files.get('icon')
        icon_name = save_icon(icon)
        product = Product(name, description, icon_name)
        products[product.id] = product
        return 'ok'


@app.route('/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def product_page(pid):
    if pid not in products:
        return Response('Product not found', 404)
    if request.method == 'GET':
        return dumps(products[pid])
    elif request.method == 'PUT':
        name = request.form.get('name')
        description = request.form.get('description')
        icon = request.files.get('icon')
        icon_name = save_icon(icon)
        products[pid].update(name, description, icon_name)
        return 'ok'
    elif request.method == 'DELETE':
        products.pop(pid)
        return 'ok'
