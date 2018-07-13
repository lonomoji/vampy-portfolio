print("What is yas?")
word = input()
def isYas(word):
	Yasses = True
	state=0
	for i in range(len(word)):
		if word[i].isalpha():
			if state == 0:
				if word[i] in ["Y","y"]:
					state=1
				else:
					Yasses = False
			elif state == 1:
				if word[i] in ["Y","y"]:
					state=1
				elif word[i] in ["A","a"]:
					state=2
				else:
					Yasses = False
			elif state == 2:
				if word[i]in ["A","a"]:
					state = 2
				elif word[i]in ["S","s"]:
					state = 3
				else:
					Yasses = False
			elif state == 3:
				if word[i]in ["S","s"]:
					state = 3
				else:
					Yasses = False
	if state != 3:
		Yasses = False
	return Yasses
isYas(word)
answer=isYas(word)
print(answer)					
