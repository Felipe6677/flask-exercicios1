from flask import Blueprint, render_template

exercicio6_routes = Blueprint("ex6", __name__)

@exercicio6_routes.route("/pagina")
def pagina():
    return render_template("pagina.html")