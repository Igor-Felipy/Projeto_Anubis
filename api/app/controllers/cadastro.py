from . import controllers

@controllers.route('/cadastro/<tipo>/', methods=['POST'])
def cadastro(tipo):
    pass

@controllers.route('/cadastro/entrega/', methods=['POST'])
def cad_entrega():
    pass