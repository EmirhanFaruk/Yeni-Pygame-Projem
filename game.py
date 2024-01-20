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
oyuncuyu postal dude yap

"""

# initialize the pygame
pygame.init()

# create the screen(width, height)
win = pygame.display.set_mode((1280, 720))

# Background
background = pygame.image.load("background2.png")


# Title and icon
pygame.display.set_caption("The Giant Enemy Spider")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


clock = pygame.time.Clock()



"""
effect = pygame.mixer.Sound('beep.wav')
effect.play()
"""

# Walking
effect = [pygame.mixer.Sound('grass_step1.wav'), pygame.mixer.Sound('grass_step1.wav'), pygame.mixer.Sound('grass_step2.wav'), pygame.mixer.Sound('grass_step3.wav'), pygame.mixer.Sound('grass_step4.wav'), pygame.mixer.Sound('grass_step5.wav'), pygame.mixer.Sound('grass_step6.wav'), pygame.mixer.Sound('grass_step7.wav')]
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png'), pygame.image.load('R10.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png'), pygame.image.load('L10.png')]
background = pygame.image.load('background2.png')
background2 = pygame.image.load('background3.png')
background_list = [background, background2]
emap = 0
eemap = 0
charr = pygame.image.load('player.png')
charl = pygame.image.load('playerleft.png')
gigip = pygame.image.load('gigi.png')



class player(object):
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkSound = 0
        self.walkSoundCount = 0
        self.walkSoundCheck = True
        self.jumpCount = 7
        self.direction = "right"
        self.hitbox = (self.x + 25, self.y, 14, 63)

    def draw(self, win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        if self.walkSoundCount + 1 >= 32:
            self.walkSoundCount = 0

        if self.walkSound > 0:
            self.walkSoundCheck = False
        
        if self.left:
            if self.walkSound == 0:
                random.choice(effect).play()
                print("yürüme sesi 0lı")
                if self.walkSoundCheck:
                    self.walkSound += 1
            print(self.walkSoundCount)
            if self.walkSoundCount % 15 == 0 and self.walkSoundCount != 0:
                if not(man[0].isJump):
                    random.choice(effect).play()
                    print("yürüme sesi")
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            self.walkSoundCount += 1
            self.direction = "left"
        elif self.right:
            if self.walkSound == 0:
                random.choice(effect).play()
                print("yürüme sesi 0lı")
                if self.walkSoundCheck:
                    self.walkSound += 1
            print(self.walkSoundCount)
            if self.walkSoundCount % 15 == 0 and self.walkSoundCount != 0:
                if not(man[0].isJump):
                    random.choice(effect).play()
                    print("yürüme sesi")
                    
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
            self.walkSoundCount += 1
            self.direction = "right"
        else:
            self.walkSoundCheck = True
            self.walkSound = 0
            if self.direction == "right":
                win.blit(charr, (self.x,self.y))
            if self.direction == "left":
                win.blit(charl, (self.x,self.y))
        self.hitbox = (self.x + 25, self.y, 14, 63)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class npc1(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x - 25, self.y, 14, 63)
        self.interaction = (self.x - 75, self.y - 7, 114, 80)
    def draw(self, win):
        win.blit(gigip, (self.x - 50, self.y))
        self.hitbox = (self.x - 25, self.y, 14, 63)
        self.interaction = (self.x - 75, self.y - 7, 114, 80)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        pygame.draw.rect(win, (0, 255, 0), self.interaction, 2)



def redrawGameWindow():
    win.blit(background, (0,0))
    man[0].draw(win)
    if emap == gigir[1]:    
        gigir[0].draw(win)
    pygame.display.update()

man = [player(162, 600, 64, 64, "right"), emap]
gigir = [npc1(500, 600, 64, 64), 1]
running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    if man[0].x > 1230:
        emap += 1
        if emap < len(background_list) and emap > -1:
            man[0].x = 10
            eemap = emap
            try:
                background = background_list[emap]
                print("map", emap)
            except:
                emap -= 1
                print("sağa gitme sınırı", emap)
        else:
            emap = eemap
            print("map sınırı sağ", emap)
        
    if man[0].x < 10:
        emap -= 1
        if emap < len(background_list) and emap > -1:
            man[0].x = 1215
            eemap = emap
            try:
                background = background_list[emap]
                print("map", emap)
            except:
                emap += 1
                print("sola gitme sınırı", emap)
        else:
            emap = eemap
            print("map sınırı sol", emap)
        
            

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man[0].x > 9:
        man[0].x -= man[0].vel
        man[0].left = True
        man[0].right = False
    elif keys[pygame.K_RIGHT] and man[0].x < 1240:
        man[0].x += man[0].vel
        man[0].right = True
        man[0].left = False
    else:
        man[0].right = False
        man[0].left = False
        man[0].walkCount = 0
        
    if not(man[0].isJump):
        if keys[pygame.K_UP]:
            man[0].isJump = True
            man[0].right = False
            man[0].left = False
            man[0].walkCount = 0
    else:
        if man[0].jumpCount >= -7:
            neg = 1
            if man[0].jumpCount < 0:
                neg = -1
            man[0].y -= (man[0].jumpCount ** 2) * 0.5 * neg
            man[0].jumpCount -= 1
        else:
            man[0].isJump = False
            man[0].jumpCount = 7

    redrawGameWindow()


    pygame.display.update()
