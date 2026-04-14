import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Car Racing")

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Clock
clock = pygame.time.Clock()

# Player Car
car_w, car_h = 50, 80
car_x = WIDTH // 2 - car_w // 2
car_y = HEIGHT - car_h - 10
car_speed = 6

# Enemy cars
enemy_list = []
enemy_speed = 5

# Road lines
line_y = 0

# Score
score = 0
font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 50)

# Function: create enemy
def create_enemy():
    x = random.randint(0, WIDTH - car_w)
    y = random.randint(-600, -100)
    return [x, y]

# Add enemies
for i in range(3):
    enemy_list.append(create_enemy())

# Function: draw road
def draw_road():
    screen.fill(GRAY)
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, WHITE, (WIDTH//2 - 5, i + line_y, 10, 20))

# Function: draw car
def draw_car(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, car_w, car_h))

# Function: draw enemies
def draw_enemies(enemies):
    for e in enemies:
        pygame.draw.rect(screen, RED, (e[0], e[1], car_w, car_h))

# Function: move enemies
def move_enemies(enemies):
    global score, enemy_speed
    for e in enemies:
        e[1] += enemy_speed
        if e[1] > HEIGHT:
            e[1] = random.randint(-200, -100)
            e[0] = random.randint(0, WIDTH - car_w)
            score += 1

# Function: check collision
def check_collision(enemies, x, y):
    for e in enemies:
        if (x < e[0] + car_w and
            x + car_w > e[0] and
            y < e[1] + car_h and
            y + car_h > e[1]):
            return True
    return False

# Game loop
running = True
game_over = False

while running:
    clock.tick(60)

    if not game_over:
        draw_road()

        # Move road lines
        line_y += 5
        if line_y > 40:
            line_y = 0

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= car_speed
        if keys[pygame.K_RIGHT]:
            car_x += car_speed

        # Boundaries
        car_x = max(0, min(WIDTH - car_w, car_x))

        # Move & draw enemies
        move_enemies(enemy_list)
        draw_enemies(enemy_list)

        # Draw player
        draw_car(car_x, car_y)

        # Collision
        if check_collision(enemy_list, car_x, car_y):
            game_over = True

        # Score text
        text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, (10, 10))

        # Increase difficulty
        if score % 5 == 0:
            enemy_speed += 0.01

    else:
        screen.fill(GRAY)
        over_text = big_font.render("GAME OVER", True, RED)
        score_text = font.render("Score: " + str(score), True, WHITE)
        restart_text = font.render("Press R to Restart", True, WHITE)

        screen.blit(over_text, (90, 200))
        screen.blit(score_text, (140, 270))
        screen.blit(restart_text, (90, 320))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reset game
                    car_x = WIDTH // 2 - car_w // 2
                    enemy_list = [create_enemy() for _ in range(3)]
                    score = 0
                    enemy_speed = 5
                    game_over = False

    pygame.display.update()

pygame.quit()