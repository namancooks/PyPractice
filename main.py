import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
BIRD_SIZE = 30
GRAVITY = 0.5
FLAP_VELOCITY = -10
PIPE_WIDTH = 50
PIPE_HEIGHT = 300
PIPE_GAP = 150
PIPE_SPEED = 3

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird properties
bird_x = WIDTH // 4
bird_y = HEIGHT // 2
bird_velocity = 0

# Pipe properties
pipe_x = WIDTH
pipe_y = HEIGHT // 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = FLAP_VELOCITY

    # Update bird position
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # Update pipe position
    pipe_x -= PIPE_SPEED
    if pipe_x < -PIPE_WIDTH:
        pipe_x = WIDTH
        pipe_y = HEIGHT // 2

    # Check for collisions
    if bird_y < 0 or bird_y > HEIGHT - BIRD_SIZE:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, PIPE_WIDTH, pipe_y))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_y + PIPE_GAP, PIPE_WIDTH, HEIGHT))
    pygame.draw.rect(screen, (255, 0, 0), (bird_x, bird_y, BIRD_SIZE, BIRD_SIZE))

    pygame.display.flip()
    pygame.time.Clock().tick(60)


