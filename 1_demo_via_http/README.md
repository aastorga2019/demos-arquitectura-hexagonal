Se envía una petición HTTP con los datos de un empleado, y se recibe un response con los mismos datos enviados, además de dejar también la respuesta en un archivo.

Creación del ambiente virtual
python -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

Curl de ejemplo
curl -X POST http://127.0.0.1:5000/saludo -H "Content-Type: application/json" -d '{"nombre": "John", "apellidos": "Doe", "rol": "Developer"}'

El archivo de salida secreará en la raiz del proyecto con el nombre empleados.txt

