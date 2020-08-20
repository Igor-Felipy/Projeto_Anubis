from . import controllers

@controllers.route('/entregas/<int:id_entrega>/', methods=['POST'])
def get_entrega(id_entrega):
    return str(id_entrega)