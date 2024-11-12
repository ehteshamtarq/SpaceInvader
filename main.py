import pygame

# Initalize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_Change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_Change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    playerX += playerX_Change
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    pygame.display.update()