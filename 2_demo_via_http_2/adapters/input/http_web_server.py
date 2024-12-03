from flask import Flask, request, jsonify
from application.use_cases import SaludoUseCase
from domain.empleado import Empleado
from adapters.output.pubsub_writer_adapter import PubSubWriterAdapter
from adapters.input.http_adapter import HttpAdapter


app = Flask(__name__)

@app.route('/get-data', methods=['POST'])
def saludo():
    data = request.json
    nombre = data.get('nombre')
    apellidos = data.get('apellidos')
    rol = data.get('rol')

    if not nombre or not apellidos or not rol:
        return jsonify({"error": "Faltan datos"}), 400

    empleado = Empleado(nombre, apellidos, rol)
    pubsubClient = PubSubWriterAdapter("latamxp-sandbox", "demo-delivery")
    http_adapter = HttpAdapter(SaludoUseCase(pubsubClient))
    respuesta = http_adapter.procesar_empleado(empleado)
    
    return jsonify({"Datos personales": respuesta}), 200

if __name__ == '__main__':
    app.run(debug=True)
