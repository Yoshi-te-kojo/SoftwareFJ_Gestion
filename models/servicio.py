from abc import ABC, abstractmethod
from models.excepciones import ParametroInvalido

class Servicio(ABC):
    def __init__(self, id_servicio: str, nombre: str, precio_base: float):
        self._id_servicio = id_servicio
        self._nombre = nombre
        self._precio_base = precio_base
        self._validar()

    def _validar(self):
        if self._precio_base <= 0:
            raise ParametroInvalido("El precio base debe ser mayor a 0")

    @abstractmethod
    def calcular_costo(self, duracion: float, **kwargs) -> float:
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass

    def __str__(self):
        return f"{self._nombre} (${self._precio_base:,})"
