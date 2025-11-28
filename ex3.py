from flask import Blueprint

exercicio3_routes = Blueprint("ex3", __name__)

@exercicio3_routes.route("/saudar/<nome>")
def saudar(nome):
    nome_formatado = nome.capitalize()
    return f"Olá, {nome_formatado}!"