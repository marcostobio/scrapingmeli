import pandas as pd
from flask import Flask,jsonify,request

import json
from scraping import allproducto,conlimite

app = Flask(__name__)

@app.route("/mercadoLibre",methods=["GET"])

def mercadoLibre():
    print(request.data,type(request.data))
    data = json.loads(request.data)
    print(data,type(data))
    print(data["producto"])
   
    if 'limite' not in data:

        titulos,urls,precios = allproducto(data["producto"])
    else:
        titulos,urls,precios = conlimite(data["producto"],data["limite"])
    return jsonify({"datos":{"titulos":titulos,"urls":urls,"precios":precios}})

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)