import pygame 
import time

size=(720,540)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
gray=(139,139,120)
darkgray=(48,48,48)
lightgray=(164,164,164)
skyblue=(142,229,238)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,230,0)
PURPLE = (255,0,255)
SKIN = (255,228,181)
xpos=10
ypos=10
movingLeft=False
movingRight=False
movingUp=False
movingDown=False
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hello World!")
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()
		if event.type==pygame.KEYDOWN and event.key==pygame.K_w:
			movingUp=True
		if event.type==pygame.KEYUP and event.key==pygame.K_w:
			movingUp=False
		if event.type==pygame.KEYDOWN and event.key==pygame.K_s:
			movingDown=True
		if event.type==pygame.KEYUP and event.key==pygame.K_s:
			movingDown=False

		if event.type==pygame.KEYDOWN and event.key==pygame.K_d:
			movingRight=True
		if event.type==pygame.KEYUP and event.key==pygame.K_d:
			movingRight=False
	
		if event.type==pygame.KEYDOWN and event.key==pygame.K_a:
			movingLeft=True
		if event.type==pygame.KEYUP and event.key==pygame.K_a:
			movingLeft=False

	if movingUp:
		ypos -=25
	if movingDown:
		ypos +=25
	if movingRight:
		xpos +=25
	if movingLeft:
		xpos -=25
	screen.fill(skyblue)
	building7=pygame.Rect(100,200,70,340)
	pygame.draw.rect(screen,lightgray,building7)
	building2=pygame.Rect(150,100,150,440)
	pygame.draw.rect(screen,darkgray,building2)
	building1=pygame.Rect(0,300,100,240)
	pygame.draw.rect(screen,gray,building1)
	building3=pygame.Rect(225,175,120,415)
	pygame.draw.rect(screen,gray,building3)
	building5=pygame.Rect(450,170,125,370)
	pygame.draw.rect(screen,darkgray,building5)
	building4=pygame.Rect(355,150,100,390)
	pygame.draw.rect(screen,lightgray,building4)
	building6=pygame.Rect(500,250,200,290)
	pygame.draw.rect(screen,lightgray,building6)
	grass=pygame.Rect(0,470,720,70)
	pygame.draw.rect(screen,green,grass)
	player = pygame.Rect(xpos,ypos,40,20)
	pygame.draw.rect(screen,BLUE,player)
	cape = pygame.Rect(xpos-10,ypos-2,50,5)
	pygame.draw.rect(screen,RED,cape)
	legs = pygame.Rect(xpos-20,ypos+5,20,10)
	pygame.draw.rect(screen,BLUE,legs)
	shoes = pygame.Rect(xpos-30,ypos+5,10,10)
	pygame.draw.rect(screen,RED,shoes)
	belt = pygame.Rect(xpos+10,ypos,5,20)
	pygame.draw.rect(screen,YELLOW,belt)

	hand = pygame.Rect(xpos+10,ypos,10,10)
	pygame.draw.ellipse(screen,SKIN,hand)
	arm = pygame.Rect(xpos+40,ypos+5,20,5)
	pygame.draw.rect(screen,BLUE,arm)
	otherhand = pygame.Rect(xpos+55,ypos+3,10,10)
	pygame.draw.ellipse(screen,SKIN,otherhand)
	hair = pygame.Rect(xpos+33,ypos-4,20,10)
	pygame.draw.rect(screen,BLACK,hair)
	head = pygame.Rect(xpos+33,ypos-3,20,20)
	pygame.draw.ellipse(screen,SKIN,head)
	bangs = pygame.Rect(xpos+33,ypos-9,20,10)
	pygame.draw.rect(screen,BLACK,bangs)



	pygame.display.flip()
	pygame.display.flip()
	time.sleep(1/45)
