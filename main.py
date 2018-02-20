import pygame, sys
from pad import Player, Enemy
from ball import Ball
from main_menu import *

running = True
pygame.init()
pygame.display.set_caption('ping-pong')
clock = pygame.time.Clock()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen.fill(pygame.color.Color('darkgreen'))
horizontal_borders = pygame.sprite.Group()
sprite_ball = pygame.sprite.Group()
left_pad_sprite = pygame.sprite.Group()
right_pad_sprite = pygame.sprite.Group()


class Borders(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(horizontal_borders)
        self.image = pygame.Surface([x2 - x1, 15])
        self.rect = pygame.Rect(x1, y1, x2, y2)
        self.image.fill(pygame.Color('white'))


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('font\pixel.ttf', size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


left_pad = Player(width, height, left_pad_sprite)
right_pad = Enemy(width, height, right_pad_sprite)
ball = Ball(screen.get_rect().center, width, sprite_ball)
Borders(0, 0, width, 0)
Borders(0, height - 10, width, height)
pause = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                draw_text(screen, 'PAUSE', width // 2, height // 2, 30)
    if not pause:
        screen.fill(pygame.color.Color('darkgreen'))
        pygame.draw.line(screen, pygame.Color('white'), (width // 2, 0), (width // 2, height), 8)
        sprite_ball.draw(screen)
        sprite_ball.update(right_pad_sprite, left_pad_sprite, left_pad, right_pad)
        horizontal_borders.draw(screen)
        left_pad_sprite.update()
        left_pad_sprite.draw(screen)
        right_pad_sprite.update()
        right_pad_sprite.draw(screen)
        if left_pad.score == 10:
            ball.move_v = (0, 0)
        elif right_pad.score == 10:
            ball.move_v = (0, 0)
        draw_text(screen, str(left_pad.score), 80, width // 4, 20)
        draw_text(screen, str(right_pad.score), 80, width - 200, 20)
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
