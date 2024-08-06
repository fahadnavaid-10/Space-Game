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

#fix change value
player_change_val=1
enemy_change_val=0.4

#enemy images
def load_enemy_image():
    enemy_file = 'enemy' + str(random.randint(1, 4)) + '.png'
    return pygame.image.load(enemy_file)

#multiple enemies
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
total_enemies=5

for i in range(total_enemies):
    enemyimg.append(load_enemy_image())
    enemyX.append(random.randint(0,745))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(enemy_change_val)
    enemyY_change.append(10)

#Bullet
bulletimg=pygame.image.load('bullet.png')
bulletX=400
bulletY=400
bulletY_change=1.5
bullet_state='off'

#score
score_val=0
font = pygame.font.Font('freesansbold.ttf', 30)

textX = 340
testY = 10


def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y ,i):
    screen.blit(enemyimg[i], (x,y))

def bullet(x,y):
    global bullet_state
    bullet_state='on'
    screen.blit(bulletimg , (x+10 , y+10))

def distance_calculator(x1,y1,x2,y2):
    return (((x2-x1)**2+(y2-y1)**2)**0.5)

def show_score(x, y):
    score = font.render("Score: " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

    
    
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
                playerX_change = -player_change_val
            if event.key==pygame.K_RIGHT:
                playerX_change=player_change_val
            #checking whether space bar is pressed
            if event.key==pygame.K_SPACE:
                if bullet_state=='off':
                    bulletX=playerX
                    bullet(bulletX,bulletY)
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
    for i in range(total_enemies):

        #changing position of enemy
        enemyX[i]=enemyX[i]+enemyX_change[i]

        #whwn enemy touches right boundary
        if enemyX[i]>=745:
            enemyX_change[i]=-enemy_change_val
            enemyX[i]=745

        #when enemy touches the left boundry
        if enemyX[i]<0:
            enemyX[i]=0
            enemyX_change[i]=enemy_change_val
            enemyY[i]+=50 #enemy comes near to our player (position downward)

        #initialize position of enemy
        enemy(enemyX[i],enemyY[i] , i)


        #calculare distance between bullet and enemy
        distance=distance_calculator(bulletX,bulletY,enemyX[i],enemyY[i])

         #COLLISION
        if distance<30:
            score_val+=1
            bullet_state='off'
            bulletY=400
            enemyX[i]=random.randint(0,745)
            enemyY[i]=random.randint(50,150)
            enemyimg[i] = load_enemy_image()  # Load a new enemy image after a hit

    
     #BULLET
    #bullet movement
    if bulletY<0:
        bulletY=400
        bullet_state='off'
    if bullet_state == 'on':
        bulletY-=bulletY_change
        bullet(bulletX,bulletY)

    

    
    show_score(textX, testY)
    pygame.display.update()


#exit the game if while loop ends            
pygame.quit()
