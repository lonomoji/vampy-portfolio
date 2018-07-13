import numpy 
import sounddevice
import time
import math
import pygame

def mus():
	fs = 48000
	sounddevice.default.samplerate=fs
	G = numpy.zeros(int(0.125*fs))
	hz=783 #G
	for x in range(len(G)):
		G[x]= round(math.sin(2*math.pi*x*hz/fs))
		
	Ab = numpy.zeros(int(.125*fs))
	hz=415 #G
	for x in range(len(Ab)):
		Ab[x]= round(math.sin(2*math.pi*x*hz/fs))
	A = numpy.zeros(int(.125*fs))
	hz=459 #G
	for x in range(len(A)):
		A[x]= round(math.sin(2*math.pi*x*hz/fs))
	Bb = numpy.zeros(int(.125*fs))

	hz=466 #G
	for x in range(len(Bb)):
		Bb[x]= round(math.sin(2*math.pi*x*hz/fs))
	B = numpy.zeros(int(.125*fs))
	hz=493 #G
	for x in range(len(B)):
		B[x]= round(math.sin(2*math.pi*x*hz/fs))
	C = numpy.zeros(int(.125*fs))
	hz=523 #G
	for x in range(len(C)):
		C[x]= round(math.sin(2*math.pi*x*hz/fs))
	Db = numpy.zeros(int(.125*fs))
	hz=554 #G
	for x in range(len(Db)):
		Db[x]= round(math.sin(2*math.pi*x*hz/fs))
	D = numpy.zeros(int(.125*fs))
	hz=587 #G
	for x in range(len(D)):
		D[x]= round(math.sin(2*math.pi*x*hz/fs))
	Eb = numpy.zeros(int(.125*fs))
	hz=622 #G
	for x in range(len(Eb)):
		Eb[x]= round(math.sin(2*math.pi*x*hz/fs))
	E = numpy.zeros(int(.125*fs))
	hz=659 #G
	for x in range(len(E)):
		E[x]= round(math.sin(2*math.pi*x*hz/fs))
	F = numpy.zeros(int(.125*fs))
	hz=698 #G
	for x in range(len(F)):
		F[x]= round(math.sin(2*math.pi*x*hz/fs))
	Gb = numpy.zeros(int(.125*fs))
	hz=739 #G
	for x in range(len(Gb)):
		Gb[x]= round(math.sin(2*math.pi*x*hz/fs))
	song = (Ab,A,Bb,B,C,Db,D,Eb,E,F,Gb,G,Gb,F,E,Eb,D,Db,C,B,Bb,A,)

	data = numpy.concatenate(song)
	sounddevice.play(data)
	time.sleep(2.5)

img = pygame.image.load('startrek.bmp')


size=(460,260)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (220,175,0)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CareerTrek")

screen.fill(WHITE)
screen.blit(img,(140,45))
#c
Cbottom=pygame.Rect(100,100,30,10)
pygame.draw.rect(screen,YELLOW,Cbottom)
Cmid=pygame.Rect(100,50,10,50)
pygame.draw.rect(screen,YELLOW,Cmid)
Ctop=pygame.Rect(100,50,30,10)
pygame.draw.rect(screen,YELLOW,Ctop)
#r
circ=pygame.Rect(195,50,30,30)
pygame.draw.ellipse(screen,YELLOW,circ)
firstline=pygame.Rect(195,50,10,60)
pygame.draw.rect(screen,YELLOW,firstline)
secondline=pygame.Rect(205,75,20,35)
pygame.draw.rect(screen,YELLOW,secondline)
pygame.draw.polygon(screen,WHITE,[(204,80),(204,110),(216,110)])
pygame.draw.polygon(screen,WHITE,[(215,75),(226,70),(226,110)])
rhole=pygame.Rect(204,59,12,12)
pygame.draw.ellipse(screen,WHITE,rhole)	
#e
Ebig=pygame.Rect(240,50,30,60)
pygame.draw.rect(screen,YELLOW,Ebig)
Etop=pygame.Rect(252,62,30,14)
pygame.draw.rect(screen,WHITE,Etop)
Ebot=pygame.Rect(252,84,30,14)
pygame.draw.rect(screen,WHITE,Ebot)
#e
Ebig=pygame.Rect(285,50,30,60)
pygame.draw.rect(screen,YELLOW,Ebig)
Etop=pygame.Rect(297,62,30,14)
pygame.draw.rect(screen,WHITE,Etop)
Ebot=pygame.Rect(297,84,30,14)
pygame.draw.rect(screen,WHITE,Ebot)
#r
circ=pygame.Rect(330,50,30,30)
pygame.draw.ellipse(screen,YELLOW,circ)
firstline=pygame.Rect(330,50,10,60)
pygame.draw.rect(screen,YELLOW,firstline)
secondline=pygame.Rect(340,75,20,35)
pygame.draw.rect(screen,YELLOW,secondline)
pygame.draw.polygon(screen,WHITE,[(339,80),(339,110),(351,110)])
pygame.draw.polygon(screen,WHITE,[(350,75),(360,70),(360,110)])
rhole=pygame.Rect(339,59,12,12)
pygame.draw.ellipse(screen,WHITE,rhole)
#t	
topt=pygame.Rect(200,150,30,15)
pygame.draw.rect(screen,YELLOW,topt)
bottomt=pygame.Rect(210,150,10,60)
pygame.draw.rect(screen,YELLOW,bottomt)
#r
circ=pygame.Rect(245,150,30,30)
pygame.draw.ellipse(screen,YELLOW,circ)
firstline=pygame.Rect(245,150,10,60)
pygame.draw.rect(screen,YELLOW,firstline)
secondline=pygame.Rect(255,175,20,35)
pygame.draw.rect(screen,YELLOW,secondline)
pygame.draw.polygon(screen,WHITE,[(254,180),(254,210),(266,210)])
pygame.draw.polygon(screen,WHITE,[(265,175),(275,170),(275,210)])
rhole=pygame.Rect(254,159,12,12)
pygame.draw.ellipse(screen,WHITE,rhole)
#e
Ebig=pygame.Rect(290,150,30,60)
pygame.draw.rect(screen,YELLOW,Ebig)
Etop=pygame.Rect(302,162,30,14)
pygame.draw.rect(screen,WHITE,Etop)
Ebot=pygame.Rect(302,184,30,14)
pygame.draw.rect(screen,WHITE,Ebot)


#k
Kmain=pygame.Rect(330,150,40,60)
pygame.draw.rect(screen,YELLOW,Kmain)
pygame.draw.polygon(screen, WHITE, [(340,150),(340,175),(360,150)])
pygame.draw.polygon(screen, WHITE, [(340,185), (340,210),(360,210)])
pygame.draw.polygon(screen, WHITE, [(350,180),(370,150),(370,210)])



pygame.display.flip()
mus()
time.sleep(2.5)	
pygame.quit()

print("Welcome to CareerTrek. This is an interactive program which will allow you to find a career path best suited to your needs. What is your name?")
name=input()
print("Hello {0}, how old are you?".format(name))
age=int(input())
print("Do you currently have a job?")
ansr=input()
print("Are you ready to find the perfect career for you?")
ready=input()
if ready in ["no", "n", "No","NO"]:
	print("Get out.")
	exit()
if ready in ["Yes","y","yes"]:
	print ("Okay, let's get it rolling.")
	mus()
# Askers
def ask_area():
	fp = open("job.data.csv","r")
	N=int(fp.readline())
	areas = []
	for i in range(N):
		line = fp.readline().strip()
		print("{0}: {1}".format(i+1, line))
		areas.append(line)
	fp.close()

	print ("What is your preferred area of interest(type in corresponding number)?")
	prefer = int(input())
	while prefer <= 0 or prefer > len(areas):
		print ("Please retype your number.")
		prefer = int(input())
	return areas[prefer-1]
	

# Main
prefer = ask_area()
print("Here are the major jobs in that field.")
time.sleep(1)	

fp = open("jobslist.csv","r")
for line in fp.readlines():
	row = line.split(", ")
	area,title,education,salary = row

	if prefer == area:
		print("{0}".format(title))	
fp.close()
time.sleep(2)
def ask_edu():
	print ("0. High School Dropout")
	print ("1: High School Diploma")
	print ("2: Associate's Degree")
	print ("3: Bachelor's Degree")
	print ("4: Master's Degree")
	print ("5: Doctorate")
	print ("What is your projected educational attainment in this field?")
	educ = int(input())
	while educ < 0 or educ >= 6:
		print ("Please retype your number.")	
		educ = int(input())
	return educ 

edu_counter=0
edu = ask_edu()
print("Here are the jobs that still match your criteria:")
time.sleep(1)
def edu_check():
	global edu_counter
	fp = open("jobslist.csv","r")
	for line in fp.readlines():
		row = line.split(", ")
		area,title,education,salary = row
		if int(edu) >= int(education) and prefer == area:
			edu_counter+=1
			print("{0}".format(title))	
fp.close()
edu_check()
while edu_counter ==0:
	print("There are no jobs matching your criteria. Try a higher level of education.")
	time.sleep(1)
	ask_edu()
	edu_check()
time.sleep(2)
def ask_sal():
	print ("0. $10-$15")
	print ("1: $15-$20")
	print ("2: $20-$25")
	print ("3: $25-$30")
	print ("4: $30-$35")
	print ("5: $35-$40")
	print ("6: $40-$45")
	print ("7: $45-$50")
	print ("8: $50+")
	print ("What is your preferred starting hourly wage?")
	sal = int(input())
	while sal < 0 or sal >= 9:
		print("Please retype your number.")
		sal = int(input())
	return sal
sal_counter=0 
def sal_check():
	global sal_counter
	sal = ask_sal()
	fp = open("jobslist.csv","r")
	print("Here are the jobs that match all your criteria and are the best suited for you, {0}:".format(name))
	time.sleep(1)
	for line in fp.readlines():
		row = line.split(", ")
		area,title,education,salary = row
		if int(edu) >= int(education) and prefer == area and int(salary) >= int(sal):
			sal_counter+=1
			print("{0}".format(title))
sal_check()
while sal_counter == 0:
		print("There are no jobs matching your criteria. Try a lower salary.")
		time.sleep(1)
		ask_sal()
		sal_check()
	
	

