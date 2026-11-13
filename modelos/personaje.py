from __future__ import annotations

from abc import ABC, abstractmethod

from modelos.inventario import Inventario


class Personaje(ABC):
    def __init__(self, nombre: str, vida: int, ataque_base: int):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self._nombre = nombre.strip()
        self._vida = max(0, vida)
        self._ataque_base = max(0, ataque_base)
        self.inventario = Inventario()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def vida(self) -> int:
        return self._vida

    @vida.setter
    def vida(self, nueva_vida: int):
        self._vida = max(0, nueva_vida)

    @property
    def ataque_base(self) -> int:
        return self._ataque_base

    @abstractmethod
    def atacar(self, objetivo: "Personaje") -> str:
        """Método abstracto implementado por cada tipo de personaje."""
        raise NotImplementedError

    def recibir_daño(self, cantidad: int):
        if cantidad < 0:
            raise ValueError("La cantidad de daño no puede ser negativa.")
        self.vida = self.vida - cantidad

    def esta_vivo(self) -> bool:
        return self._vida > 0


class Guerrero(Personaje):
    def __init__(self, nombre: str):
        super().__init__(nombre=nombre, vida=120, ataque_base=20)
        self.armadura = 10

    def atacar(self, objetivo: "Personaje") -> str:
        daño = self.ataque_base + 5
        objetivo.recibir_daño(daño)
        return (
            f"{self.nombre} (Guerrero) ataca con espada a {objetivo.nombre} "
            f"infligiendo {daño} de daño."
        )


class Mago(Personaje):
    def __init__(self, nombre: str):
        super().__init__(nombre=nombre, vida=80, ataque_base=30)
        self.mana = 100

    def atacar(self, objetivo: "Personaje") -> str:
        daño = self.ataque_base + 10
        objetivo.recibir_daño(daño)
        return (
            f"{self.nombre} (Mago) lanza una bola de fuego a {objetivo.nombre} "
            f"infligiendo {daño} de daño."
        )
