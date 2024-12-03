from abc import ABC, abstractmethod
from domain.empleado import Empleado

class InputPort(ABC):
    @abstractmethod
    def procesar_empleado(self, empleado: Empleado) -> str:
        pass
