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
    def __init__(self, id_s, nombre, precio_base):
        if not nombre or not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ErrorValidacion("Nombre del servicio inválido.")
        if not isinstance(precio_base, (int, float)) or precio_base < 0:
            raise ErrorValidacion("Precio base debe ser número no negativo.")
        if not isinstance(id_s, int) or id_s <=0:
            raise ErrorValidacion("ID del servicio debe ser entero positivo.")
        self.id = id_s
        self.nombre = nombre.strip()
        self.precio_base = precio_base

    #Métodos abstractos para calcular costo y descripción
    @abstractmethod
    def calcular_costo(self, descuento=0.0, impuesto=0.19):
        """
        Método sobrecargado para calcular costo final.
        Parámetros opcionales:
        - descuento: monto a descontar (float >=0)
        - impuesto: tasa impositiva (float entre 0 y 1)
        """
        pass
    
    #método abstracto para descripción del servicio
    @abstractmethod
    def descripcion(self):
        """Descripción del servicio."""
        pass

#Servicios especializados
class ReservaSala(Servicio):
    def calcular_costo(self, descuento=0.0, impuesto=0.19):
        base = max(0, self.precio_base - descuento)
        #+50 por servicio adicional
        costo = base * (1 + impuesto) + 50  
        return round(costo, 2)

    #Método para describir el servicio de reserva de sala
    def descripcion(self):
        return f"Reserva de Sala: {self.nombre} - Precio Base: {self.precio_base}"

#Servicio de alquiler de equipo con recargo adicional
class AlquilerEquipo(Servicio):
    def calcular_costo(self, descuento=0.0, impuesto=0.19):
        base = max(0, self.precio_base - descuento)
        #+10% recargo por alquiler de equipo
        costo = base * (1 + impuesto) * 1.10  
        return round(costo, 2)

    #Método para describir el servicio de alquiler de equipo
    def descripcion(self):
        return f"Alquiler de Equipo: {self.nombre} - Precio Base: {self.precio_base}"

#Servicio de asesoría con costo fijo adicional
class Asesoria(Servicio):
    def calcular_costo(self, descuento=0.0, impuesto=0.19):
        base = max(0, self.precio_base - descuento)
        #+100 por asesoría
        costo = base * (1 + impuesto) + 100  
        return round(costo, 2)

    #Método para describir el servicio de asesoría
    def descripcion(self):
        return f"Asesoría especializada: {self.nombre} - Precio Base: {self.precio_base}"

#Clase de reserva
class Reserva:
    def __init__(self, cliente, servicio, duracion):
        from excepciones import ErrorValidacion
        if cliente is None or servicio is None:
            raise ErrorValidacion("Cliente y Servicio no pueden ser nulos.")
        if not isinstance(duracion, int) or duracion <= 0:
            raise ErrorValidacion("Duración debe ser entero positivo.")
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"  
        #Otros estados pueden ser: Confirmada, Cancelada

    #Métodos para cambiar estado de la reserva
    def confirmar(self):
        self.estado = "Confirmada"

    #Método para cancelar la reserva
    def cancelar(self):
        self.estado = "Cancelada"

    #Método para procesar la reserva con validación de estado
    def procesar(self):
        if self.estado != "Pendiente":
            raise ErrorValidacion(f"No se puede procesar una reserva en estado '{self.estado}'.")
        self.confirmar()

    #Método para calcular costo total de la reserva con opciones de descuento e impuesto
    def costo_total(self, descuento=0.0, impuesto=0.19):
        return self.servicio.calcular_costo(descuento, impuesto) * self.duracion

    def __str__(self):
        return (f"Reserva de {self.cliente.nombre} para {self.servicio.nombre} "
                f"duración: {self.duracion} horas, estado: {self.estado}")