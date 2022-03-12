from flask import Blueprint, render_template

clientes = Blueprint("clientes", __name__)


@clientes.route("/")
def home():
    return render_template("/clientes/inicio.html")


@clientes.route("/servicios")
def services():
    return render_template("/clientes/servicios.html")


@clientes.route("/somos")
def about():
    return render_template("/clientes/about.html")


@clientes.route("/contactanos")
def contact():
    return render_template("/clientes/contactos.html")
