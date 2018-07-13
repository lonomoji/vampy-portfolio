import turtle
import math

pen = turtle.Turtle()
pen.up()
pen.lt(180)
pen.fd(275)
pen.lt(180)
pen.down()
def L(a):
	pen.rt(90)
	pen.fd(a)
	pen.lt(90)
	pen.fd(a/3)
def space(a):
	pen.up()
	pen.fd(a)
def O(a):
	for i in range(2):
		pen.down()
		pen.fd(2/3*a)
		pen.lt(90)
		pen.fd(a)
		pen.lt(90)
	pen.fd(2/3*a)
		
def R(a):
	pen.down()
	pen.lt(90)
	pen.fd(a)
	pen.rt(90)
	pen.fd(a/2)
	pen.rt(90)
	pen.fd(a/2)
	pen.rt(90)
	pen.fd(a/2)
	pen.lt(135)
	pen.fd(math.sqrt(2)*(a/2))
	pen.lt(45)
def E(a):
	pen.down()
	pen.lt(90)
	pen.fd(a)
	pen.rt(90)
	pen.fd(a/2)
	pen.lt(180)
	pen.fd(a/2)
	pen.lt(90)
	pen.fd(a/2)
	pen.lt(90)
	pen.fd(a/3)
	pen.lt(180)
	pen.fd(a/3)
	pen.lt(90)
	pen.fd(a/2)
	pen.lt(90)
	pen.fd(a/2)
def N(a):
	pen.down()
	pen.lt(90)
	pen.fd(a)
	pen.rt(135)
	pen.fd(math.sqrt(2)*a)
	pen.lt(135)
	pen.fd(a)
	pen.lt(180)
	pen.fd(a)
	pen.lt(90)
def Z(a):
	pen.lt(90)
	pen.fd(a)
	pen.down()
	pen.rt(90)
	pen.fd(a)
	pen.rt(135)
	pen.fd(1/2*math.sqrt(2)*a)	
	pen.rt(45)
	pen.fd(1/4*a)
	pen.lt(180)
	pen.fd(1/2*a)
	pen.lt(180)
	pen.fd(1/4*a)	
	pen.lt(45)
	pen.fd(1/2*math.sqrt(2)*a)
	pen.lt(135)
	pen.fd(a)
	
print("How big is the L?")
Lmod = int(input())
L(Lmod)
print("How big is the space between letters?")
spcmod = int(input())

space(spcmod)
print("How big is the O?")
Omod = int(input())
O(Omod)
space(spcmod)
print("How big is the R?")
Rmod = int(input())
R(Rmod)
space(spcmod)
print("How big is the E?")
Emod = int(input())
E(Emod)
space(spcmod)
print("How big is the N?")
Nmod = int(input())
N(Nmod)
space(spcmod)
print("How big is the Z?")
Zmod = int(input())
Z(Zmod)
space(spcmod)
O(Omod)






turtle.exitonclick()
