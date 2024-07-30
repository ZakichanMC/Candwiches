import pygame
import random
from Scripts import customerScript as cus
from Scripts import images as img
pygame.init()

SCREEN = pygame.display.set_mode((640, 360))
BACKSCREEN = pygame.Surface((640, 360))

pygame.display.set_caption("Candwiches")
clock = pygame.time.Clock()

pygame.mixer.music.load('Assets/Sounds/titletheme.wav')
pygame.mixer.music.play(-1)


CUSTOMEREVENT = pygame.USEREVENT + 0
FINISHEVENT = pygame.USEREVENT + 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

gameState = "title"
orderFinished = False
isCustomer = False
customerOnScreen = False
whichCustomer = None
tutorialDone = False

isClicking = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            isClicking = True
        if event.type == pygame.MOUSEBUTTONUP:
            isClicking = False

        if gameState == "title" and isClicking and cus.startRect.collidepoint(pygame.mouse.get_pos()):
            pygame.mixer.music.load('Assets/Sounds/maintheme.wav')
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
            gameState = "shop" 


        if gameState == "shop":
            if not cus.isCustomer and not cus.orderFinished:
                pygame.time.set_timer(CUSTOMEREVENT, 1000)

            if event.type == CUSTOMEREVENT:
                if not cus.isCustomer:
                    cus.spawn_customer()  # isCustomer == True
                    cus.chooseOrder(SCREEN)

        elif gameState == "back":
            pygame.time.set_timer(CUSTOMEREVENT, 0)

        if event.type == pygame.MOUSEBUTTONDOWN and cus.isCustomer:
            if cus.acceptRect.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.Sound.play(img.chaching)
                cus.totalMoney += cus.price
                if not tutorialDone:
                    gameState = "tutorial"
                else:
                    gameState = "back"
            if cus.declineRect.collidepoint(pygame.mouse.get_pos()):
                cus.isCustomer = False
                pygame.time.set_timer(CUSTOMEREVENT, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and gameState == "tutorial":
            gameState = "back"
            tutorialDone = True

        if event.type == pygame.MOUSEBUTTONDOWN and cus.finishRect.collidepoint(pygame.mouse.get_pos()) and gameState == "back":
            thanksText = cus.chooseTipText(cus.checkOrderFulfilled())
            cus.isCan, cus.isBread1, cus.isBread2, cus.isFilling, cus.needsCooked, cus.isCooked, cus.isWrap, cus.isBag, cus.currentFilling, cus.currentWrap = False, False, False, False, False, False, False, False, None, None
            gameState = "shop"
            cus.orderFinished = True
            pygame.time.set_timer(FINISHEVENT, 1000)  # Customer leaves after 1 second

        if cus.orderFinished and event.type == FINISHEVENT:
            cus.orderFinished = False
            cus.isCustomer = False
            pygame.time.set_timer(CUSTOMEREVENT, 1000)

        # Toggle fullscreen mode
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()

    BACKSCREEN.blit(img.backdraw, (0, 0))
    BACKSCREEN.blit(img.guidraw, (0, 0))

    if gameState == "title":
        SCREEN.blit(img.title, (0, 0))
        version = pygame.font.Font('Assets/myfont.ttf', 17).render("Alpha 0.1.0", False, WHITE)
        SCREEN.blit(version, (640 - version.get_width() - 2, 360 - version.get_height() - 2))

    if gameState == "shop":
        SCREEN.blit(img.shopdraw, (0, 0))
    if cus.isCustomer:
        cus.spritesList.draw(SCREEN)
        SCREEN.blit(img.bubbleImg, (cus.bubbleX, cus.bubbleY))
        if not cus.orderFinished:
            for i in range(len(cus.order)):
                SCREEN.blit(cus.order[i][0], (cus.order[i][1], cus.order[i][2]))
                text = pygame.font.Font('Assets/myfont.ttf', 15).render(cus.order[i][3], False, BLACK)
                SCREEN.blit(text, (cus.order[i][4], cus.order[i][5]))
        else:
            cus.drawTipText(SCREEN, thanksText)

    if gameState == "tutorial":
        SCREEN.blit(img.tutorial, (0,0))
        cus.tutorialText(SCREEN)
    if gameState == "back":  # when you're in the back
        SCREEN.blit(BACKSCREEN, (0, 0))
        for i in range(len(cus.ingrRectList)):
            if cus.ingrRectList[i][1][3] != None:
                SCREEN.blit(cus.ingrRectList[i][1][2], cus.ingrRectList[i][0])
        cus.assemble(pygame.mouse.get_pos(), isClicking)
        cus.drawAssemble(SCREEN)
        cus.remindOrder(pygame.mouse.get_pos(), SCREEN, isClicking)
        cus.displayMoney(SCREEN)
        

    pygame.display.update()
    clock.tick(30)
