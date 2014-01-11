import random

def playGame():
	answer = random.randint(1, 100)
	guess = 0
	tries = 0
	
	while guess != answer:
		guess = int(input("Guess a number"))
		tries += 1
		if guess > answer:
			print "Too big, try a smaller number."
		if guess < answer:
			print "Too small, try a bigger number."
	
	print "You guessed the right number in " + str(tries) + " tries."

playagain = "yes"
while playagain == "yes":
	playGame()
	playagain = input("Do you want to play another round? (yes/no)")


# 1. How many tries it took you to get the answer
# 2. Do you want to play another round? (yes/no)
# 3. If no, print out max # of tries and min # of tries
