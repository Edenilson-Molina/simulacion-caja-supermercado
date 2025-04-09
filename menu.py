import pygame
import pygame_gui

ANCHO, ALTO = 800, 600

class PantallaMenu:
    def __init__(self, ventana):
        self.ventana = ventana
        self.gestor_ui = pygame_gui.UIManager((ANCHO, ALTO))
        
        # Elementos de interfaz
        self.label_cajas = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((100, 100), (200, 30)),
            text="Número de cajas (1 a 8):",
            manager=self.gestor_ui
        )

        self.input_cajas = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((320, 100), (100, 30)),
            manager=self.gestor_ui
        )

        self.boton_simular = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 200), (200, 50)),
            text="Iniciar simulación",
            manager=self.gestor_ui
        )

        self.valor_cajas = 3  # valor por defecto

    def manejar_evento(self, evento):
        self.gestor_ui.process_events(evento)
        if evento.type == pygame.USEREVENT:
            if evento.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if evento.ui_element == self.boton_simular:
                    valor = self.input_cajas.get_text()
                    if valor.isdigit() and 1 <= int(valor) <= 8:
                        self.valor_cajas = int(valor)
                        return "simulacion", self.valor_cajas
        return "menu", None

    def actualizar(self, tiempo_delta):
        self.gestor_ui.update(tiempo_delta)

    def dibujar(self):
        self.ventana.fill((240, 240, 240))
        self.gestor_ui.draw_ui(self.ventana)
