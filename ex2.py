from flask import Blueprint

exercicio2_routes = Blueprint("ex2", __name__)

@exercicio2_routes.route("/versao")
def versao():
    versao = "1.1.0"  
    return f"App v{versao}"