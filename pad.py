import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, w, h,group):
        self.x = 0
        self.y = h // 2 - 50
        super().__init__(group)
        self.image = pygame.Surface([15, 150])
        self.rect = pygame.Rect(self.x, self.y, 15, 150)
        self.v = 5
        self.score = 0
        pygame.draw.rect(self.image, pygame.Color('purple'), self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.rect.y -= self.v
        if pressed[pygame.K_s]:
            self.rect.y += self.v
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())


class Enemy(pygame.sprite.Sprite):
    def __init__(self, w, h, group):
        self.x = w - 15
        self.y = h // 2 - 50
        super().__init__(group)
        self.image = pygame.Surface([15, 150])
        self.rect = pygame.Rect(self.x, self.y, 15, 150)
        self.score = 0
        self.v = 5
        pygame.draw.rect(self.image, pygame.Color('purple'), self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.rect.y -= self.v
        if pressed[pygame.K_DOWN]:
            self.rect.y += self.v
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())
