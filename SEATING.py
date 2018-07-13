print("What day is it")
day = int(input())
real_day = (day%4)
if real_day == 1:
	print("On day {0}, seating is this.".format(day))
	print ("0 1")
	print ("3 2")
elif real_day == 2:
	print("On day {0}, seating is this.".format(day))
	print("3 2")
	print("0 1")
elif real_day == 3:
	print("On day {0}, seating is this.".format(day))
	print("2 3")
	print("1 0")
else:
	print("On day {0}, seating is this.".format(day))
	print("1 0")
	print("2 3")	
