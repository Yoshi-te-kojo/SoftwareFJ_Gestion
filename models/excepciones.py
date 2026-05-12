class ErrorSistema(Exception):
    """Excepción base del sistema"""
    pass

class ClienteInvalido(ErrorSistema):
    def __init__(self, mensaje="Datos del cliente son inválidos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ServicioInvalido(ErrorSistema):
    def __init__(self, mensaje="Datos del servicio son inválidos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ReservaInvalida(ErrorSistema):
    def __init__(self, mensaje="Datos de la reserva son inválidos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ParametroInvalido(ErrorSistema):
    def __init__(self, mensaje="Parámetro inválido"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
