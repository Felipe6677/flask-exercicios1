from flask import Blueprint

exercicio7_routes = Blueprint("ex7", __name__)

@exercicio7_routes.route("/buscar/<item>")
def buscar(item):
    lista = ["banana", "maçã", "uva", "melancia"]

    for elemento in lista:
        if elemento.lower() == item.lower():
            return f"Item encontrado: {elemento}"

    return "Item não encontrado"
