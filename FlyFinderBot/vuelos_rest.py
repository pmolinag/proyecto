import test_vuelos
from flask import Flask, jsonify, request
app = Flask(__name__)

vuelos_prueba = test_vuelos.vuelos()
vuelos_prueba.insertaVuelo( "Granada", "Barcelona",50)
vuelos_prueba.insertaVuelo( "Madrid", "Paris",50)

@app.route('/')
def test():
    return {'Status' : 'OK'}

@app.route('/dest', methods=['GET'])
def get_dest():
    return jsonify({'Ciudades destino' : vuelos_prueba.cdestino})

@app.route('/dest/<string:name>', methods=['GET'])
def get_dest_particular(name):
    if vuelos_prueba.compruebaDestino(name) == True:
        return jsonify({'Existe ese destino.' : name})
    else:
        return jsonify({'No existe. ' : name})

@app.route('/orig', methods=['GET'])
def get_orig():
    return jsonify({'Ciudades origen' : vuelos_prueba.corigen})

@app.route('/orig/<string:name>', methods=['GET'])
def get_orig_particular(name):
    if vuelos_prueba.compruebaOrigen(name) == True:
        return jsonify({'Existe ese origen.' : name})
    else:
        return jsonify({'No existe. ' : name})

@app.route('/vuelos', methods=['GET'])
def get_vuelos():
    return jsonify({'Vuelos ' : vuelos_prueba.vuelos})

@app.route('/vuelos/<string:fly>', methods=['GET'])
def get_vuelo_particular(fly):
    if vuelos_prueba.compruebaVuelo(fly) == True:
        return jsonify({'Existe ese vuelo.' : fly})
    else:
        return jsonify({'No existe. ' : fly})

@app.route('/vuelo/<string:flyor>/<string:flydest>/<int:flymon>')
def insertar_vuelo(flyor, flydest, flymon):
    vuelos_prueba.insertaVuelo(flyor, flydest, flymon)

    return jsonify({'Vuelos ' : vuelos_prueba.vuelos})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
