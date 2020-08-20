from . import controllers

@controllers.route("/login")
def home():
    return 'login'
