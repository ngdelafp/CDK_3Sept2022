#!/bin/python

from flask import Flask, request

app = Flask(__name__)

# Metodos de API REST
@app.route('/')
def saludo():
    return '¡Hola desde mi servicio!'


@app.route('/saludo/<persona>')
def saludoDinamico(persona):
    return 'Hola %s, bienvenido!!!' % persona

@app.route('/cuadrado/<float:num>')
def calculaCuadrado(num):
    resp = num * num
    return 'Respuesta: %f' % resp

@app.route('/test', methods=['POST', 'GET'])
def recibeParams():
    textReturn = "Método no aceptado"
    if request.method == "POST":
        data = request.get_json()
        try:
            mascota = data['mascota']
            numero = data['num'] * 2
            textReturn = 'Se recibio: %si,' % mascota 
            textReturn = textReturn + ' por 2: %i' % numero
        except:
            textReturn = "Ocurrió un error"
    return textReturn

# Lanzamiento de servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)