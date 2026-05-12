from abc import ABC, abstractmethod
from models.excepciones import ParametroInvalido

class Servicio(ABC):
    """Clase Abstracta"""
    def __init__(self, id_servicio: str, nombre: str, precio_base: float):
        self._id_servicio = id_servicio
        self._nombre = nombre
        self._precio_base = precio_base
        self._validar()

    def _validar(self):
        if self._precio_base <= 0:
            raise ParametroInvalido("El precio base debe ser mayor a 0")

    @abstractmethod
    def calcular_costo(self, duracion: float = 1.0, **kwargs) -> float:
        """Método polimórfico"""
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass

    def __str__(self):
        return f"{self._nombre} (${self._precio_base:,.0f})"


class ReservaSala(Servicio):
    def __init__(self, id_servicio: str, nombre: str, precio_base: float, capacidad: int):
        super().__init__(id_servicio, nombre, precio_base)
        self.capacidad = capacidad

    def calcular_costo(self, duracion: float = 1.0, **kwargs) -> float:
        costo = self._precio_base * duracion
        if kwargs.get("es_fin_de_semana", False):
            costo *= 1.3
        return round(costo, 2)

    def descripcion(self) -> str:
        return f"Reserva de Sala '{self._nombre}' (Cap: {self.capacidad})"


class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio: str, nombre: str, precio_base: float, tipo_equipo: str):
        super().__init__(id_servicio, nombre, precio_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, duracion: float = 1.0, cantidad: int = 1, **kwargs) -> float:
        costo = self._precio_base * duracion * cantidad
        return round(costo, 2)

    def descripcion(self) -> str:
        return f"Alquiler de {self.tipo_equipo}"


class AsesoriaEspecializada(Servicio):
    def __init__(self, id_servicio: str, nombre: str, precio_base: float, experto: str):
        super().__init__(id_servicio, nombre, precio_base)
        self.experto = experto

    def calcular_costo(self, duracion: float = 1.0, **kwargs) -> float:
        costo = self._precio_base * duracion
        if kwargs.get("con_informe", False):
            costo += 150000
        return round(costo, 2)

    def descripcion(self) -> str:
        return f"Asesoría con {self.experto}"
