import random
username = raw_input("Howdy, what's your name? ")

start_over = True
still_guessing = False
end_game = False
count = 0
guess = 0
high_score = 100

while end_game == False:

	if start_over == True and still_guessing == False:
		print("%s, I'm thinking of a number between 1 and 100. Try to guess my number.") % username

		random_number = random.randrange(1,101)
	
	guess = int(raw_input("Your guess? "))
	
	count = count + 1
	
	if guess in range(1, 101):
		start_over = True
		if guess < random_number:
			print "Your guess is too low, try again."
			still_guessing = True
		elif guess > random_number:
			print "Your guess is too high, try again."
			still_guessing = True
		else:
			print "Well done, %s! You found my number in %d tries!" % (username, count)
			if count < high_score:
				high_score = count
				print "Hey %s.  You guessed my number in the least amount of guesses" % username
				print "Congratulations!"
			play_again_flag = "Y"
			while play_again_flag == "Y":
				play_again = raw_input("Do you want to play again? ")
				if play_again.upper() == "Y":
					start_over = True
					print "Cool!  Here we go!"
					count = 0
					play_again_flag = "N"
					still_guessing = False
				elif play_again.upper() == "N":
					print "Awww.  I wanted to play again!"
					end_game = True
					play_again_flag = "N"
				else:
					print "Really!!??!! You can't decide Yes or No?"
	else:
		print "Hey %s! %s is not a number between 1 and 100?", (username, str(guess))


