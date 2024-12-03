import argparse
from application.use_cases import SaludoUseCase
from adapters.output.file_writer_adapter import FileWriterAdapter
from domain.empleado import Empleado
from ports.input.input_port import InputPort

class CLIAdapter(InputPort):
    def __init__(self, use_case: SaludoUseCase):
        self.use_case = use_case

    def procesar_empleado(self, empleado: Empleado) -> str:
        self.use_case.procesar_y_escribir(empleado)
        return f"Empleado {empleado.nombre} guardado en archivo."

def main():
    parser = argparse.ArgumentParser(description='Procesar empleado desde CLI')
    parser.add_argument('--nombre', required=True)
    parser.add_argument('--apellidos', required=True)
    parser.add_argument('--rol', required=True)

    args = parser.parse_args()
    empleado = Empleado(args.nombre, args.apellidos, args.rol)
    
    file_writer = FileWriterAdapter('empleados.txt')
    cli_adapter = CLIAdapter(SaludoUseCase(file_writer))
    
    cli_adapter.procesar_empleado(empleado)

if __name__ == '__main__':
    main()
