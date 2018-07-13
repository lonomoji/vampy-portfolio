i=0
print("Answer these generic questions and we will tell you your counselor soulmate")
print("What is your name?")
name = input()
print ("What is your favorite color? Blue Red Green Yellow")
color = input()
if color == "Blue":
	i+=0
if color == "Red":
	i+=1
if color == "Green":
	i+=2
if color == "Yellow":
	i+=3
print ("What is your favorite fruit? Apples Oranges Bananas Strawberries")
fruit = input()
if fruit == "Apples": 
	i+=0
if fruit == "Oranges":
	i+=1
if fruit == "Bananas":
	i+=2
if fruit == "Strawberries":
	i+=3
print ("What is your favorite season? Spring Summer Fall Winter")
season = input()
if season == "Spring":
	i+=0
if season == "Summer":
	i+=1
if season == "Fall":
	i+=2
if season == "Winter":
	i+=3
print(i)
if i>=0 and i<2:
	print("{0} you are meant for Aaron Bard, his beans, and his Soviet Cap. It was meant to be.".format(name))
elif i>=2 and i<4:
	print("{0} you are meant for Jacob Couch, his friendship bracelets, dislocated shoulder, and deflated raft. Free trips to the Couch Store for you.".format(name))
elif i>=4 and i<6:
	print("{0} you are meant for Tori Edwardson, the Good Counselor, official badbutt. Head Counselor privileges go to you.".format(name))
elif i>=6 and i<=8:
	print("{0} you are meant for Gabe Smith. You must stop those darn swingin' lanyards and campers without their name tags. Keep things in order!".format(name))
elif i==9:
	print("{0} you are meant for Dr. Julia Link Roberts herself. Wave at campers as they return from class and compliment campers for their pizza-scooping.".format(name))
