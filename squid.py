import pygame
import time
def wideclarinet(question):
	global xstretch
	global ystretch
	print (question)
	answer = input()
	if answer not in ["clarinet","Clarinet","CLARINET"]:
		xstretch*=4
		screen = pygame.display.set_mode(size)
		screen.fill(RED)
		pygame.display.flip()
		time.sleep(1/24)

def tallclarinet(question):
	global xstretch
	global ystretch
	print (question)
	answer = input()
	if answer not in ["clarinet","Clarinet","CLARINET"]:
		ystretch *= 4
		screen = pygame.display.set_mode(size)
		screen.fill(RED)
		pygame.display.flip()
		time.sleep(1/24)

size=(720,540)
white=(255,255,255)
black=(0,0,0)
TEAL=(193,255,193)
BLACK=(0,0,0)
WHITE=(255,255,255)
DARKTEAL=(143,188,143)
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
xstretch = 2
ystretch = 2 
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Squidward Compatibility Test")
def squidward():
	
	screen.fill(skyblue)
	face=pygame.Rect(300-xstretch,150-ystretch,120+2*xstretch,60+2*ystretch)
	pygame.draw.ellipse(screen,TEAL,face)
	lol=pygame.Rect(330-xstretch,200-ystretch,60+2*xstretch,40+2*ystretch)
	pygame.draw.rect(screen,TEAL,lol)
	mouth=pygame.Rect(300-xstretch,230-ystretch,120+2*xstretch,30+2*ystretch)
	pygame.draw.ellipse(screen,TEAL,mouth)
	eyeone=pygame.Rect(335-xstretch,185-ystretch,25+2*xstretch,45+2*ystretch)
	pygame.draw.ellipse(screen,WHITE,eyeone)
	eyetwo=pygame.Rect(360-xstretch,185-ystretch,25+2*xstretch,45+2*ystretch)
	pygame.draw.ellipse(screen,WHITE,eyetwo)
	eyedotone=pygame.Rect(340-xstretch,195-ystretch,10+2*xstretch,10+2*ystretch)
	pygame.draw.rect(screen,RED,eyedotone)
	eyedottwo=pygame.Rect(365-xstretch,195-ystretch,10+2*xstretch,10+2*ystretch)
	pygame.draw.rect(screen,RED,eyedottwo)
	line=pygame.Rect(310-xstretch,250-ystretch,100+2*xstretch,2+2*ystretch)
	pygame.draw.rect(screen,BLACK,line)
	nose=pygame.Rect(345-xstretch,215-ystretch,20+2*xstretch,50+2*ystretch)
	pygame.draw.ellipse(screen,DARKTEAL,nose)
	pygame.display.flip()

squidward()
tallclarinet("What is your favorite instrument?")
squidward()
wideclarinet("What is your favorite color?")
squidward()
tallclarinet("What do you like to do on the weekends?")
squidward()
wideclarinet("Who is your favorite singer?")
squidward()
tallclarinet("What is your favorite thing to get at the Krusty Krab?")
squidward()
wideclarinet("What secrets do you have?")
squidward()
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()	
