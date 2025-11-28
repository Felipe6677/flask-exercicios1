from flask import Blueprint

exercicio4_routes = Blueprint("ex4", __name__)

@exercicio4_routes.route("/quadrado/<int:n>")
def quadrado(n):
    resultado = n * n
    return f"{n}² = {resultado}"