from modelos.personaje import Guerrero, Mago


def test_encapsulamiento_vida():
    guerrero = Guerrero("Aragorn")
    assert guerrero.vida == 120

    guerrero.recibir_daño(200)
    assert guerrero.vida == 0


def test_polimorfismo_ataque():
    guerrero = Guerrero("Thorin")
    mago = Mago("Gandalf")

    vida_inicial = mago.vida
    resultado = guerrero.atacar(mago)

    assert "Guerrero" in resultado
    assert mago.vida < vida_inicial


def test_composicion_inventario():
    mago = Mago("Merlín")
    mago.inventario.agregar_item("Poción de maná")

    assert "Poción de maná" in mago.inventario.listar_items()


def test_creacion_y_validacion_nombre():
    mago = Mago("  Gandalf  ")
    assert mago.nombre == "Gandalf"

    try:
        Mago("   ")
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError para nombre vacío.")
