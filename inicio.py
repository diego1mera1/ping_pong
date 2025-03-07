import pygame
import sys

# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tamaño de la ventana
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong con Menú")

# Fuentes
font = pygame.font.SysFont("Arial", 40)
font_small = pygame.font.SysFont("Arial", 30)

# Opciones de skins
skins = ["Default", "Cielo", "Verde"]
current_skin = 0

# Definir las palas y la pelota
paddle_width = 15
paddle_height = 100
ball_size = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 7, 7

# Función para dibujar el menú principal
def draw_menu(selected_option):
    screen.fill(BLACK)
    title_text = font.render("Pong", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

    # Jugar
    play_text = font.render("Jugar", True, WHITE if selected_option != 0 else GREEN)
    play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(play_text, play_rect)

    # Skins
    skin_text = font.render("Skins", True, WHITE if selected_option != 1 else GREEN)
    skin_rect = skin_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(skin_text, skin_rect)

    pygame.display.update()

# Función para dibujar la pantalla de selección de skins
def draw_skin_menu(selected_skin):
    screen.fill(BLACK)
    title_text = font.render("Selecciona un Skin", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

    # Mostrar las opciones de skins
    for i, skin in enumerate(skins):
        skin_text = font_small.render(skin, True, WHITE if selected_skin != i else GREEN)
        skin_rect = skin_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50 + i * 40))
        screen.blit(skin_text, skin_rect)

    pygame.display.update()

# Función para aplicar el skin seleccionado
def apply_skin(skin_index):
    global current_skin
    current_skin = skin_index

    if skin_index == 1:  # Skin Cielo
        screen.fill(RED)
    elif skin_index == 2:  # Skin Verde
        screen.fill(GREEN)
    else:  # Skin Default
        screen.fill(BLACK)

# Función principal del juego
def game_loop():
    global ball_x, ball_y, ball_dx, ball_dy, current_skin

    paddle1_y, paddle2_y = HEIGHT // 2 - paddle_height // 2, HEIGHT // 2 - paddle_height // 2
    paddle1_dy, paddle2_dy = 0, 0
    clock = pygame.time.Clock()

    # Configurar las palas y la pelota
    paddle1 = pygame.Rect(30, paddle1_y, paddle_width, paddle_height)
    paddle2 = pygame.Rect(WIDTH - 30 - paddle_width, paddle2_y, paddle_width, paddle_height)
    ball = pygame.Rect(ball_x, ball_y, ball_size, ball_size)

    while True:
        screen.fill(BLACK)
        
        # Detectar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    paddle2_dy = -10
                elif event.key == pygame.K_DOWN:
                    paddle2_dy = 10
                elif event.key == pygame.K_w:
                    paddle1_dy = -10
                elif event.key == pygame.K_s:
                    paddle1_dy = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle2_dy = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle1_dy = 0

        # Mover las palas
        paddle1.y += paddle1_dy
        paddle2.y += paddle2_dy

        # Mover la pelota
        ball.x += ball_dx
        ball.y += ball_dy

        # Rebotar pelota en las paredes
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy *= -1

        # Rebotar la pelota en las palas
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_dx *= -1

        # Controlar la posición de las palas (evitar que salgan de la pantalla)
        if paddle1.top < 0:
            paddle1.top = 0
        if paddle1.bottom > HEIGHT:
            paddle1.bottom = HEIGHT
        if paddle2.top < 0:
            paddle2.top = 0
        if paddle2.bottom > HEIGHT:
            paddle2.bottom = HEIGHT

        # Dibujar los objetos
        pygame.draw.rect(screen, WHITE, paddle1)
        pygame.draw.rect(screen, WHITE, paddle2)
        pygame.draw.ellipse(screen, WHITE, ball)

        pygame.display.update()
        clock.tick(60)

# Función para el menú de selección
def menu():
    in_menu = True
    selected_option = 0
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % 2  # Cambiar entre Jugar y Skins
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % 2  # Cambiar entre Jugar y Skins
                if event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Opción Jugar
                        game_loop()
                    elif selected_option == 1:  # Opción Skins
                        skin_menu()

        # Dibujar el menú principal
        draw_menu(selected_option)

# Función para el menú de selección de skins
def skin_menu():
    selected_skin = 0
    in_skin_menu = True
    while in_skin_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_skin = (selected_skin + 1) % len(skins)
                if event.key == pygame.K_UP:
                    selected_skin = (selected_skin - 1) % len(skins)
                if event.key == pygame.K_RETURN:
                    apply_skin(selected_skin)
                    in_skin_menu = False  # Volver al menú principal

        # Dibujar la pantalla de selección de skins
        draw_skin_menu(selected_skin)

# Iniciar el juego
menu()
