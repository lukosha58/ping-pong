import pygame, sys

pygame.init()
running = True
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images\\bg.png")
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)


class GUI:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self, surface):
        for element in self.elements:
            render = getattr(element, "render", None)
            if callable(render):
                element.render(surface)

    def update(self):
        for element in self.elements:
            update = getattr(element, "update", None)
            if callable(update):
                element.update()

    def get_event(self, event):
        for element in self.elements:
            get_event = getattr(element, "get_event", None)
            if callable(get_event):
                element.get_event(event)


class ButtonMenu:
    def __init__(self, rect, text):
        self.Rect = pygame.Rect(rect)
        self.text = text
        self.font = pygame.font.Font('font\pixel.ttf', 30)
        self.pressed = False
        self.collided = False
        self.font_color = [pygame.Color("black"), pygame.Color("white")]

    def render(self, surface):
        if self.collided:
            self.rendered_text = self.font.render(self.text, 1, self.font_color[1])
            self.rendered_rect = self.rendered_text.get_rect(x=self.Rect.x, y=self.Rect.y)
            surface.blit(self.rendered_text, self.rendered_rect)
        else:
            self.rendered_text = self.font.render(self.text, 1, self.font_color[0])
            self.rendered_rect = self.rendered_text.get_rect(x=self.Rect.x + 2, y=self.Rect.y + 2)
            surface.blit(self.rendered_text, self.rendered_rect)

    def get_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.collided = self.Rect.collidepoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.pressed = self.Rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.pressed = False


bg = Background()
bg_help = Background()
gui = GUI()
play = ButtonMenu((width - 300, 250, 100, 50), "Играть")
help = ButtonMenu((width - 300, 380, 100, 50), "Помощь")
exit = ButtonMenu((width - 300, 510, 100, 50), "Выход")
back = ButtonMenu((width - 300, 510, 100, 50), "Назад")
gui.add_element(play)
gui.add_element(help)
gui.add_element(exit)
pygame.mixer.init()
menu_music = pygame.mixer.Sound('music\menu_music.ogg')
menu_music.play(300)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if exit.pressed:
            sys.exit()
        if play.pressed:
            running = False
        gui.get_event(event)

    if help.pressed:
        gui.add_element(back)
        introText = ["W и S - чтобы управлять левой ракеткой",
                     "↑ и ↓ - чтобы управлять правой ракеткой",
                     "space - приостановить игру"]

        screen.fill(pygame.Color('blue'))
        font = pygame.font.Font('font\pixel.ttf', 14)
        screen.blit(bg_help.image, (0, 0))
        textCoord = 250
        for line in introText:
            stringRendered = font.render(line, 1, pygame.Color('black'))
            introRect = stringRendered.get_rect()
            textCoord += 10
            introRect.top = textCoord
            introRect.x = width // 2 - 200
            textCoord += introRect.height
            screen.blit(stringRendered, introRect)
        gui.elements = [back]
        gui.render(screen)
        if back.pressed:

            gui.elements = [play, help, exit]
            help.pressed = False
            back.pressed = False
    else:
        screen.blit(bg.image, (0, 0))
        gui.render(screen)
        gui.update()
    pygame.display.flip()

pygame.quit()
