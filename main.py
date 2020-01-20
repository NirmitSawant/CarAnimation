import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 700))

# BackGround = Background('road.png',[0,0])
bg = pygame.image.load("road.v3.png")
pygame.display.set_caption("SMART STREET LIGHTS")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('car2.png')
playerX = 150
playerY = 636
playerY_change = 0

player2Img = pygame.image.load('car.png')
player2X = 550
player2Y = 50
player2Y_change = 0

Lbulb1Img = pygame.image.load('idea (1).png')
Lbulb1X = 320
Lbulb1Y = 500

Lbulb2Img = pygame.image.load('idea (1).png')
Lbulb2X = 320
Lbulb2Y = 400

Lbulb3Img = pygame.image.load('idea (1).png')
Lbulb3X = 320
Lbulb3Y = 300

Lbulb4Img = pygame.image.load('idea (1).png')
Lbulb4X = 320
Lbulb4Y = 200

Lbulb5Img = pygame.image.load('idea (1).png')
Lbulb5X = 320
Lbulb5Y = 100

Rbulb1Img = pygame.image.load('business-and-finance.png')
Rbulb1X = 450
Rbulb1Y = 100

Rbulb2Img = pygame.image.load('business-and-finance.png')
Rbulb2X = 450
Rbulb2Y = 200

Rbulb3Img = pygame.image.load('business-and-finance.png')
Rbulb3X = 450
Rbulb3Y = 300

Rbulb4Img = pygame.image.load('business-and-finance.png')
Rbulb4X = 450
Rbulb4Y = 400

Rbulb5Img = pygame.image.load('business-and-finance.png')
Rbulb5X = 450
Rbulb5Y = 500

def player(x, y):
    screen.blit(playerImg, (x, y))

def player2(x, y):
    screen.blit(player2Img, (x, y))

def Lbulb1(x,y):
    screen.blit(Lbulb1Img,(x,y))

def Lbulb2(x, y):
    screen.blit(Lbulb2Img,(x, y))

def Lbulb3(x, y):
    screen.blit(Lbulb3Img,(x, y))

def Lbulb4(x, y):
    screen.blit(Lbulb4Img,(x, y))

def Lbulb5(x, y):
    screen.blit(Lbulb5Img,(x, y))

def Rbulb1(x,y):
    screen.blit(Rbulb1Img,(x,y))

def Rbulb2(x, y):
    screen.blit(Rbulb2Img,(x, y))

def Rbulb3(x, y):
    screen.blit(Rbulb3Img,(x, y))

def Rbulb4(x, y):
    screen.blit(Rbulb4Img,(x, y))

def Rbulb5(x, y):
    screen.blit(Rbulb4Img,(x, y))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2Y_change = 9
            if event.key == pygame.K_DOWN:
                player2Y_change = -9
            if event.key == pygame.K_w:
                playerY_change = -9
            if event.key == pygame.K_s:
                playerY_change = 9

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2Y_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

    playerY += playerY_change
    player2Y += player2Y_change

    if 300 <= playerY <= 700:
        Lbulb1(Lbulb1X, Lbulb1Y)
    if 200 <= playerY <= 600:
        Lbulb2(Lbulb2X, Lbulb2Y)
    if 100 <= playerY <= 500:
        Lbulb3(Lbulb3X, Lbulb3Y)
    if 0 <= playerY <= 400:
        Lbulb4(Lbulb4X,Lbulb4Y)
    if 0 <= playerY <= 300:
        Lbulb5(Lbulb5X,Lbulb5Y)

    if 0 <= player2Y <= 300:
        Rbulb1(Rbulb1X, Rbulb1Y)
    if 0 <= player2Y <= 400:
        Rbulb2(Rbulb2X, Rbulb2Y)
    if 100 <= player2Y <= 500:
        Rbulb3(Rbulb3X, Rbulb3Y)
    if 200 <= player2Y <= 600:
        Rbulb4(Rbulb4X,Rbulb4Y)
    if 300 <= player2Y <= 700:
        Rbulb5(Rbulb5X,Rbulb5Y)

    if playerY<= 50:
        playerY = 50
    elif playerY >= 580:
        playerY = 580

    if player2Y <= 50:
        player2Y = 50
    elif player2Y >= 580:
        player2Y = 580

    player (playerX, playerY)
    player2(player2X,player2Y)

    pygame.display.update()