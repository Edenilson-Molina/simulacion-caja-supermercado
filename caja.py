import pygame
from config import NEGRO

class Caja:
    def __init__(self, x):
        self.x = x
        self.y = 100
        self.ancho = 80
        self.cola = []

    def atender(self):
        if self.cola:
            cliente = self.cola[0]
            cliente.tiempo_restante -= 1
            if cliente.tiempo_restante <= 0:
                self.cola.pop(0)

    def agregar_cliente(self, cliente):
        if len(self.cola) < 5:
            self.cola.append(cliente)
            return True
        return False

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, NEGRO, (self.x, self.y - 30, self.ancho, 30))
        for i, cliente in enumerate(self.cola):
            pygame.draw.rect(ventana, cliente.color, (self.x, self.y + i * 40, self.ancho, 30))
