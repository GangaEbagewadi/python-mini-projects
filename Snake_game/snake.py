import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load and scale images


HEAD_IMG = pygame.image.load('assets/snake_head.png')
BODY_IMG = pygame.image.load('assets/snake_body.png')
APPLE_IMG = pygame.image.load('assets/apple.png')

HEAD_IMG = pygame.transform.scale(HEAD_IMG, (GRID_SIZE, GRID_SIZE))
BODY_IMG = pygame.transform.scale(BODY_IMG, (GRID_SIZE, GRID_SIZE))
APPLE_IMG = pygame.transform.scale(APPLE_IMG, (GRID_SIZE, GRID_SIZE))

# Create the screen and maximize window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Snake Game")

# Snake initial position and size
snake = [(100, 100), (80, 100), (60, 100)]
direction = pygame.K_RIGHT

# Initial apple position
apple_position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, 
                  random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

# Game variables
running = True
clock = pygame.time.Clock()
score = 0

# Font for score
font = pygame.font.SysFont(None, 35)

def check_collision(pos1, pos2):
    return pos1 == pos2

def get_random_apple_position():
    return (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, 
            random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

def show_score():
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, [0, 0])

def game_over():
    screen.fill(WHITE)
    game_over_text = font.render("Game Over! Score: " + str(score), True, BLACK)
    screen.blit(game_over_text, [WIDTH // 3, HEIGHT // 3])
    play_again_text = font.render("Press R to Play Again or Q to Quit", True, BLACK)
    screen.blit(play_again_text, [WIDTH // 4, HEIGHT // 2])
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                direction = event.key

    # Move snake
    x, y = snake[0]
    if direction == pygame.K_UP:
        y -= GRID_SIZE
    elif direction == pygame.K_DOWN:
        y += GRID_SIZE
    elif direction == pygame.K_LEFT:
        x -= GRID_SIZE
    elif direction == pygame.K_RIGHT:
        x += GRID_SIZE
    new_head = (x, y)
    
    # Check for collision with apple
    if check_collision(new_head, apple_position):
        snake.append((0, 0))  # Add new segment to snake
        apple_position = get_random_apple_position()  # Reposition apple
        score += 1
    else:
        snake = [new_head] + snake[:-1]

    # Check for collisions with self or walls
    if new_head in snake[1:] or x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        if not game_over():
            running = False
        else:
            # Reset the game
            snake = [(100, 100), (80, 100), (60, 100)]
            direction = pygame.K_RIGHT
            apple_position = get_random_apple_position()
            score = 0

    # Clear screen
    screen.fill(WHITE)

    # Draw snake
    screen.blit(HEAD_IMG, snake[0])
    for segment in snake[1:]:
        screen.blit(BODY_IMG, segment)

    # Draw apple
    screen.blit(APPLE_IMG, apple_position)

    # Show score
    show_score()

    # Update the screen
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
