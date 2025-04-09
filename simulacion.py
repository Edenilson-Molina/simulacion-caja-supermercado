import pygame
from config import *
from caja import Caja
from gestor_cajas import cliente_a_caja
from generador_clientes import crear_cliente

def correr_simulacion(ventana, num_cajas):
    reloj = pygame.time.Clock()
    cajas = [Caja(150 + i * 120) for i in range(num_cajas)]
    cliente_id = 1
    frames = 0
    corriendo = True

    while corriendo:
        tiempo_delta = reloj.tick(FPS) / 1000.0
        ventana.fill(BLANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        frames += 1
        if frames >= TIEMPO_ENTRE_CLIENTES:
            frames = 0
            nuevo = crear_cliente(cliente_id)
            cliente_a_caja(nuevo, cajas)
            cliente_id += 1

        for caja in cajas:
            caja.atender()
            caja.dibujar(ventana)

        pygame.display.update()
