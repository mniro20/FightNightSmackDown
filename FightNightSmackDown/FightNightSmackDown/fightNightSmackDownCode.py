import pygame, sys
from pygame.locals import *
import random
from pygame.rect import RectType

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

WIDTH = 1300
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# actual images
backgroundImg = pygame.image.load('Background(start).png')
CSS = pygame.image.load('Character select Screen.png')
bg1 = pygame.image.load('bg1.gif')
bgDay = pygame.image.load('bgDay.gif')
bgNight = pygame.image.load('bgNight.gif')

startImg = pygame.image.load('start.png')
testconImg = pygame.image.load('tempconfirm.png')
blanktest = pygame.image.load('blank.png')

mikeImg = pygame.image.load('mike.png')
alexImg = pygame.image.load('Army Character.png')
marleyImg = pygame.image.load('lyberry.png')
gusImg = pygame.image.load('bird.png')
gianImg = pygame.image.load('bird.png')
edwinImg = pygame.image.load('bird.png')

int1Img = pygame.image.load('P1 movement.png')
int2Img = pygame.image.load('P2 movement.png')
bint1 = pygame.image.load('blank.png')
bint2 = pygame.image.load('blank.png')

char1 = pygame.image.load('blank.png')
char2 = pygame.image.load('blank.png')
char3 = pygame.image.load('blank.png')
char4 = pygame.image.load('blank.png')
char5 = pygame.image.load('blank.png')
char6 = pygame.image.load('blank.png')

# test images
testImg = pygame.image.load('bird.png')
testBg = pygame.image.load('testBg.jpg')
blank = pygame.image.load('blank.png')
blank1 = pygame.image.load('blank.png')

CSSrect = pygame.Rect(0, 0, 144, 256)
BgRect = pygame.Rect(200, 0, 144, 256)

startRect = pygame.Rect(552, 500, 195, 61)
readyRect = pygame.Rect(750 - 43, 440, 86, 23)
confirmRect = pygame.Rect(700 - 120, 440, 100, 38)

instructRect1 = pygame.Rect(200, 500, 86, 23)
instructRect2 = pygame.Rect(900, 500, 86, 23)

char1Rect = pygame.Rect(315, 145, 100, 85)
char2Rect = pygame.Rect(575, 145, 100, 80)
char3Rect = pygame.Rect(825, 145, 100, 90)
char4Rect = pygame.Rect(320, 320, 195, 61)
char5Rect = pygame.Rect(600, 320, 195, 61)
char6Rect = pygame.Rect(820, 330, 195, 61)

CSSChar1 = pygame.Rect(100, 500, 0, 0)
CSSChar2 = pygame.Rect(1100, 500, 0, 0)
blankchar1 = pygame.image.load('blank.png')
blankchar2 = pygame.image.load('blank.png')

Display = 1

red = (255, 0, 0)

images = []

char1directionX = 'none'
char1directionY = 'none'
char2directionX = 'none'
char2directionY = 'none'

for x in range(2):
    images.insert(0, pygame.image.load('ready' + str(x) + '.png'))

ready = 0

choice = 0

LEFT = 1
player1_health = 50
player2_health = 150
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

BgChoice = random.choice([0, 1, 2])


def health_bars(player1_health, player2_health):
    if player1_health > 200:
        player1_health_color = green
    elif player1_health > 100:
        player1_health_color = yellow
    else:
        player1_health_color = red

    if player2_health > 200:
        player2_health_color = green
    elif player2_health > 100:
        player2_health_color = yellow
    else:
        player2_health_color = red

    hb1 = pygame.draw.rect(screen, player1_health_color, (700, 25, player1_health, 75))
    hb2 = pygame.draw.rect(screen, player2_health_color, (100, 25, player2_health, 75))


# print(player1_health)
#  print(player2_health)

def intersects(rect1, rect2):
    if (rect1.right > rect2.left and rect1.left < rect2.right) and (
            rect1.top < rect2.bottom and rect1.bottom > rect2.top):
        return True
    return False


def directions(rect1, rect2):
    global Display
    global char1directionX
    global char1directionY
    global char2directionX
    global char2directionY
    if char1directionX == 'left':
        rect1.left = rect1.left - 10
    if char1directionX == 'right':
        rect1.right = rect1.right + 10
    if char1directionX == 'none':
        rect1.bottom = rect1.bottom + 0

    if char1directionY == 'up':
        rect1.top = rect1.top - 10
    if char1directionY == 'down':
        rect1.bottom = rect1.bottom + 10
    if char1directionX == 'none':
        rect1.bottom = rect1.bottom + 0

    if char2directionX == 'left':
        rect2.left = rect2.left - 10
    if char2directionX == 'right':
        rect2.right = rect2.right + 10
    if char2directionX == 'none':
        rect2.bottom = rect2.bottom + 0

    if char2directionY == 'up':
        rect2.top = rect2.top - 10
    if char2directionY == 'down':
        rect2.bottom = rect2.bottom + 10
    if char2directionY == 'none':
        rect2.bottom = rect2.bottom + 0


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def isOver1(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def isOver2(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


startButton = button((0, 255, 0), 552, 500, 195, 61, "start")
readyButton = button((0, 255, 0), 750 - 43, 440, 86, 23, "ready")
confirmButton = button((0, 255, 0), 700 - 120, 440, 100, 38, "ready")

CharSelBut1 = button((0, 255, 0), 315, 145, 100, 85, "ready")
CharSelBut2 = button((0, 255, 0), 575, 145, 100, 80, "ready")
CharSelBut3 = button((0, 255, 0), 825, 145, 100, 90, "ready")
CharSelBut4 = button((0, 255, 0), 320, 320, 195, 61, "ready")
CharSelBut5 = button((0, 255, 0), 600, 320, 195, 61, "ready")
CharSelBut6 = button((0, 255, 0), 820, 330, 195, 61, "ready")

# Game loop.
while True:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, BgRect)

    screen.blit(startImg, startRect)
    screen.blit(blanktest, confirmRect)

    screen.blit(char1, char1Rect)
    screen.blit(char2, char2Rect)
    screen.blit(char3, char3Rect)
    screen.blit(char4, char4Rect)
    screen.blit(char5, char5Rect)
    screen.blit(char6, char6Rect)
    screen.blit(bint1, instructRect1)
    screen.blit(bint2, instructRect2)

    screen.blit(blankchar1, CSSChar1)
    screen.blit(blankchar2, CSSChar2)

    directions(CSSChar2, CSSChar1)

    if BgChoice == 0 and Display == 3:
        backgroundImg = bg1
    if BgChoice == 1 and Display == 3:
        backgroundImg = bgDay
    if BgChoice == 2 and Display == 3:
        backgroundImg = bgNight

    if CSSChar1.left < 0:
        CSSChar1.left = 1
    if CSSChar1.right > 1200:
        CSSChar1.right = 1199

    if CSSChar2.left < 0:
        CSSChar2.left = 1
    if CSSChar2.right > 1200:
        CSSChar2.right = 1199

    if (Display == 2):
        (screen.blit(images[ready], readyRect))

    pos = pygame.mouse.get_pos()

    ready = ready + 1
    if (Display == 3):
        health_bars(player1_health, player2_health)

    if intersects(CSSChar2, CSSChar1):
        player2_health = player2_health - 100
        player1_health = player1_health - 100
        print(player2_health)
        print(player1_health)

    if ready >= len(images):
        ready = 0

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.isOver1(pos):
                startImg = blank
                Display = 2
                backgroundImg = CSS
                char1 = mikeImg
                char2 = alexImg
                char3 = marleyImg
                char4 = gusImg
                char5 = gianImg
                char6 = edwinImg
                bint1 = int1Img
                bint2 = int2Img
                blanktest = testconImg
                fps = 5
            if (confirmButton.isOver2(pos)):
                choice = 1

            if (CharSelBut1.isOver2(pos)) and (choice == 0):
                blankchar1 = mikeImg

            elif CharSelBut1.isOver2(pos) and (choice == 1):
                blankchar2 = mikeImg

            if CharSelBut2.isOver2(pos) and (choice == 0):
                blankchar1 = alexImg

            elif CharSelBut2.isOver2(pos) and (choice == 1):
                blankchar2 = alexImg

            if CharSelBut3.isOver2(pos) and (choice == 0):
                blankchar1 = marleyImg

            elif CharSelBut3.isOver2(pos) and (choice == 1):
                blankchar2 = marleyImg

            if CharSelBut4.isOver2(pos) and (choice == 0):
                blankchar1 = gusImg

            elif CharSelBut4.isOver2(pos) and (choice == 1):
                blankchar2 = gusImg

            if CharSelBut5.isOver2(pos) and (choice == 0):
                blankchar1 = gianImg

            elif CharSelBut5.isOver2(pos) and (choice == 1):
                blankchar2 = gianImg

            if CharSelBut6.isOver2(pos) and (choice == 0):
                blankchar1 = edwinImg

            elif CharSelBut6.isOver2(pos) and (choice == 1):
                blankchar2 = edwinImg

            if (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == mikeImg) and (blankchar2 == mikeImg)):
                backgroundImg = testBg
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == mikeImg) and (blankchar2 == alexImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == mikeImg) and (blankchar2 == marleyImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == mikeImg) and (blankchar2 == gusImg)):
                backgroundImg = testBg
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == mikeImg) and (blankchar2 == gianImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == mikeImg) and (blankchar2 == edwinImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == alexImg) and (blankchar2 == mikeImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == alexImg) and (blankchar2 == alexImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == alexImg) and (blankchar2 == marleyImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == alexImg) and (blankchar2 == gusImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == alexImg) and (blankchar2 == gianImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == alexImg) and (blankchar2 == edwinImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == marleyImg) and (blankchar2 == mikeImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == marleyImg) and (blankchar2 == alexImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == marleyImg) and (blankchar2 == marleyImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == marleyImg) and (blankchar2 == gusImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == marleyImg) and (blankchar2 == gianImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == marleyImg) and (blankchar2 == edwinImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == gusImg) and (blankchar2 == mikeImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == gusImg) and (blankchar2 == alexImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == gusImg) and (blankchar2 == marleyImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == gusImg) and (blankchar2 == gusImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == gusImg) and (blankchar2 == gianImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == gusImg) and (blankchar2 == edwinImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == gianImg) and (blankchar2 == mikeImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == gianImg) and (blankchar2 == alexImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == gianImg) and (blankchar2 == marleyImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == gianImg) and (blankchar2 == gusImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == gianImg) and (blankchar2 == gianImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == gianImg) and (blankchar2 == edwinImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == edwinImg) and (blankchar2 == mikeImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == edwinImg) and (blankchar2 == alexImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == edwinImg) and (blankchar2 == marleyImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and ((blankchar1 == edwinImg) and (blankchar2 == gusImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == edwinImg) and (blankchar2 == gianImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

            elif (readyButton.isOver1(pos)) and (choice == 1) and (
                    (blankchar1 == edwinImg) and (blankchar2 == edwinImg)):
                char1 = blank
                char2 = blank
                char3 = blank
                char4 = blank
                char5 = blank
                char6 = blank
                bint1 = blank
                bint2 = blank
                Display = 3
                blanktest = blank

        if (Display == 3):
            fps = 30
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    char1directionX = 'left'
                if event.key == pygame.K_RIGHT:
                    char1directionX = 'right'
                if event.key == pygame.K_UP:
                    char1directionX = 'up'
                if event.key == pygame.K_DOWN:
                    char1directionX = 'down'

                if event.key == pygame.K_a:
                    char2directionX = 'left'
                if event.key == pygame.K_d:
                    char2directionX = 'right'
                if event.key == pygame.K_w:
                    char2directionX = 'up'
                if event.key == pygame.K_s:
                    char2directionX = 'down'

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    char1directionY = 'none'
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    char1directionX = 'none'
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    char2directionY = 'none'
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    char2directionX = 'none'

    pygame.display.update()
    fpsClock.tick(fps)
