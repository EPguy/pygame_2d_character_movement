import pygame

pygame.init()

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

GRAVITY = 0.7
PLAYER_RUN_SPEED = 2
PLAYER_JUMP_SPEED = 6
PLAYER_MASS = 0.7

class Character:
    def __init__(self, image, run_speed, jump_speed):
        self.original_image = image
        self.image = image
        self.rect = image.get_rect()
        self.movement = 0
        self.direction = 1
        self.run_speed = run_speed
        self.jump_speed = jump_speed
        self.isJump = False

    def isGround(self):
        return self.rect.y >= HEIGHT - self.image.get_height()

    def gravity(self):
        if(not self.isGround()):
            self.rect.y += GRAVITY

    def move(self):
        if(self.movement != 0):
            self.direction = self.movement / abs(self.movement)
            self.flip_image()
            self.rect.x += self.movement
        
        if(self.isJump):
            F = 0
            if self.jump_speed > 0:
                F = -(0.5 * PLAYER_MASS * (self.jump_speed ** 2))
            else:
                F = (0.5 * PLAYER_MASS * (self.jump_speed ** 2))

            if(self.rect.y + F > HEIGHT - self.image.get_height()):
                self.rect.y = HEIGHT - self.image.get_height()
            else:
                self.rect.y += F

            self.jump_speed -= 0.5

            if(self.isGround()):
                self.jump_speed = PLAYER_JUMP_SPEED
                self.isJump = False


    def flip_image(self):
        if self.direction == -1:
            self.image = self.original_image.copy()
        else:
            self.image = pygame.transform.flip(self.original_image, True, False)

    def jump(self):
        if(self.isGround()):
            self.isJump = True

    
    def update(self):
        self.gravity()
        self.move()

player = Character(pygame.image.load("./image/player.png"), PLAYER_RUN_SPEED, PLAYER_JUMP_SPEED)
player.rect.y = HEIGHT - player.image.get_height()
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.movement = PLAYER_RUN_SPEED
            if event.key == pygame.K_LEFT:
                player.movement = -PLAYER_RUN_SPEED
            if event.key == pygame.K_SPACE:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.movement = 0
            if event.key == pygame.K_LEFT:
                player.movement = 0

    screen.fill(WHITE)

    player.update()

    screen.blit(player.image, player.rect)
    pygame.display.update()