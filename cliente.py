import random
from config import COLORES_CLIENTES, TIEMPO_PRODUCTO_BASE

class Cliente:
    def __init__(self, id_, productos):
        self.id = id_
        self.productos = productos
        self.color = random.choice(COLORES_CLIENTES)
        self.tiempo_restante = productos * TIEMPO_PRODUCTO_BASE
