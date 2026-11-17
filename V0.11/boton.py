import pygame

# Botón de salida: cuadrado rojo con el símbolo de "salir" ([>)
# Ocupa el mismo lugar que el botón anterior: x 360-410, y 10-50
def dibujar_boton_salida(pantalla):
    x, y = 360, 10
    blanco = (255, 255, 255)

    # Fondo rojo con borde oscuro
    pygame.draw.rect(pantalla, (200, 30, 30), (x, y, 50, 40))
    pygame.draw.rect(pantalla, (110, 10, 10), (x, y, 50, 40), 2)

    # Corchete "[" (cuadrado sin el lado derecho)
    pygame.draw.line(pantalla, blanco, (x + 10, y + 9), (x + 10, y + 31), 3)
    pygame.draw.line(pantalla, blanco, (x + 10, y + 9), (x + 24, y + 9), 3)
    pygame.draw.line(pantalla, blanco, (x + 10, y + 31), (x + 24, y + 31), 3)

    # Flecha ">" saliendo hacia la derecha
    pygame.draw.line(pantalla, blanco, (x + 20, y + 20), (x + 34, y + 20), 3)
    pygame.draw.polygon(pantalla, blanco, [(x + 33, y + 12), (x + 33, y + 28), (x + 43, y + 20)])
