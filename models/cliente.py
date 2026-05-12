from datetime import datetime
from models.excepciones import ClienteInvalido

class Cliente:
    def __init__(self, id_cliente: str, nombre: str, email: str, telefono: str):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._fecha_registro = datetime.now()
        self._validar()

    def _validar(self):
        if not self._id_cliente or len(self._id_cliente) < 3:
            raise ClienteInvalido("El ID del cliente debe tener al menos 3 caracteres")
        if not self._nombre or len(self._nombre.strip()) < 3:
            raise ClienteInvalido("El nombre es inválido")
        if "@" not in self._email:
            raise ClienteInvalido("El email debe contener @")
        if len(self._telefono) < 7:
            raise ClienteInvalido("El teléfono debe tener al menos 7 dígitos")

    # Encapsulación
    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def nombre(self):
        return self._nombre

    def __str__(self):
        return f"Cliente[{self._id_cliente}] - {self._nombre}"
