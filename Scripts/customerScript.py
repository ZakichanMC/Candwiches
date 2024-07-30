import pygame, random, os, sys 
from Scripts import images as img
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir) 

pygame.init()
BLACK = (0, 0, 0)

cusX, cusY, cusW, cusH = 149, 57, img.matt.get_width(), img.matt.get_height()

class Customer(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.x, self.y = cusX, cusY
        self.rect.x, self.rect.y = self.x, self.y

isCustomer = False
customerTimer = 0
orderFinished = False
whichOrder, whichCustomer = None, None

customer1 = Customer(img.matt)
customer2 = Customer(img.fray)
customer3 = Customer(img.zach)
customer4 = Customer(img.dom)
customer5 = Customer(img.jason)
customer6 = Customer(img.zane)
customerList = [customer1, customer2, customer3, customer4, customer5, customer6]
spritesList = pygame.sprite.Group()

def spawn_customer():
    global isCustomer, whichCustomer, whichOrder
    isCustomer = True
    whichCustomer = random.choice(customerList)  # new random customer
    spritesList.empty()
    spritesList.add(whichCustomer)
    whichOrder = random.randint(0, 1)  # set the customer's order


bubbleX, bubbleY = 303 , 28
acceptRect = pygame.Rect(bubbleX + 244, bubbleY + 88, 35, 22)
declineRect = pygame.Rect(bubbleX + 198, bubbleY + 96, 26, 24)
textRect = pygame.Rect(bubbleX + 41, bubbleY + 20, 240, 65)

#all ingredients [image, needscooked, which ingrRect, filling img, wrap img, price]
pbj = [img.pbjImg, 0, img.pbjRect1, img.pbjFilling, img.pbjWrap, 3.99, 1.29]
chicken = [img.chickenImg, 1, img.chickenRect2, img.chickenFilling, img.chickenWrap, 5.99, 1.49]
phillycheese = [img.phillycheeseImg, 1, img.phillycheeseRect3, img.phillycheesefilling, img.phillycheeseWrap, 7.99, 1.59]
fourthIngr = [None, 0, None, None, None, 0.00, 0.00] #add something eventually
unlockedFlavorList = [pbj, chicken, phillycheese, fourthIngr]


whichFlavor = None
flavorX, flavorY, flavorW, flavorH = 0, 0, 59, 38
chosen = None
order = []
toMake = []
made = []
amountX, amountY = 0, 0
price = 0.00
tip = 0.00
totalMoney = 0.00


ingr1Rect = pygame.rect.Rect(22, 54, 87, 70)
ingr2Rect = pygame.rect.Rect(131, 54, 87, 70)
ingr3Rect = pygame.rect.Rect(240, 54, 87, 70)
ingr4Rect = pygame.rect.Rect(347, 54, 87, 70)  
#edit based on where they place stuff (save data)
ingrRectList = [[ingr1Rect, pbj], [ingr2Rect, chicken], [ingr3Rect, phillycheese], [ingr4Rect, fourthIngr]]

def chooseOrder(surface):
    global whichFlavor, flavorX, flavorY, flavorW, flavorH, chosen, order, toMake, amountX, amountY, price, tip, totalMoney
    order = []
    toMake = []
    price = 0.00
    tipPCList = random.choices([0.15, 0.20, 0.25], weights=[10, 1, 1])
    tipPC = tipPCList[0]
    tip = 0.00
    def getChosen(ingrRectList):
        global chosen
        chosen = random.sample([ingrRectList[0][1], ingrRectList[1][1], ingrRectList[2][1], ingrRectList[3][1]], random.randint(1, 3))
        chosen = [i for i in chosen if i and None not in i]
        if not chosen:
            getChosen(ingrRectList)
    getChosen(ingrRectList)
    for i in range(len(chosen)):
        flavorX, flavorY = bubbleX + 46 + i * 70, bubbleY + 19
        whichFlavor = chosen[i][0]
        surface.blit(whichFlavor, (flavorX, flavorY))

        amount = random.randint(1, 2)  # how many of each they want
        amountX, amountY = flavorX + flavorW, flavorY + flavorH - 10
        order.append([whichFlavor, flavorX, flavorY, str(amount), amountX, amountY])
        for j in range(amount):
            toMake.append(whichFlavor)  # list of every can you need to make
            price += chosen[i][5]
    tip = price * tipPC

    


breadRect = pygame.rect.Rect(22, 153, 87, 70)
board1Rect = pygame.rect.Rect(158, 138, 133, 67)
board2Rect = pygame.rect.Rect(296, 138, 133, 67)
board3Rect = pygame.rect.Rect(435, 138, 133, 67)
canBoxRect = pygame.rect.Rect(6, 269, 102, 91)
wrapBoxRect = pygame.rect.Rect(544, 304, 96, 56)
microwaveRect = pygame.rect.Rect(457, 81, 98, 28)
bagRect = pygame.rect.Rect(581, 77, 39, 79)
finishRect = pygame.rect.Rect(587, 185, 42, 47)

assemblyRect = pygame.rect.Rect(200, 146, 53, 43)
wrapRect = pygame.rect.Rect(476, 147, 53, 43)

isCan, isBread1, isFilling, isBread2, needsCooked, isCooked, isWrap, isBag, currentFilling, currentWrap = False, False, False, False, False, False, False, False, None, None
cost = 0.00

def assemble(pos, isClicking):
    global toMake, made, cost, tip, totalMoney
    global isCan, isBread1, isFilling, isBread2, needsCooked, isCooked, isWrap, isBag, currentFilling, currentWrap
    cost = 0.00
    if not isBag:
        if not isWrap:
            if not isCooked:
                if not isBread2:
                    if not isFilling:
                        if not isBread1:
                            if not isCan:
                                if canBoxRect.collidepoint(pos) and isClicking:
                                    pygame.mixer.Sound.play(img.canSound)
                                    isCan = True
                            if breadRect.collidepoint(pos) and isClicking and isCan:
                                isBread1 = True

                        for j in range(len(ingrRectList)):
                                if ingrRectList[j][0].collidepoint(pos) and isClicking and isBread1:
                                    cost = ingrRectList[j][1][6]
                                    totalMoney -= cost
                                    if ingrRectList[j][1][0] in toMake:
                                        made.append(ingrRectList[j][1][0])
                                    if ingrRectList[j][1][1] == 1:
                                        needsCooked = True
                                    pygame.mixer.Sound.play(img.fillingSound)
                                    isFilling = True
                                    currentFilling = ingrRectList[j][1][3]
                                    currentWrap = ingrRectList[j][1][4]
                    if breadRect.collidepoint(pos) and isClicking and isFilling:
                        isBread2 = True
                if needsCooked:
                    if microwaveRect.collidepoint(pos) and isClicking and isBread2:
                        isCooked = True
                elif not needsCooked and isBread2:
                    isCooked = True
            if wrapBoxRect.collidepoint(pos) and isClicking and isCooked:
                pygame.mixer.Sound.play(img.wrapSound)
                isWrap = True
        if bagRect.collidepoint(pos) and isClicking and isWrap:
            pygame.mixer.Sound.play(img.bagSound)
            isBag = True
            isCan, isBread1, isBread2, isFilling, needsCooked, isCooked, isWrap, isBag, currentFilling, currentWrap = False, False, False, False, False, False, False, False, None, None
            
def checkOrderFulfilled():
    global toMake, made
    tempToMake = toMake.copy()
    tempMade = made.copy()

    for item in tempToMake:
        if item in tempMade:
            tempMade.remove(item)
        else:
            return False
    return True

def drawAssemble(surface):
    if isCan and not isCooked:
        surface.blit(img.isCan, assemblyRect)
    if isBread1 and not isCooked:
        surface.blit(img.isBread1, assemblyRect)
    if isFilling and not isCooked:
        surface.blit(currentFilling, assemblyRect)
    if isBread2 and not isCooked:
        surface.blit(img.isBread2, assemblyRect)
    if isCooked and not isBag:
        surface.blit(img.isCan, wrapRect)
        surface.blit(img.isCooked, wrapRect)
    if isWrap and not isBag:
        surface.blit(currentWrap, wrapRect)

remindRect = pygame.rect.Rect(42, 0, 37, 26)
escRemindRect = pygame.rect.Rect(430, 110, 44, 38)
isRemind = False
def remindOrder(pos, surface, isClicking):
    global remindRect, isRemind, order
    if remindRect.collidepoint(pos) and not isRemind and isClicking:
        isRemind = True
    if escRemindRect.collidepoint(pos) and isRemind and isClicking:
        isRemind = False

    if isRemind:
        surface.blit(img.remind, (180, 110))
        for i in range(len(order)):
            surface.blit(order[i][0], (order[i][1] - 140, order[i][2] + 100))
            text = pygame.font.Font('Assets/myfont.ttf', 15).render(order[i][3], False, BLACK)
            surface.blit(text, (order[i][4] - 140, order[i][5] + 100))

def chooseTipText(condition):
    global tip
    if condition:
        thanksList = ["Thanks!", "Thanks a lot!", "Thank you.", "Have a good one.", "Appreciate it."]
        thanksText = random.choice(thanksList)
        tip = round(tip, 2)
        pygame.mixer.Sound.play(img.tipSound)
    else:
        thanksList = ["You messed up my order!", "Moron!", "Screw you!", "I'm never coming back.", "How about do your job?", "Lazy piece of crap."]
        thanksText = random.choice(thanksList)
        tip = 0.00
    return thanksText

def drawTipText(surface, thanksText):
    global tip
    text = pygame.font.Font('Assets/myfont.ttf', 17).render(thanksText, False, BLACK)
    plus = pygame.font.Font('Assets/myfont.ttf', 17).render("+", False, BLACK)
    tipText = pygame.font.Font('Assets/myfont.ttf', 17).render(str(tip), False, BLACK)
    surface.blit(text, (bubbleX + 50, bubbleY + 25))
    if tip != 0.00:
        surface.blit(plus, (bubbleX + 50, bubbleY + 75))
        surface.blit(tipText, (bubbleX + 60, bubbleY + 75))

def tutorialText(surface):
    howTo = "How to make a Candwich:"
    optional = "(optional)"
    e = "\"E\""
    text = pygame.font.Font('Assets/myfont.ttf', 30).render(howTo, False, BLACK)
    surface.blit(text, (50, 40))
    text = pygame.font.Font('Assets/myfont.ttf', 20).render(optional, False, BLACK)
    surface.blit(text, (250, 262))
    text = pygame.font.Font('Assets/myfont.ttf', 30).render(e, False, BLACK)
    surface.blit(text, (520, 298))

def displayMoney(surface):
    global totalMoney
    text = pygame.font.Font('Assets/myfont.ttf', 25).render(str(round(totalMoney, 2)), False, BLACK)
    dollar = "$"
    dollarText = pygame.font.Font('Assets/myfont.ttf', 25).render(dollar, False, BLACK)
    surface.blit(dollarText, (200, 1))
    surface.blit(text, (200 + dollarText.get_width() + 10, 1))

startRect = pygame.rect.Rect(146, 272, 286, 77)