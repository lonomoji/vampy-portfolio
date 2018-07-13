print("Give me ur data")
data = str(input())
l = []
stack=l

for i in range(len(data)):
	if data[i] == "{":
		l.append("{")
		print(l)
	if data[i] =="[":
		l.append("[")
		print(l)
	if data[i] == "(":
		l.append("(")
		print(l)

	if data[i] == "}":
		if len(l)==0:
			print ("Wrong")
			break
		top=l.pop()
		print(l)
		if top != "{":
			print("WRONG!")
			break	
	if data[i] == "]":
		if len(l)==0:
			print ("Wrong")
			break
		top=l.pop()
		print(l)
		if top != "[":
			print("WRONG!")
			break
	if data[i] == ")":
		if len(l)==0:
			print ("Wrong")
			break
		top=l.pop()
		print(l)
		if top != "(":
			print("WRONG!")
			break
for i in range(1):
	if len(l)!=0:
		print("you are wrong")
	
