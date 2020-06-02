import random
import pygame
import sys
from pygame.locals import *
from pygame.rect import RectType
from pygame import mixer

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

WIDTH = 1300
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
P1 = 1
P2 = 1
# actual images
backgroundImg = pygame.image.load('Background(start).png')
CSS = pygame.image.load('Character select Screen.png')
bg1 = pygame.image.load('bg1.png')
bgDay = pygame.image.load('bgDay.png')
bgNight = pygame.image.load('bgNight.png')

Endgame1 = pygame.image.load('Player1W.png')
Endgame2 = pygame.image.load('Player2W.png')

startImg = pygame.image.load('start.png')
testconImg = pygame.image.load('tempconfirm.png')
blanktest = pygame.image.load('blank.png')

mikeImg = pygame.image.load('Playerhead.png')
alexImg = pygame.image.load('Soldierhead.png')
marleyImg = pygame.image.load('libaryhead.png')
gusImg = pygame.image.load('Pinkhead.png')
gianImg = pygame.image.load('ithead.png')
edwinImg = pygame.image.load('ehead.png')

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
testBg = pygame.image.load('testBg.jpg')
blank = pygame.image.load('blank.png')
blank1 = pygame.image.load('blank.png')

eImg = pygame.image.load('E2.png')
epunchImg = pygame.image.load('Epunch2.png')
ekickImg = pygame.image.load('Ekick2.png')

PinkImg = pygame.image.load('Pink2.png')
PinkpunchImg = pygame.image.load('Pinkpunch2.png')
PinkkickImg = pygame.image.load('Pinkkick2.png')

libaryImg = pygame.image.load('libary2.png')
libarypunchImg = pygame.image.load('libarypunch2.png')
libarykickImg = pygame.image.load('libarykick2.png')

SoldierImg = pygame.image.load('Soldier2.png')
SoldierpunchImg = pygame.image.load('Soldierpunch2.png')
SoldierkickImg = pygame.image.load('Soldierkick2.png')

PlayerImg = pygame.image.load('Player2.png')
PlayerpunchImg = pygame.image.load('Playerpunch2.png')
PlayerkickImg = pygame.image.load('Playerkick2.png')

ItImg = pygame.image.load('it2.png')
ItpunchImg = pygame.image.load('itpunch2.png')
ItkickImg = pygame.image.load('itkick2.png')

eImg2 = pygame.image.load('E.png')
epunchImg2 = pygame.image.load('Epunch.png')
ekickImg2 = pygame.image.load('Ekick.png')

PinkImg2 = pygame.image.load('Pink.png')
PinkpunchImg2 = pygame.image.load('Pinkpunch.png')
PinkkickImg2 = pygame.image.load('Pinkkick.png')

libaryImg2 = pygame.image.load('libary.png')
libarypunchImg2 = pygame.image.load('libarypunch.png')
libarykickImg2 = pygame.image.load('libarykick.png')

SoldierImg2 = pygame.image.load('Soldier.png')
SoldierpunchImg2 = pygame.image.load('Soldierpunch.png')
SoldierkickImg2 = pygame.image.load('Soldierkick.png')

PlayerImg2 = pygame.image.load('Player.png')
PlayerpunchImg2 = pygame.image.load('Playerpunch.png')
PlayerkickImg2 = pygame.image.load('Playerkick.png')

ItImg2 = pygame.image.load('it.png')
ItpunchImg2 = pygame.image.load('itpunch.png')
ItkickImg2 = pygame.image.load('itkick.png')
# Sound effect
Punch = pygame.mixer.Sound('Punch.wav')
Rolecredits = pygame.mixer.Sound('rolecredits.wav')
mixer.music.load('Fighttime.wav')

mixer.music.play(-1)

Charrect1 = pygame.Rect(0, 20, 336, 393)
Charect2 = pygame.Rect(1100, 500, 336, 393)

CSSrect = pygame.Rect(0, 0, 144, 256)
BgRect = pygame.Rect(200, 0, 144, 256)
BGRect = pygame.Rect(0, 0, 0, 0)
endRect = pygame.Rect(0, 0, 1300, 1300)

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

CSSChar1 = pygame.Rect(100, 450, 85, 200)
CSSChar2 = pygame.Rect(1100, 450, 85, 200)
blankchar1 = pygame.image.load('blank.png')
blankchar2 = pygame.image.load('blank.png')

Display = 1

sound = 1

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
player1_health = 300
player2_health = 300
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

BgChoice = random.choice([0, 1, 2])


def intersects(rect1, rect2):
    if (rect1.right > rect2.left and rect1.left < rect2.right) and (
            rect1.top < rect2.bottom and rect1.bottom > rect2.top):
        return True
    return False


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


def endgame(player1_health, player2_health):
    global Display
    if player1_health <= 0:
        screen.fill((0, 0, 0))
        Display = 4

    if player2_health <= 0:
        screen.fill((0, 0, 0))
        Display = 5


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
    if char1directionY == 'none':
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


def reset():
    global Display
    global player1_health
    global player2_health
    global choice
    global blankchar1
    global blankchar2
    global CSSChar1
    global CSSChar2
    global P1
    global P2
    global BgChoice
    global BgRect
    Display = 2
    CSSChar1 = pygame.Rect(100, 450, 85, 200)
    CSSChar2 = pygame.Rect(1100, 450, 85, 200)
    BgRect = pygame.Rect(200, 0, 144, 256)
    BgChoice = random.choice([0, 1, 2])
    P1 = 1
    P2 = 1
    choice = 0
    player1_health = 300
    player2_health = 300
    pygame.mixer.music.play(-1)
    blankchar1 = blank
    blankchar2 = blank
    Rolecredits.stop()


def pause():
    global sound
    if sound == 1:
        pygame.mixer.music.unpause()
    elif sound == 0:
        pygame.mixer.music.pause()


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def isOver1(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False

    def isOver2(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
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
    intersects(CSSChar1, CSSChar2)

    if BgChoice == 0 and Display == 3:
        backgroundImg = bg1
        BgRect = pygame.Rect(0, 0, 144, 256)
    if BgChoice == 1 and Display == 3:
        backgroundImg = bgDay
        BgRect = pygame.Rect(0, 0, 144, 256)
    if BgChoice == 2 and Display == 3:
        backgroundImg = bgNight
        BgRect = pygame.Rect(0, 0, 144, 256)

    if CSSChar1.left < 0:
        CSSChar1.left = 1
    if CSSChar1.right > 1200:
        CSSChar1.right = 1199
    if CSSChar1.bottom > 650:
        CSSChar1.bottom = 649
    if CSSChar1.top < 0:
        CSSChar1.top = 1

    if CSSChar2.left < 0:
        CSSChar2.left = 1
    if CSSChar2.right > 1200:
        CSSChar2.right = 1199
    if CSSChar2.bottom > 650:
        CSSChar2.bottom = 649
    if CSSChar2.top < 0:
        CSSChar2.top = 1

    if Display == 2:
        fps = 5
        startImg = blank
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
        (screen.blit(images[ready], readyRect))
    pos = pygame.mouse.get_pos()
    ready = ready + 1

    if Display == 3:
        health_bars(player1_health, player2_health)
        endgame(player1_health, player2_health)

    if ready >= len(images):
        ready = 0

    if Display == 4:
        pygame.mixer.music.stop()
        screen.blit(Endgame1, endRect)
        if sound == 1:
            Rolecredits.play()
    if Display == 5:
        pygame.mixer.music.stop()
        screen.blit(Endgame2, endRect)
        if sound == 1:
            Rolecredits.play()

    if ready >= len(images):
        ready = 0

    # Player 1 controls
    if P1 == 1:
        if blankchar1 == epunchImg or blankchar1 == ekickImg:
            blankchar1 = eImg
            if sound == 1:
                Punch.play()
        if blankchar1 == PinkpunchImg or blankchar1 == PinkkickImg:
            blankchar1 = PinkImg
            if sound == 1:
                Punch.play()
        if blankchar1 == libarykickImg or blankchar1 == libarypunchImg:
            blankchar1 = libaryImg
            if sound == 1:
                Punch.play()
        if blankchar1 == SoldierpunchImg or blankchar1 == SoldierkickImg:
            blankchar1 = SoldierImg
            if sound == 1:
                Punch.play()
        if blankchar1 == PlayerpunchImg or blankchar1 == PlayerkickImg:
            blankchar1 = PlayerImg
            if sound == 1:
                Punch.play()
        if blankchar1 == ItpunchImg or blankchar1 == ItkickImg:
            blankchar1 = ItImg
            if sound == 1:
                Punch.play()

    if P1 == 2:
        if blankchar1 == eImg:
            blankchar1 = epunchImg
            if sound == 1:
                Punch.play()
        if blankchar1 == PinkImg:
            blankchar1 = PinkpunchImg
            if sound == 1:
                Punch.play()

        if blankchar1 == libaryImg:
            blankchar1 = libarypunchImg
            if sound == 1:
                Punch.play()

        if blankchar1 == SoldierImg:
            blankchar1 = SoldierpunchImg
            if sound == 1:
                Punch.play()

        if blankchar1 == PlayerImg:
            blankchar1 = PlayerpunchImg
            if sound == 1:
                Punch.play()

        if blankchar1 == ItImg:
            blankchar1 = ItpunchImg
            if sound == 1:
                Punch.play()

    if P1 == 3:
        if blankchar1 == eImg:
            blankchar1 = ekickImg
            if sound == 1:
                Punch.play()

        if blankchar1 == PinkImg:
            blankchar1 = PinkkickImg
            if sound == 1:
                Punch.play()

        if blankchar1 == libaryImg:
            blankchar1 = libarykickImg
            if sound == 1:
                Punch.play()

        if blankchar1 == SoldierImg:
            blankchar1 = SoldierkickImg
            if sound == 1:
                Punch.play()

        if blankchar1 == PlayerImg:
            blankchar1 = PlayerkickImg
            if sound == 1:
                Punch.play()

        if blankchar1 == ItImg:
            blankchar1 = ItkickImg
            if sound == 1:
                Punch.play()

    # Player 2 controls
    if P2 == 1:
        if blankchar2 == epunchImg2 or blankchar2 == ekickImg2:
            blankchar2 = eImg2
            if sound == 1:
                Punch.play()
        if blankchar2 == PinkpunchImg2 or blankchar2 == PinkkickImg2:
            blankchar2 = PinkImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == libarykickImg2 or blankchar2 == libarypunchImg2:
            blankchar2 = libaryImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == SoldierpunchImg2 or blankchar2 == SoldierkickImg2:
            blankchar2 = SoldierImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == PlayerpunchImg2 or blankchar2 == PlayerkickImg2:
            blankchar2 = PlayerImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == ItpunchImg2 or blankchar2 == ItkickImg2:
            blankchar2 = ItImg2
            if sound == 1:
                Punch.play()

    if P2 == 2:
        if blankchar2 == eImg2:
            blankchar2 = epunchImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == PinkImg2:
            blankchar2 = PinkpunchImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == libaryImg2:
            blankchar2 = libarypunchImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == SoldierImg2:
            blankchar2 = SoldierpunchImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == PlayerImg2:
            blankchar2 = PlayerpunchImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == ItImg2:
            blankchar2 = ItpunchImg2
            if sound == 1:
                Punch.play()

    if P2 == 3:
        if blankchar2 == eImg2:
            blankchar2 = ekickImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == PinkImg2:
            blankchar2 = PinkkickImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == libaryImg2:
            blankchar2 = libarykickImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == SoldierImg2:
            blankchar2 = SoldierkickImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == PlayerImg2:
            blankchar2 = PlayerkickImg2
            if sound == 1:
                Punch.play()

        if blankchar2 == ItImg2:
            blankchar2 = ItkickImg2
            if sound == 1:
                Punch.play()

    if intersects(CSSChar1, CSSChar2) and P1 == 2 or intersects(CSSChar1, CSSChar2) and P1 == 3:
        player1_health = player1_health - 5
    if intersects(CSSChar1, CSSChar2) and P2 == 3 or intersects(CSSChar1, CSSChar2) and P2 == 2:
        player2_health = player2_health - 5

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.isOver1(pos):
                Display = 2
                fps = 5

            if confirmButton.isOver2(pos):
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

        if Display == 3:
            fps = 30
            if blankchar1 == edwinImg:
                blankchar1 = eImg
            if blankchar1 == gianImg:
                blankchar1 = ItImg
            if blankchar1 == gusImg:
                blankchar1 = PinkImg
            if blankchar1 == marleyImg:
                blankchar1 = libaryImg
            if blankchar1 == alexImg:
                blankchar1 = SoldierImg
            if blankchar1 == mikeImg:
                blankchar1 = PlayerImg

            if blankchar2 == edwinImg:
                blankchar2 = eImg2
            if blankchar2 == gianImg:
                blankchar2 = ItImg2
            if blankchar2 == gusImg:
                blankchar2 = PinkImg2
            if blankchar2 == marleyImg:
                blankchar2 = libaryImg2
            if blankchar2 == alexImg:
                blankchar2 = SoldierImg2
            if blankchar2 == mikeImg:
                blankchar2 = PlayerImg2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                char1directionX = 'left'
            if event.key == pygame.K_RIGHT:
                char1directionX = 'right'
            if event.key == pygame.K_UP:
                char1directionY = 'up'
            if event.key == pygame.K_DOWN:
                char1directionY = 'down'

            if event.key == pygame.K_a:
                char2directionX = 'left'
            if event.key == pygame.K_d:
                char2directionX = 'right'
            if event.key == pygame.K_w:
                char2directionY = 'up'
            if event.key == pygame.K_s:
                char2directionY = 'down'
            if event.key == pygame.K_p:
                if sound == 1:
                    sound = 0
                elif sound == 0:
                    sound = 1
                pause()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                char1directionY = 'down'
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                char1directionX = 'none'
            if event.key == pygame.K_w or event.key == pygame.K_s:
                char2directionY = 'down'
            if event.key == pygame.K_a or event.key == pygame.K_d:
                char2directionX = 'none'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if Display == 4:
                    reset()
                if Display == 5:
                    reset()
        if event.type == pygame.KEYDOWN and Display == 3:
            if event.key == pygame.K_q:
                P1 = 2

            if event.key == pygame.K_e:
                P1 = 3

            # player 2 action
            if event.key == pygame.K_m:
                P2 = 2

            if event.key == pygame.K_b:
                P2 = 3


        if event.type == pygame.KEYUP and Display == 3:
            # player 1 reset
            if event.key == pygame.K_q:
                P1 = 1
            if event.key == pygame.K_e:
                P1 = 1
            # player 2 reset
            if event.key == pygame.K_m:
                P2 = 1
            if event.key == pygame.K_b:
                P2 = 1

    pygame.display.update()
    fpsClock.tick(fps)