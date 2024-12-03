Se le da la oportunidad al usuario si quiere interactuar con la aplicación vía HTTP o vía CLI y en dependencia de la opción que se elija la salida va a ser o un Response HTTP o la escritura en un archivo.

Creación del ambiente virtual
python -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

Curl de ejemplo
curl -X POST http://127.0.0.1:5000/saludo -H "Content-Type: application/json" -d '{"nombre": "John", "apellidos": "Doe", "rol": "Developer"}'

El archivo de salida secreará en la raiz del proyecto con el nombre empleados.txt

