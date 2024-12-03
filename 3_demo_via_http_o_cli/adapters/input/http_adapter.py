from flask import Flask, request, jsonify
from application.use_cases import SaludoUseCase
from domain.empleado import Empleado
from ports.input.input_port import InputPort

app = Flask(__name__)

class HttpAdapter(InputPort):
    def __init__(self, use_case: SaludoUseCase):
        self.use_case = use_case

    def procesar_empleado(self, empleado: Empleado) -> str:
        return self.use_case.procesar_y_responder(empleado)

http_adapter = HttpAdapter(SaludoUseCase(None))

@app.route('/get-data', methods=['POST'])
def saludo():
    data = request.json
    nombre = data.get('nombre')
    apellidos = data.get('apellidos')
    rol = data.get('rol')

    if not nombre or not apellidos or not rol:
        return jsonify({"error": "Faltan datos"}), 400

    empleado = Empleado(nombre, apellidos, rol)
    respuesta = http_adapter.procesar_empleado(empleado)
    
    return jsonify({"saludo": respuesta}), 200

if __name__ == '__main__':
    app.run(debug=True)
