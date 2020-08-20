from flask import Blueprint

controllers = Blueprint("controllers", __name__)

from . import login
from . import cliente
from . import entrega
from . import entregador
from . import controllers