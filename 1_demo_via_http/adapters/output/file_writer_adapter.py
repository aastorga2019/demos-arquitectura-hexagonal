from ports.output.output_port import OutputPort
from domain.empleado import Empleado

class FileWriterAdapter(OutputPort):
    def __init__(self, filename: str):
        self.filename = filename

    def escribir_empleado(self, empleado: Empleado) -> None:
        with open(self.filename, 'a') as f:
            f.write(f"{empleado}\n")
