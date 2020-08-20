from . import controllers

@controllers.route('/cliente/<int:id>/', methods=['GET'])
def get_clientes(id):
    return str(id)