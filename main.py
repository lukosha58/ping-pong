import pygame, sys
from pad import Player, Enemy
from ball import Ball
from main_menu import *

running = True
pygame.init()
pygame.display.set_caption('ping-pong')
clock = pygame.time.Clock()
SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
screen.fill(pygame.color.Color('lightgreen'))
horizontal_borders = pygame.sprite.Group()
sprite_ball = pygame.sprite.Group()
left_pad_sprite = pygame.sprite.Group()
right_pad_sprite = pygame.sprite.Group()


class Borders(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(horizontal_borders)
        self.image = pygame.Surface([x2 - x1, 10])
        self.rect = pygame.Rect(x1, y1, x2, y2)
        pygame.draw.rect(self.image, pygame.Color('black'), self.rect)


font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


left_pad = Player(WIDTH, HEIGHT, left_pad_sprite)
right_pad = Enemy(WIDTH, HEIGHT, right_pad_sprite)
ball = Ball(screen.get_rect().center, WIDTH, sprite_ball)
Menu(punkts).menu()
Borders(0, 0, WIDTH, 0)
Borders(0, HEIGHT - 10, WIDTH, HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.color.Color('lightgreen'))
    pygame.draw.line(screen, pygame.Color('black'), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 8)
    sprite_ball.draw(screen)
    sprite_ball.update(right_pad_sprite, left_pad_sprite, left_pad, right_pad)
    horizontal_borders.draw(screen)
    left_pad_sprite.update()
    left_pad_sprite.draw(screen)
    right_pad_sprite.update()
    right_pad_sprite.draw(screen)
    if (left_pad.score or right_pad.score) == 10:
        sys.exit()
    draw_text(screen, str(left_pad.score), 80, WIDTH // 4, 20)
    draw_text(screen, str(right_pad.score), 80, WIDTH - 200, 20)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
