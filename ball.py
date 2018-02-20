import pygame, time
from random import choice


def add(u, v):
    return [u[i] + v[i] for i in range(len(u))]


class Ball(pygame.sprite.Sprite):
    def __init__(self, start_pos, width, group):
        self.width = width
        self.speed_x, self.speed_y = choice([-7, 7]), 1
        self.start_pos = start_pos
        self.x = start_pos[0]
        super().__init__(group)
        self.image = pygame.surface.Surface((20, 20))
        self.rect = self.image.get_rect(center=start_pos)
        pygame.draw.circle(self.image, pygame.color.Color('White'), self.image.get_rect().center, 10)
        self.image.set_colorkey(pygame.color.Color('Black'))
        self.impactObj = pygame.mixer.music.load("music\impact.ogg")
        self.mask = pygame.mask.from_surface(self.image)
        self.move_v = (self.speed_x, self.speed_y)
        self.pos = self.rect.center

    def update(self, group1, group2, pad1, pad2):
        if pygame.sprite.spritecollideany(self, group1) or pygame.sprite.spritecollideany(self, group2):
            self.move_v = [-self.move_v[0], choice([-self.move_v[1], self.move_v[1]])]
            pygame.mixer.music.play()
        if int(self.pos[0].real) < 0:
            pad2.score += 1
            pad2.v += 3
            pad1.v += 1
            self.move_v[0] *= 1.03
            self.rect = self.image.get_rect(center=self.start_pos)
        elif int(self.pos[0].real) >= self.width:
            pad1.score += 1
            pad1.v += 3
            pad2.v += 1
            self.move_v[0] *= 1.03
            self.rect = self.image.get_rect(center=self.start_pos)

        display = pygame.display.get_surface().get_rect()
        if self.rect.top < display.top + 10 and self.move_v[1] < 0 or self.rect.bottom + 10 > display.bottom and \
                        self.move_v[1] > 0:
            pygame.mixer.music.play()
            self.move_v = [self.move_v[0], choice([-self.move_v[1], self.move_v[1]])]

        self.pos = add(self.rect.center, self.move_v)
        self.rect.center = (int(self.pos[0].real), int(self.pos[1].real))
