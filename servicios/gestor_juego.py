from modelos.personaje import Guerrero, Mago, Personaje


class GestorJuego:
    def __init__(self):
        self.personajes = []

    def crear_personaje(self, tipo: str, nombre: str) -> Personaje:
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        nombre = nombre.strip()
        if any(p.nombre.lower() == nombre.lower() for p in self.personajes):
            raise ValueError(f"Ya existe un personaje llamado '{nombre}'.")

        if tipo == "Guerrero":
            personaje = Guerrero(nombre)
        elif tipo == "Mago":
            personaje = Mago(nombre)
        else:
            raise ValueError("Tipo de personaje desconocido.")

        self.personajes.append(personaje)
        return personaje

    def simular_combate(self, p1: Personaje, p2: Personaje) -> str:
        if p1 is p2:
            return "Un personaje no puede atacarse a sí mismo."

        if not p1.esta_vivo() or not p2.esta_vivo():
            return "Uno de los personajes ya está derrotado."

        resultado1 = p1.atacar(p2)
        if not p2.esta_vivo():
            return (
                f"{resultado1}\n"
                f"{p2.nombre} ha caído en combate. ¡{p1.nombre} gana!"
            )

        resultado2 = p2.atacar(p1)
        if not p1.esta_vivo():
            return (
                f"{resultado1}\n{resultado2}\n"
                f"{p1.nombre} ha caído en combate. ¡{p2.nombre} gana!"
            )

        return (
            f"{resultado1}\n{resultado2}\n"
            "--- Estado ---\n"
            f"{p1.nombre}: {p1.vida} HP\n"
            f"{p2.nombre}: {p2.vida} HP"
        )
