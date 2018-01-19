import pygame

running = True
pygame.init()
clock = pygame.time.Clock()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
def draw_border():
    pygame.draw.line(screen, pygame.Color('white'), (0,0), (width, 0), 15)
    pygame.draw.line(screen, pygame.Color('white'), (0,0), (0, height), 15)
    pygame.draw.line(screen, pygame.Color('white'), (width, 0), (width, height), 15)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        draw_border()
    pygame.display.flip()