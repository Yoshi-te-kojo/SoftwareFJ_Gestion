from abc import ABC, abstractmethod
from excepciones import ErrorValidacion

#Clases de entidades
class Cliente:
    def __init__(self, nombre, id_cliente):
        if not nombre or not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ErrorValidacion("El nombre del cliente es inválido.")
        if not isinstance(id_cliente, int) or id_cliente <= 0:
            raise ErrorValidacion("El ID del cliente debe ser un entero positivo.")
        self.__nombre = nombre.strip()
        self.__id = id_cliente

    #Propiedades para acceder a los atributos privados
    @property
    def nombre(self):
        return self.__nombre
    #Propiedad para acceder al ID del cliente
    @property
    def id(self):
        return self.__id
    #Método para representar el cliente como cadena
    def __str__(self):
        return f"Cliente[{self.__id}]: {self.__nombre}"

#Clase abstracta para servicios
class Servicio(ABC):
   # --- CLASE ABSTRACTA PARA SERVICIOS ---
class Servicio(ABC):
    def _init_(self, id_servicio, cliente):
        self.id_servicio = id_servicio
        self.cliente = cliente # Aquí pasamos el objeto Cliente que ya tienes

    @abstractmethod
    def calcular_costo(self):
        """Método que será diferente para cada tipo de servicio (Polimorfismo)"""
        pass

    def _str_(self):
        return f"Servicio {self.id_servicio} - Cliente: {self.cliente.nombre}"

# --- CLASES HIJAS (IMPLEMENTACIÓN) ---

class ReservaSala(Servicio):
    def _init_(self, id_servicio, cliente, horas):
        super()._init_(id_servicio, cliente)
        self.horas = horas
        self.precio_hora = 50000

    def calcular_costo(self):
        # Polimorfismo: Cálculo basado en horas
        return self.horas * self.precio_hora

class AlquilerEquipo(Servicio):
    def _init_(self, id_servicio, cliente, dias):
        super()._init_(id_servicio, cliente)
        self.dias = dias
        self.precio_dia = 35000

    def calcular_costo(self):
        # Polimorfismo: Cálculo basado en días
        return self.dias * self.precio_dia

class Asesoria(Servicio):
    def _init_(self, id_servicio, cliente, tipo):
        super()._init_(id_servicio, cliente)
        self.tipo = tipo  # 'Basica' o 'Especializada'

    def calcular_costo(self):
        # Polimorfismo: Cálculo basado en tarifa fija
        tarifas = {'Basica': 100000, 'Especializada': 200000}
        return tarifas.get(self.tipo, 50000)

    def _str_(self):
        return f"Asesoría {self.tipo} para {self.cliente.nombre}"
