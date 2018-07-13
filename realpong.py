import pygame 
import numpy 
import sounddevice
import time
import math
import random
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
yellow = (255,230,0)
purple = (255,0,255)
SKIN = (255,228,181)
RANDOM = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
print ("What score are you playing to today?")
win=int(input())
print("Would you like to play against a CPU(AI) or one another(1v1)?")
answer=input()
if answer == "AI":
	print("What difficulty would you like?)")
	print("1.Beginner")
	print("2.Intermediate")
	print("3.Advanced")
	difficulty=int(input())
print("Would you like original(O), CRAZY(C), or customizable(custom) pong?")
pong=input()
if pong == "custom":
	print("What color should the background be?(red, green, blue, skyblue, yellow, purple, random)")
	red=(255,0,0)
	green=(0,255,0)
	blue=(0,0,255)
	skyblue=(142,229,238)
	yellow = (255,230,0)
	purple = (255,0,255)	
	backg_color=input()
	print("What color should the paddles be?(red, green, blue, skyblue, yellow, purple, random)")
	red=(255,0,0)
	green=(0,255,0)
	blue=(0,0,255)
	skyblue=(142,229,238)
	yellow = (255,230,0)
	purple = (255,0,255)
	paddle_color=input()
	print("What color should the ball be?(red, green, blue, skyblue, yellow, purple, random)")
	red=(255,0,0)
	green=(0,255,0)
	blue=(0,0,255)
	skyblue=(142,229,238)
	yellow = (255,230,0)
	purple = (255,0,255)
	ball_color=input()
xpos=350
fs = 48000 	
sounddevice.default.samplerate=fs
state=0
ypos=260
p1count=0
p2count=0
def scorer():
	if p1count == win:
		pygame.quit()
		print("Player 1 has won with a score of {0} to {1}".format(p1count,p2count))
		exit()
	elif p2count == win:
		pygame.quit()
		print("Player 2 has won with a score of {0} to {1}".format(p2count,p1count))
		exit()
	elif p2count>p1count:
		print("The score is {0} to {1} in favor of Player 2".format(p2count,p1count))
	elif p1count>p2count:
		print("The score is {1} to {0} in favor of Player 1".format(p2count,p1count))
	elif p2count==p1count:
		print("The score is tied {1} to {0}".format(p2count,p1count))

def paddlecol(a):
	paddle1 = pygame.Rect(30,200+paddle1x,20,140)
	pygame.draw.rect(screen,a,paddle1)
	paddle2 = pygame.Rect(670,200+paddle2x,20,140)
	pygame.draw.rect(screen,a,paddle2)
def ballcol(color):
	ball = pygame.Rect(xpos,ypos,20,20)
	pygame.draw.ellipse(screen,a,ball)	
movingLeft=True
movingRight=False
movingUp=False
movingDown=False
paddle1up=False
paddle2up=False
paddle1down=False
paddle2down=False
newStart=False
paddle1x=0
paddle2x=0
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Welcome to pong?!?")
while True:
	RANDOMPADDLE1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	RANDOMPADDLE2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	RANDOMBALL = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	RANDOMBG = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	if pong == "C":
		screen.fill(RANDOMBG)
		ball = pygame.Rect(xpos,ypos,20,20)
		pygame.draw.ellipse(screen,RANDOMBALL,ball)
		paddle1 = pygame.Rect(30,200+paddle1x,20,140)
		pygame.draw.rect(screen,RANDOMPADDLE1,paddle1)
		paddle2 = pygame.Rect(670,200+paddle2x,20,140)
		pygame.draw.rect(screen,RANDOMPADDLE2,paddle2)
	if pong == "O":
		screen.fill(black)
		ball = pygame.Rect(xpos,ypos,20,20)
		pygame.draw.ellipse(screen,white,ball)
		paddle1 = pygame.Rect(30,200+paddle1x,20,140)
		pygame.draw.rect(screen,white,paddle1)
		paddle2 = pygame.Rect(670,200+paddle2x,20,140)
		pygame.draw.rect(screen,white,paddle2)


	if pong == "custom":
		if backg_color== "red":
			screen.fill(red)
		if backg_color== "green":
			screen.fill(green)
		if backg_color== "yellow":
			screen.fill(yellow)
		if backg_color== "blue":
			screen.fill(blue)
		if backg_color== "skyblue":
			screen.fill(skyblue)
		if backg_color== "purple":
			screen.fill(purple)
		if backg_color== "random":
			screen.fill(RANDOMBG)
		if paddle_color == "red":
			paddle1 = pygame.Rect(30,200+paddle1x,20,140)
			pygame.draw.rect(screen,red,paddle1)
			paddle2 = pygame.Rect(670,200+paddle2x,20,140)
			pygame.draw.rect(screen,red,paddle2)
		if paddle_color == "random":
			paddle1 = pygame.Rect(30,200+paddle1x,20,140)
			pygame.draw.rect(screen,RANDOMPADDLE1,paddle1)
			paddle2 = pygame.Rect(670,200+paddle2x,20,140)
			pygame.draw.rect(screen,RANDOMPADDLE2,paddle2)
		if paddle_color == "green":
			paddle1 = pygame.Rect(30,200+paddle1x,20,140)
			pygame.draw.rect(screen,green,paddle1)
			paddle2 = pygame.Rect(670,200+paddle2x,20,140)
			pygame.draw.rect(screen,green,paddle2)
		if paddle_color == "yellow":
			paddle1 = pygame.Rect(30,200+paddle1x,20,140)
			pygame.draw.rect(screen,yellow,paddle1)
			paddle2 = pygame.Rect(670,200+paddle2x,20,140)
			pygame.draw.rect(screen,yellow,paddle2)
		if paddle_color == "blue":
			paddle1 = pygame.Rect(30,200+paddle1x,20,140)
			pygame.draw.rect(screen,blue,paddle1)
			paddle2 = pygame.Rect(670,200+paddle2x,20,140)
			pygame.draw.rect(screen,blue,paddle2)
		if paddle_color == "skyblue":
			paddle1 = pygame.Rect(30,200+paddle1x,20,140)
			pygame.draw.rect(screen,skyblue,paddle1)
			paddle2 = pygame.Rect(670,200+paddle2x,20,140)
			pygame.draw.rect(screen,skyblue,paddle2)
		if paddle_color == "purple":
			paddle1 = pygame.Rect(30,200+paddle1x,20,140)
			pygame.draw.rect(screen,red,paddle1)
			paddle2 = pygame.Rect(670,200+paddle2x,20,140)
			pygame.draw.rect(screen,red,paddle2)
		if ball_color == "red":
			ball = pygame.Rect(xpos,ypos,20,20)
			pygame.draw.ellipse(screen,red,ball)
		if ball_color == "green":
			ball = pygame.Rect(xpos,ypos,20,20)
			pygame.draw.ellipse(screen,green,ball)
		if ball_color == "yellow":
			ball = pygame.Rect(xpos,ypos,20,20)
			pygame.draw.ellipse(screen,yellow,ball)
		if ball_color == "blue":
			ball = pygame.Rect(xpos,ypos,20,20)
			pygame.draw.ellipse(screen,blue,ball)
		if ball_color == "random":
			ball = pygame.Rect(xpos,ypos,20,20)
			pygame.draw.ellipse(screen,RANDOMBALL,ball)
		if ball_color == "skyblue":
			ball = pygame.Rect(xpos,ypos,20,20)
			pygame.draw.ellipse(screen,skyblue,ball)
		if ball_color == "purple":
			ball = pygame.Rect(xpos,ypos,20,20)
			pygame.draw.ellipse(screen,purple,ball)
		
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()
		if event.type==pygame.KEYDOWN and event.key==pygame.K_w:
			paddle1up=True
		if event.type==pygame.KEYUP and event.key==pygame.K_w:
			paddle1up=False
		if event.type==pygame.KEYDOWN and event.key==pygame.K_s:
			paddle1down=True
		if event.type==pygame.KEYUP and event.key==pygame.K_s:
			paddle1down=False
		if event.type==pygame.KEYDOWN and event.key==pygame.K_i:
			paddle2up=True
		if event.type==pygame.KEYUP and event.key==pygame.K_i:
			paddle2up=False
		if event.type==pygame.KEYDOWN and event.key==pygame.K_k:
			paddle2down=True
		if event.type==pygame.KEYUP and event.key==pygame.K_k:
			paddle2down=False
		if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
			movingLeft=True
			movingRight=False
			movingUp=False
			movingDown=False
			state=0
	def wall():	
		wall = numpy.zeros(int(0.16*fs))
		hz=226 #G
		for x in range(len(wall)):
			wall[x]= round(math.sin(2*math.pi*x*hz/fs))
		sounddevice.play(wall)
	def paddle(): 
		paddle = numpy.zeros(int(0.25*fs))
		hz=459 #G
		for x in range(len(paddle)):
			paddle[x]= round(math.sin(2*math.pi*x*hz/fs))
		sounddevice.play(paddle)
	def score():
		score = numpy.zeros(int(.5*fs))
		hz=459 #G
		for x in range(len(score)):
			score[x]= round(math.sin(2*math.pi*x*hz/fs))
		sounddevice.play(score)
	if paddle1up:	
		paddle1x-=15
	if paddle1down:
		paddle1x+=15
	if answer == "1v1":
		if paddle2up:
			paddle2x-=15
		if paddle2down:
			paddle2x+=15
	if answer == "AI":
		if difficulty == 1:
			if paddle2up:
				paddle2x-=5
			if paddle2down:
				paddle2x+=5
		if difficulty == 2:
			if paddle2up:
				paddle2x-=10
			if paddle2down:
				paddle2x+=10
		if difficulty == 3:
			if paddle2up:
				paddle2x-=15
			if paddle2down:
				paddle2x+=15
		
	if paddle1x <= -200:
		paddle1up=False
	if paddle1x >= 200:
		paddle1down=False
	if paddle2x <= -200:
		paddle2up=False
	if paddle2x >= 200:
		paddle2down=False
	if xpos<=30 and xpos>=10 and ypos>=200+paddle1x and ypos<= 340+paddle1x:
		if paddle1up:
			movingLeft=False
			movingRight=True
			movingDown=False
			movingUp=True	
			paddle()	
		elif paddle1down:
			movingLeft=False
			movingRight=True
			movingUp=False
			movingDown=True
			paddle()
		else:
			movingLeft=False
			movingRight=True
			movingDown=False
			mvoingUp=False
			paddle()
	if xpos>=670 and xpos<=690 and ypos>=180+paddle2x and ypos<= 340+paddle2x:
		if paddle2up:
			movingRight=False
			movingLeft=True
			movingDown=False
			movingUp=True	
			paddle()	
		elif paddle2down:
			movingRight=False
			movingLeft=True
			movingUp=False
			movingDown=True
			paddle()
		else:
			movingRight=False
			movingLeft=True
			movingDown=False
			mvoingUp=False
			paddle()
	if state == 1:
		paddle1x=0
		paddle2x=0
		paddle1up=False
		paddle1down=False
		paddle2up=False
		paddle2down=False
	if xpos>740:
		score()
		print("Player 1 wins!")
		state=1
		movingLeft=False
		movingRight=False
		movingUp=False
		movingDown=False
		p1count+=1
		scorer()
		xpos=350
		ypos=260
		paddle1x=0
		paddle2x=0
		
	if xpos<-20:

		print("Player 2 wins!")
		score()
		p2count+=1
		state=1
		movingLeft=False
		movingRight=False
		movingUp=False
		movingDown=False
		scorer()
		xpos=350
		ypos=250
	if state==1:
		paddle1x=0
		paddle2x=0
		paddle1up=False
		paddle1down=False
		paddle2up=False
		paddle2down=False

		
	if answer == "AI":
		if movingLeft:
			if paddle2x>0:
				paddle2down=False
				paddle2up=True
				
			if paddle2x<0:
				paddle2up=False
				paddle2down=False
		if movingRight:
			if movingUp and 270+paddle2x>ypos:
				paddle2down=False
				paddle2up=True
			if movingUp and 270+paddle2x<ypos:
				paddle2up=False
				paddle2down=True
			if movingDown and 270+paddle2x<ypos:
				paddle2up=False
				paddle2down=True
			if movingDown and 270+paddle2x>ypos:
				paddle2down=False
				paddle2up=True
			if movingUp == False and movingDown == False and 270+paddle2x>ypos:
				paddle2down=False
				paddle2up=True
			if movingUp == False and movingDown == False and 270+paddle2x<ypos:
				paddle2up=False
				paddle2down=True
				
	if movingLeft:
		xpos-=20
	if movingRight: 
		xpos+=20
	if movingDown:
		ypos+=15
	if movingUp:
		ypos -=15
	if ypos >= 540:
		movingDown=False
		movingUp=True
		wall()
	elif ypos <= 0:
		movingUp=False
		movingDown=True
		wall()
	pygame.display.flip()
	time.sleep(1/45)
