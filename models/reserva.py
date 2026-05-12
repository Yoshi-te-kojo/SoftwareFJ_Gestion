from datetime import datetime
from models.cliente import Cliente
from models.servicio import Servicio
from models.excepciones import ReservaInvalida

class Reserva:
    def __init__(self, id_reserva: str, cliente: Cliente, servicio: Servicio, duracion: float):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.fecha = datetime.now()
        self.estado = "pendiente"
        self.costo_total = 0.0
        self._validar()

    def _validar(self):
        if self.duracion <= 0:
            raise ReservaInvalida("La duración debe ser mayor a 0")

    def confirmar(self, **kwargs):
        try:
            self.costo_total = self.servicio.calcular_costo(self.duracion, **kwargs)
            self.estado = "confirmada"
            print(f"✅ Reserva {self.id_reserva} confirmada - Total: ${self.costo_total:,.2f}")
        except Exception as e:
            raise ReservaInvalida(f"Error al confirmar reserva: {e}")

    def cancelar(self):
        self.estado = "cancelada"
        print(f"❌ Reserva {self.id_reserva} ha sido cancelada.")

    def __str__(self):
        return f"Reserva {self.id_reserva} | {self.cliente.nombre} | {self.servicio} | {self.duracion}h | {self.estado}"
