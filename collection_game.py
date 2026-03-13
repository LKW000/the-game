import pygame
import sys

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
LAVA_RED = (255, 69, 0)
GOLD = (255, 215, 0)
SKY_BLUE = (135, 206, 235)
GRAY = (100, 100, 100)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coin Collector")
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        try:
            self.image_right = pygame.image.load("player.png").convert_alpha()
            self.image_right = pygame.transform.scale(self.image_right, (50, 50))
            self.image_left = pygame.transform.flip(self.image_right, True, False)
        except:
            self.image_right = pygame.Surface((50, 50))
            self.image_right.fill((0, 255, 0))
            self.image_left = self.image_right

        self.image = self.image_right
        self.rect = self.image.get_rect(midbottom=(100, 550))
        self.speed = 5
        self.gravity = 0.8
        self.jump_height = -16
        self.velocity_y = 0
        self.is_grounded = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = self.image_left
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = self.image_right
        if keys[pygame.K_SPACE] and self.is_grounded:
            self.velocity_y = self.jump_height
            self.is_grounded = False

    def apply_physics(self, floor_rect):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.colliderect(floor_rect):
            self.rect.bottom = floor_rect.top
            self.velocity_y = 0
            self.is_grounded = True
        else:
            self.is_grounded = False

    def reset(self):
         self.rect.x = 100 
         self.rect.y = 500
         self.velocity_y = 0


    def draw(self, surface):
        surface.blit(self.image, self.rect)

player = Player()
floor = pygame.Rect(0, 550, SCREEN_WIDTH, 50)
lava = pygame.Rect(300, 550, 200, 50)
coins = [
    pygame.Rect(150, 480, 20, 20),
    pygame.Rect(300, 400, 20, 20),
    pygame.Rect(450, 480, 20, 20),
    pygame.Rect(600, 400, 20, 20),
    pygame.Rect(700, 500, 20, 20)
]

font = pygame.font.SysFont("Arial", 72, bold=True)
win = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not win:
         player.handle_input()
         player.apply_physics(floor)

    if player.rect.colliderect(lava):
            print("Ouch! Resetting...")
            player.reset()

    for coin in coins[:]:
            if player.rect.colliderect(coin):
                coins.remove(coin)

    if len(coins) == 0:
            win = True

    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, GRAY, floor)
    pygame.draw.rect(screen, LAVA_RED, lava)
    
    for coin in coins:
        pygame.draw.ellipse(screen, GOLD, coin)

    player.draw(screen)

    if win:
        text = font.render("YOU WIN!", True, (0, 100, 0))
        screen.blit(text, text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))

    pygame.display.flip()
    clock.tick(FPS)
