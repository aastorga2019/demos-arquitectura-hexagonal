from abc import ABC, abstractmethod
from domain.empleado import Empleado

class OutputPort(ABC):
    @abstractmethod
    def escribir_empleado(self, empleado: Empleado) -> None:
        pass
