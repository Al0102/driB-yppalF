import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1920, 1080))
        self.background = pygame.image.load("assets/background.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.background.get_width(), self))
        self.bg_rect = self.background.get_rect()
        self.rect = pygame.Rect(0,0,10,10)
        self.running = True
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.display.blit(self.background, self.bg_rect)
            pygame.display.update()

if __name__ == "__main__":
    game = Main()
    game.run()