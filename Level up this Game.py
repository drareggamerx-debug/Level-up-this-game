import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader - Level Up")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)

clock = pygame.time.Clock()

background_image = pygame.image.load("background1.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

collision_sound = pygame.mixer.Sound("hit_sound.wav")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(0, HEIGHT - 150)


all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        score += 1
        collision_sound.play()

    screen.blit(background_image, (0, 0))

    all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()