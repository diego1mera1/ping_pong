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

ball_img = pygame.transform.scale(ball_img, (20, 20))
background = pygame.transform.scale(pygame.image.load('fondoping.jpg'), (WIDTH,HEIGHT))

# Colores y configuración
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
FPS = 60

# Posiciones iniciales
left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

ball_speed_x, ball_speed_y = 4, 4
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
    
    # Movimiento de la pelota
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1
    
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_speed_x *= -1
    
    # Dibujar elementos
    pygame.draw.rect(screen, BLACK, left_paddle)
    pygame.draw.rect(screen, BLACK, right_paddle)
    screen.blit(ball_img, (ball.x, ball.y))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
