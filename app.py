from flask import Flask
from routes.pagina_clientes.clientes import clientes


app = Flask(__name__)

app.register_blueprint(clientes)
