print("Welcome to SOUP.")
print("What is your birth month number?")
month = int(input())
if month == 1:
	first = "Rusty"
if month == 2:
	first = "Chummy"
if month == 3:
	first = "Pockmark"
if month == 4:
	first = "Sea Legs"
if month == 5:
	first = "Plunderin'"
if month == 6:
	first = "Peg Leg"
if month == 7:
	first = "Two-Toes"
if month == 8:
	first = "FishFace"
if month == 9:
	first = "Rapscallion"
if month == 10:
	first = "Yerr"
if month == 11:
	first = "Swashbuckler"
if month == 12:
	first = "Squidlips"
print("What is your birth day number?")
day = int(input())
numday = day%5
print(numday)
if numday == 0:
	last = "Swabslop"
if numday == 1:
	last = "O'Jeff"
if numday == 2:
	last = "Crabcakes"
if numday == 3:
	last = "Rattlebones"
if numday == 4:
	last = "Noosemaker"
print("What is your favorite color?")
print("Red?")
print("Orange?")
print("Yellow?")
print("Green?")
print("Blue?")
print("Purple?")
color = input()
if color == "Red":
	middle = "McStubby" 
if color == "Yellow":
	middle == "O'Jelly"
if color == "Orange":
	middle = "Felonious"
if color == "Green":
	middle = "Plunderboot"
if color == "Blue":
	middle = "O'Scurvy"
if color == "Purple":
	middle = "O'Growly"
print("What is SOUP you ask?")
print("It's quite simple.")
print("Super")
print("Old")
print("Ugly")
print("Pirate")
print("We have generate your SOUP name")
print("Are ye ready kids?")
capt = input()
print("Your SOUP name is {0} {1} {2}.".format(first,middle,last))
