import pygame
import time

size=(720,540)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,230,0)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CareerTrek")

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()
	screen.fill(BLACK)
	#T
	topt=pygame.Rect(300,50,30,15)
	pygame.draw.rect(screen,YELLOW,topt)
	bottomt=pygame.Rect(310,50,10,60)
	pygame.draw.rect(screen,YELLOW,bottomt)
	#R
	circ=pygame.Rect(335,50,30,30)
	pygame.draw.ellipse(screen,YELLOW,circ)
	firstline=pygame.Rect(335,50,10,60)
	pygame.draw.rect(screen,YELLOW,firstline)
	secondline=pygame.Rect(345,75,20,35)
	pygame.draw.rect(screen,YELLOW,secondline)
	pygame.draw.polygon(screen,BLACK,[(344,80),(344,110),(356,110)])
	pygame.draw.polygon(screen,BLACK,[(355,75),(365,70),(365,110)])
	rhole=pygame.Rect(344,59,12,12)
	pygame.draw.ellipse(screen,BLACK,rhole)
	#E
	Ebig=pygame.Rect(400,50,30,60)
	pygame.draw.rect(screen,YELLOW,Ebig)
	Etop=pygame.Rect(412,62,30,14)
	pygame.draw.rect(screen,BLACK,Etop)
	Ebot=pygame.Rect(412,84,30,14)
	pygame.draw.rect(screen,BLACK,Ebot)



	pygame.display.flip()
	time.sleep(1/45)

