import pygame
from menu import PantallaMenu
from simulacion import correr_simulacion

pygame.init()
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación de supermercado")

def main():
    estado = "menu"
    menu = PantallaMenu(ventana)

    while True:
        tiempo_delta = pygame.time.Clock().tick(60) / 1000.0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if estado == "menu":
                nuevo_estado, valor = menu.manejar_evento(evento)
                if nuevo_estado == "simulacion":
                    correr_simulacion(ventana, valor)
                    estado = "menu"

        if estado == "menu":
            menu.actualizar(tiempo_delta)
            menu.dibujar()
            pygame.display.update()

if __name__ == "__main__":
    main()
