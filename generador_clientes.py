import random
from cliente import Cliente

def crear_cliente(id_actual):
    productos = random.randint(1, 10)
    return Cliente(id_actual, productos)
