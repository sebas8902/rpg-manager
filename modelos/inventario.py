class Inventario:
    def __init__(self):
        self._items = []

    def agregar_item(self, item: str):
        if not item or not item.strip():
            raise ValueError("El nombre del ítem no puede estar vacío.")
        self._items.append(item.strip())

    def listar_items(self) -> list:
        return list(self._items)

    def limpiar(self):
        self._items.clear()
