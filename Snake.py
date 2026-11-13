import pygame

CELL = 20
COLS, ROWS = 24, 18

TURNS = {
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
}

pygame.init()
screen = pygame.display.set_mode((COLS * CELL, ROWS * CELL))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def draw_cell(cell, color):
    col, row = cell
    pygame.draw.rect(screen, color, (col * CELL + 1, row * CELL + 1, CELL - 2, CELL - 2))

head = (5, 9)
direction = (1, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key in TURNS:
            direction = TURNS[event.key]
    
    head = (head[0] + direction[0], head[1] + direction[1])

    screen.fill((30, 30, 46))
    draw_cell(head, (180, 255, 160))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
