import pygame
import random

#Initializin pygame
pygame.init()

#setting screen
screen=pygame.display.set_mode((800,500))

#caption
pygame.display.set_caption('Space Warrior')

#icon
icon = pygame.image.load('spaceship icon.png')
pygame.display.set_icon(icon)

#background
Background=pygame.image.load('Background.jpg')

#player
playerimg=pygame.image.load('spaceship.png')
playerX=400
playerY=400
playerX_change=0
change_val=0.5  #fix change value

#enemy
enemyimg=pygame.image.load('ufo.png')
enemyX=random.randint(0,745)
enemyY=random.randint(50,150)
enemyX_change=change_val




def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y):
    screen.blit(enemyimg, (x,y))
#main game

status = True
while status:

    screen.fill((0,0,0))
    screen.blit(Background, (0,0))

    #load all events
    for event in pygame.event.get():
        #check if user click exit button
        if event.type==pygame.QUIT:
            status = False
            
        #check whether user press any key
        if event.type== pygame.KEYDOWN:
            #check whether which key is pressed
            if event.key==pygame.K_LEFT:
                playerX_change = -change_val
            if event.key==pygame.K_RIGHT:
                playerX_change=change_val
        #check whether pressed key is removed
        if event.type==pygame.KEYUP:
            playerX_change=0
    
    #PLAYER
            
    
    #change the position of player
    playerX=playerX+playerX_change

    #if player touches the boundary
    if playerX>755:
        playerX=0
    if playerX<-5:
        playerX=755
    #initializing position of player
    player(playerX,playerY)


     #ENEMY

    #changing position of enemy
    enemyX=enemyX+enemyX_change

    #whwn enemy touches right boundary
    if enemyX>=745:
        enemyX_change=-change_val
        enemyX=745

    #when enemy touches the left boundry
    if enemyX<0:
        enemyX=0
        enemyX_change=change_val
        enemyY+=50 #enemy comes near to our player (position downward)

    #initialize position of enemy
    enemy(enemyX,enemyY)


    pygame.display.update()

#exit the game if while loop ends            
pygame.quit()
