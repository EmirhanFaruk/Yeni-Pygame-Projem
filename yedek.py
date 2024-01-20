import pygame
from time import *
import random
import math
from pygame import mixer
"""
regular show müziğini ölme müziği yap
t pose
animasyonlar
the giant enemy spider

"""

# initialize the pygame
pygame.init()

# create the screen(width, height)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")


# Title and icon
pygame.display.set_caption("The Giant Enemy Spider")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# The Giant Enemy Spider


# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 500
playerX_change = 0
playerY_change = 0
alive = True
cheat = ""

"""

# Walking
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
background = pygame.image.load('background.png')
playerImg = pygame.image.load('player.png')


"""


"""

# about jumping
isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    win.blit(background, (0,0))
    pygame.display.update() 

"""



# Jump
jump_state = "ground"

# Small Enemy Spiders
spiderImg = []
spiderX = []
spiderY = []
spiderX_change = []
num_of_spiders = 4

for i in range(num_of_spiders):
    spiderImg.append(pygame.image.load("spider.png"))
    spiderX.append(random.randint(800, 1600))
    spiderY.append(505)
    spiderX_change.append(-1)


# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load("bullet.png")
bulletX = -5
bulletY = playerY + 40
bulletX_change = 10
bulletY_change = 0
bullet_state = "ready"


spidersKilled = 0


# Font
font = pygame.font.Font("freesansbold.ttf", 20)

textX = 10
textY = 10

# Showing how many spiders killed
kill_font = pygame.font.Font("freesansbold.ttf", 15)

# Game Over text
over_font = pygame.font.Font("freesansbold.ttf", 64)

# Anti Cheat
cheat_font = pygame.font.Font("freesansbold.ttf", 64)


def dont_cheat():
    cheat_text = cheat_font.render("DONT CHEAT", True, (255, 10, 10))
    screen.blit(cheat_text, (220, 200))    

def spiders_killed():
    kill_text = kill_font.render("Small spiders killed: " + str(spidersKilled), True, (0, 0, 0))
    screen.blit(kill_text, (10, 10))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 10, 10))
    screen.blit(over_text, (220, 270))
    spiders_killed()

def player(x, y):
    screen.blit(playerImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def spider(x, y, i):
    screen.blit(spiderImg[i], (x, y))


def isspiderdt(spiderX, spiderY, bulletX, bulletY):
    spiderbld = math.sqrt((math.pow(spiderX - bulletX, 2) + math.pow(spiderY - bulletY, 2)))
    if spiderbld < 10 or spiderX == 0:
        return True
    else:
        return False

def isplayerdt(spiderX, spiderY, playerX, playerY):
    playerspd = math.sqrt((math.pow(spiderX - playerX, 2) + math.pow(spiderY - playerY, 2)))
    if playerspd < 40 or spiderX < 0:
        return True
    else:
        return False


running = True
while running:
    pygame.time.delay(1)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if alive == True:
            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -1
                if event.key == pygame.K_RIGHT:
                    playerX_change = 3
                if event.key == pygame.K_UP:
                    if jump_state == "ground":
                        if playerY <= 500:
                            playerY_change = -2
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        # Get the current x coordinate of the spaceship
                        bulletX = playerX
                        bulletY = playerY
                        fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                if event.key == playerY < 470:
                    jump_state = "air"
                    playerY_change = 2
            
                



    TheGiantEnemySpiderImg = pygame.image.load("TheGiantEnemySpider.png")
    screen.blit(TheGiantEnemySpiderImg, (672, 422))



    

    # Checking for boundaries of spaceship so it doesn't go out of bounds

    playerX += playerX_change
    playerY += playerY_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if jump_state == "air":
        playerY_change = 2
    if playerY >= 500:
        playerY = 500
        jump_state = "ground"
    elif playerY <= 450:
        playerY = 450
        playerY_change = 2
        jump_state = "air"

    # Spider movement
    for i in range(num_of_spiders):
        playerdt = isplayerdt(spiderX[i], spiderY[i], playerX, playerY)
        # Death
        if playerdt:
            for j in range(num_of_spiders):
                spiderX_change[j] = 0
            game_over_text()
            alive = False
            playerX_change = 0
            playerY_change = 0
            playerY = 500
            playerImg = pygame.image.load("dplayer.png")
            break
        try:
            spiderX[i] += spiderX_change[i]
        except:
            spiderX[i] = spiderX[i]


            
        # Spider death
        spiderdt = isspiderdt(spiderX[i], spiderY[i], bulletX, bulletY)
        if spiderdt and bullet_state == "fire":
            spidersKilled += 1
            bulletX = -5
            bullet_state = "ready"          
            spiderX[i] = random.randint(800, 1600)
            
        spiders_killed()
        spider(spiderX[i], spiderY[i], i)


    # Bullet Movement
    if bulletX >= 800:
        bulletX = -5
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY + 8)
        bulletX += bulletX_change


        



    player(playerX, playerY)
    pygame.display.update()
