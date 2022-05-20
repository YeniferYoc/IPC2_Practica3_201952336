from flask import Flask, Response,json, request, jsonify
from flask_cors import CORS
from Cliente import *
from CRUD_CLIENTES import *

crud = Crud_clientes()

# Inicializar flask
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})

# Métodos de peticiones

# GET -> recuperar informacion
# POST -> enviar informacion
# DELETE -> eliminar informacion
# PUT -> insertar informacion

# Códigos de HTTP

# 200 -> ok
# 201 -> objeto creado
# 400 -> peticion incorrecta
# 404 -> no se encontro


# Ruta Raiz
@app.route('/', methods=["GET"])
def Raiz():
    return jsonify({ "mensaje": "Servidor Levantado"}), 200

@app.route('/agregar', methods=["POST"])
def Agregar():
    # Parametros que nos envia el frontend
    
    nombre = str(request.args.get('nombre'))
    dpi = int(request.args.get('dpi'))
    print("----------------------- SE ESTA EJECUTANDO UN METODO POST -----------------------")
    

    resultado = crud.AgregarCliente(dpi, nombre)
    print(resultado)
    return str(resultado)

# LETRAS ------------------------- FRASES 
@app.route('/actualizar', methods=["PUT"])
def actualizar():
    # Parametros que nos envia el frontend
    print("entro")
    dpi = int(request.args.get('dpi'))
    nombre = request.args.get('nombre')
    
    print('----------------------- SE ESTA EJECUTANDO UN METODO PUT -----------------------')

    resultado = crud.Actualizar_cliente(dpi, nombre)
    return str(resultado)

@app.route('/borrar', methods=["DELETE"])
def borrar():
    # Parametros que nos envia el frontend
    print("entro")
    dpi = int(request.args.get('dpi'))
    
    print('----------------------- SE ESTA EJECUTANDO UN METODO DELETE -----------------------')

    resultado = crud.Borrar_cliente(dpi)
    return str(resultado)

@app.route('/mostrar', methods=["GET"])
def mostrar():
    print("----------------------- SE ESTA EJECUTANDO UN METODO GET -----------------------")
    
    resultado = crud.MostrarTodos()
    return str(resultado)


if __name__ == '__main__':
    app.run(debug=True, port=4000)

