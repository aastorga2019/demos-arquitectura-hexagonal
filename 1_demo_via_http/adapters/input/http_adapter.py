from flask import Flask, request, jsonify
from application.use_cases import SaludoUseCase
from domain.empleado import Empleado
from ports.input.input_port import InputPort


class HttpAdapter(InputPort):
    def __init__(self, use_case: SaludoUseCase):
        self.use_case = use_case

    def procesar_empleado(self, empleado: Empleado) -> str:
        return self.use_case.procesar_solicitud(empleado)
