import pygame, os, sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir) 
pygame.init()

matt = pygame.image.load('Assets/Sprites/Customers/customer1.png')
fray = pygame.image.load('Assets/Sprites/Customers/customer2.png')
zach = pygame.image.load('Assets/Sprites/Customers/customer3.png')
dom = pygame.image.load('Assets/Sprites/Customers/customer4.png')
jason = pygame.image.load('Assets/Sprites/Customers/customer5.png')
zane = pygame.image.load('Assets/Sprites/Customers/customer6.png')

bubbleImg = pygame.image.load('Assets/Sprites/Customers/speechbubble.png')

pbjImg = pygame.image.load('Assets/Sprites/Flavors/pbj.png')
chickenImg = pygame.image.load('Assets/Sprites/Flavors/chicken.png')
phillycheeseImg = pygame.image.load('Assets/Sprites/Flavors/phillycheese.png')

shopdraw = pygame.image.load('Assets/Backgrounds/Shop.png')
tutorial = pygame.image.load('Assets/Backgrounds/Tutorial.png')
backdraw = pygame.image.load('Assets/Backgrounds/Back.png')
guidraw = pygame.image.load('Assets/Backgrounds/GUI.png')
title = pygame.image.load('Assets/Backgrounds/Title.png')

pbjRect1 = pygame.image.load('Assets/Sprites/Flavors/pbjrect1.png')
pbjRect2 = pygame.image.load('Assets/Sprites/Flavors/pbjrect2.png')
pbjRect3 = pygame.image.load('Assets/Sprites/Flavors/pbjrect3.png')
pbjRect4 = pygame.image.load('Assets/Sprites/Flavors/pbjrect4.png')
chickenRect1 = pygame.image.load('Assets/Sprites/Flavors/chickenrect1.png')
chickenRect2 = pygame.image.load('Assets/Sprites/Flavors/chickenrect2.png')
chickenRect3 = pygame.image.load('Assets/Sprites/Flavors/chickenrect3.png')
chickenRect4 = pygame.image.load('Assets/Sprites/Flavors/chickenrect4.png')
phillycheeseRect1 = pygame.image.load('Assets/Sprites/Flavors/phillycheeserect1.png')
phillycheeseRect2 = pygame.image.load('Assets/Sprites/Flavors/phillycheeserect2.png')
phillycheeseRect3 = pygame.image.load('Assets/Sprites/Flavors/phillycheeserect3.png')
phillycheeseRect4 = pygame.image.load('Assets/Sprites/Flavors/phillycheeserect4.png')

isCan = pygame.image.load('Assets/Sprites/Flavors/iscan.png')
isBread1 = pygame.image.load('Assets/Sprites/Flavors/isbread1.png')
isBread2 = pygame.image.load('Assets/Sprites/Flavors/isbread2.png')
pbjFilling = pygame.image.load('Assets/Sprites/Flavors/pbjisfilling.png')
chickenFilling = pygame.image.load('Assets/Sprites/Flavors/chickenisfilling.png')
phillycheesefilling = pygame.image.load('Assets/Sprites/Flavors/phillycheeseisfilling.png')
isCooked = pygame.image.load('Assets/Sprites/Flavors/iscooked.png')

pbjWrap = pygame.image.load('Assets/Sprites/Flavors/pbjwrap.png')
chickenWrap = pygame.image.load('Assets/Sprites/Flavors/chickenwrap.png')
phillycheeseWrap = pygame.image.load('Assets/Sprites/Flavors/phillycheesewrap.png')

remind = pygame.image.load('Assets/Sprites/Customers/remind.png')

chaching = pygame.mixer.Sound('Assets/Sounds/chaching.wav')
canSound = pygame.mixer.Sound('Assets/Sounds/iscan.wav')
fillingSound = pygame.mixer.Sound('Assets/Sounds/isfilling.wav')
wrapSound = pygame.mixer.Sound('Assets/Sounds/iswrap.wav')
bagSound = pygame.mixer.Sound('Assets/Sounds/isbag.wav')
tipSound = pygame.mixer.Sound('Assets/Sounds/tip.wav')