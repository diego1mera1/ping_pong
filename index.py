import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Cargar imágenes
background = pygame.image.load("fondoping.jpg")
ball_img = pygame.image.load("pelota.png")
ball2_img = pygame.image.load("pelotabasquet.png")

ball_img = pygame.transform.scale(ball_img, (20, 20))
background = pygame.transform.scale(pygame.image.load('fondoping.jpg'), (WIDTH, HEIGHT))

# Colores y configuración
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
FPS = 60
PUNTO1 = 0
PUNTO2 = 0

# Posiciones iniciales
left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball2 = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

ball_speed_x, ball_speed_y = 4, 4
ball2_speed_x, ball2_speed_y = 3, -5
paddle_speed = 6

# Controles
keys = {"w": False, "s": False, "up": False, "down": False}

# Bucle del juego
running = True
clock = pygame.time.Clock()
while running:
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys["w"] = True
            if event.key == pygame.K_s:
                keys["s"] = True
            if event.key == pygame.K_UP:
                keys["up"] = True
            if event.key == pygame.K_DOWN:
                keys["down"] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys["w"] = False
            if event.key == pygame.K_s:
                keys["s"] = False
            if event.key == pygame.K_UP:
                keys["up"] = False
            if event.key == pygame.K_DOWN:
                keys["down"] = False
    
    # Movimiento de las paletas
    if keys["w"] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys["s"] and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed
    if keys["up"] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys["down"] and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed
    
    # Movimiento de la pelota 1
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Movimiento de la pelota 2
    ball2.x += ball2_speed_x
    ball2.y += ball2_speed_y
    
    # Rebote de la pelota 1 (ball)
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1
    
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_speed_x *= -1
        PUNTO1 += 1

    # Rebote de la pelota 2 (ball2)
    if ball2.top <= 0 or ball2.bottom >= HEIGHT:  # Corregir rebote en el borde superior e inferior
        ball2_speed_y *= -1

    if ball2.colliderect(left_paddle) or ball2.colliderect(right_paddle):  # Corregir colisión con las palas
        ball2_speed_x *= -1

    if ball2.left <= 0 or ball2.right >= WIDTH:  # Si la pelota 2 se sale por los lados
        ball2.x, ball2.y = WIDTH // 2, HEIGHT // 2
        ball2_speed_x *= -1
        PUNTO2 += 1
    
    # Dibujar elementos
    pygame.draw.rect(screen, BLACK, left_paddle)
    pygame.draw.rect(screen, BLACK, right_paddle)
    screen.blit(ball_img, (ball.x, ball.y))
    
    # Mostrar la segunda pelota si los puntos son múltiplos de 7
    if PUNTO1 % 7 == 0 or PUNTO2 % 7 == 0:
        screen.blit(ball2_img, (ball2.x, ball2.y))
    
    # Mostrar el marcador en pantalla
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{PUNTO1} - {PUNTO2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
