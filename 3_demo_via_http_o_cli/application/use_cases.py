from domain.empleado import Empleado
from ports.output.output_port import OutputPort

class SaludoUseCase:
    def __init__(self, output_port: OutputPort):
        self.output_port = output_port

    def procesar_y_responder(self, empleado: Empleado) -> str:
        return f"Hola, {empleado.nombre} {empleado.apellidos}!"

    def procesar_y_escribir(self, empleado: Empleado) -> None:
        self.output_port.escribir_empleado(empleado)
