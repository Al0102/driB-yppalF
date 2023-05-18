import pygame


class Main:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1024, 768))

        self.background = pygame.image.load("assets/background.png").convert_alpha() #load image
        self.background = pygame.transform.scale(self.background, (self.display.get_width(), self.display.get_height())) #fits to new height
        self.bg_rect = self.background.get_rect()

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