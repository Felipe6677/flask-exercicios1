from flask import Blueprint

exercicio1_routes = Blueprint("ex1", __name__)

@exercicio1_routes.route("/")
def index():
    return "<h1>Hello, Flask !!</h1>"