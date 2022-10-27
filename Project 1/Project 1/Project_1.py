print("Welcome to my computer quiz")

input()

print("Do you want to play? (Y/N)")

playing = input()

if playing != "Y":
	quit()


print("")
print("Lets goooo :)")

print("")
Question = ["What was Meta Platforms Inc formerly known as?", "Which former British colony was given back to China in 1997?", "What does CIA stand for?", "How many lives is a cat said to have?", "Why do german girls scream their age?", "Rojo is the Spanish word for which colour?"]
Answer = ["Facebook", "Hongkong", "Central Intelligence Agency", "9", "My Genetics", "Red"]
number = 0

for x in Question:
	print(x)
	response = input()

	if response == Answer[number]:
		print("Correct")
		number = number + 1
	else:
		print("Wrong")
		quit()
		break

print("Congratulations, you've completed the exam")
quit()