import random

words = []						# createing empty array to store all the loaded words
database = open("words.data")				# opening the file "words.data" which contains the database of words
words = database.read().split(";")			# converting the database into an array by splitting it at every semicolon

word = words[random.randint(0, len(words) - 1)]		# choosing a random word from the database
word = word.upper()					# making sure the word is uppercase
progress = ["*"] * len(word)				# createing an array to store the word progress and filling it with asterisks
lives = 10						# creating a variable to store the lives left and initializing it with the value 10
wrongLetters = []					# creating an empty array to show all the wrong letters the player has already tried


def check(testLetter):					# creating the function to do all the logic
	global lives					# loading the lives variable into the function"s scope
	indexes = []					# creating an empty array to store all the indexes at which the word has the passed letter 
	for index in range(len(word)):			# looping through the word
		if word[index] == testLetter:		# comparing the current letter of the word to the passed letter
			indexes.append(index)		# if these two letter are the same, add the index to the "indexes" array
	for index in indexes:				# looping through all the indexes from the "indexes" array
		progress[index] = testLetter		# changing all the asterisks in the "progress" array the the passed letter which are in the right spot
	if len(indexes) == 0:				# if the "indexes" array contains no items (if the passed letter doesn"t apear in the word)...
		wrongLetters.append(testLetter)		# ...add the passed letter to the "wrongLetters" array and...
		lives -= 1				# ...subtracting 1 life for guessing a wrong letter


def printProgress():					# creating a function to print the current state of the game to the console
	progressStr = ""				# creating an empty string, that will contain the current progress on the word
	for item in progress:				# looping through the "progress" array
		progressStr += item			# attaching each item to the "progressStr" variable
	wrongLettersStr = ""				# creating an empty string, that will contain all the letters the player has guessed wrong
	for item in wrongLetters:			# looping through the "wrongLetters" array
		wrongLettersStr += " " + item + ","	# attaching each item to the "wrongLettersStr" variable and adding a space before and a comma after it
	wrongLettersStr = wrongLettersStr[:-1]		# trimming off the last letter, because it will be a comma (see above)
	print(buildImage(lives))			# printing the current progress
	print("word: " + progressStr)			# printing the current word progress
	print("Failed attempts:" + wrongLettersStr)	# printing the failed letters

def buildImage(livesLeft = 10):				# creating a function to get a string containing the image of the current state of the game
	images = [					# creating an array containing all possible images to display
		" ______\n |/    |\n |    O|\n |    /|\ \n |    / \ \n_|_",
		" ______\n |/    |\n |     O\n |    /|\ \n |    / \ \n_|_",
		" ______\n |/    |\n |     O\n |    /|\ \n |        \n_|_",
		" ______\n |/    |\n |     O\n |     |  \n |        \n_|_",
		" ______\n |/    |\n |     O\n |        \n |        \n_|_",
		" ______\n |/    |\n |      \n |        \n |        \n_|_",
		" ______\n |/     \n |      \n |        \n |        \n_|_",
		"       \n |/     \n |      \n |        \n |        \n_|_",
		"       \n |      \n |      \n |        \n |        \n_|_",
		"       \n        \n        \n          \n          \n_ _",
		"       \n        \n        \n          \n          \n   "]
	return images[livesLeft]			# returning the selected image


while True:						# This is the main loop of the game. "while True" ensures that the game will run forever, until it is stopped by a game over or a win with a "break"
	printProgress()					# print the current progress
	print("")					# add an empty line under it
	inputChar = str(raw_input("Your guess: "))	# get the player"s guess
	upperChar = inputChar.upper()			# make the guess uppercase
	guess = upperChar[0]				# take only the first letter of the input
	check(guess)					# check the letter (run the logic)
	print("")					# add an empty line

	if lives == 0:					# if the lives reach 0...
		print(buildImage(0))			# ...print an image of the man committing suicide to the console, ...
		print("Game Over")			# ...print "Game Over" to the console and...
		break					# stop the loop (stop the game)

	numberOfUnknown = 0				# create a variable to store how many letters are still unknown
	for letter in progress:				# loop through the "progress" array
		if letter == "*":			# check for an asterisk
			numberOfUnknown += 1		# if an asterisk is found, add 1 to the "numberOfUnknown" variable

	if numberOfUnknown == 0:			# if the number of unknown letters is 0 (word is figured out)...
		print(					# ...print an image of the man not committing suicied to the console, ...
			" ______\n |/    |\n |     O\n |  \O/ \n |   |    \n_|_ / \ ")
		print("You Win")			# ...print "You Win" to the console and...
		break					# stop the loop
