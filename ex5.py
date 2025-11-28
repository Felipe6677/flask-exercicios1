from flask import Blueprint, redirect, url_for

exercicio5_routes = Blueprint("ex5", __name__)

@exercicio5_routes.route("/home")
def home():
    return redirect(url_for("ex1.index"))