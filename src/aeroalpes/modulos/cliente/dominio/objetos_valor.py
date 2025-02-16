"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from aeroalpes.seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombres: str
    apellidos: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    address: str
    dominio: str
    es_empresarial: bool

@dataclass(frozen=True)
class Cedula(ObjetoValor):
    numero: int
    ciudad: Ciudad

@dataclass(frozen=True)
class Rut(ObjetoValor):
    numero: int
    ciudad: Ciudad

@dataclass(frozen=True)
class TokenSeguridad(ObjetoValor):
    token: str

@dataclass
class MetodosPago(ObjetoValor):
    tipo: str  # Ejemplo: 'tarjeta de crédito', 'débito', 'transferencia bancaria'
    nombre: str
    token_seguridad: TokenSeguridad

    def actualizar_nombre(self, nuevo_nombre: str):
        self.nombre = nuevo_nombre

    def obtener_token(self) -> str:
        return self.token_seguridad.token

