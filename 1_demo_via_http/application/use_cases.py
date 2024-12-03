from domain.empleado import Empleado
from ports.output.output_port import OutputPort

class SaludoUseCase:
    def __init__(self, output_port: OutputPort):
        self.output_port = output_port

    def procesar_solicitud(self, empleado: Empleado) -> str:
        self.output_port.escribir_empleado(empleado)
        return f"Usted es {empleado.nombre} {empleado.apellidos}!"
        
        