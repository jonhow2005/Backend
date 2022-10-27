import random

print("Welcome")
print("")
print("Pick a number")
print("")
print("It's very important...")
print("")

range = input()
	
while range.isdigit:
	range = int(range)
	print("")
	break	
	if range.isdigit == False:
		print("Please pick a number")
		range = input()


r = random.randint(0,range * 2)

print("Magnificent")
print("")
print("I Have Chosen A Number")
print("")
print("You are to select a number yourself")
print("")
print("If the numbers are the same")
print("")
print("You Win")
print("")
print("Would You like to play my game? (Y/N)")
print("")
playing = input()
print("")
if playing != "Y":
	quit()
	
print("Great")
print("")
print("Please")
print("")
print("Pick a number")
print("")
number = input();
print("")

while number.isdigit:
	number = int(number)
	break	
	if number.isdigit == False:
		print("Please pick a number")
		number = input()
		print("")

		
print("You guessed ")
print("")
print(number)
print("")
print("I guessed ")
print("")
print(r)
print("")
if r == number:
	print("You win")
if r != number:
	print("You Lose")