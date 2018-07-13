import numpy 
import sounddevice
import time
import math
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
	Gb[x]= round(math.sin(*math.pi*x*hz/fs))
song = (Ab,A,Bb,B,C,Db,D,Eb,E,F,Gb,G,Gb,F,E,Eb,D,Db,C,B,Bb,A,)

data = numpy.concatenate(song)
sounddevice.play(data)
time.sleep(30)
