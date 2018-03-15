import random
words = []
database = open("words.data")
words = database.read().split(";")
print(words)

word = words[random.randint(0, len(words) - 1)]
word = word.upper()
progress = ['*'] * len(word)
lifes = 10
wrongLetters = []


def check(letter):
	global lifes
	indexi = []
	for index in range(len(word)):
		if word[index] == letter:
			indexi.append(index)
	for index in indexi:
		progress[index] = letter
	if len(indexi) == 0:
		wrongLetters.append(letter)
		lifes -= 1


def printProgress():
	progressStr = ''
	for letter in progress:
		progressStr += letter
	wrongLettersStr = ""
	for letter in wrongLetters:
		wrongLettersStr += " " + letter + ","
	wrongLettersStr = wrongLettersStr[:-1]
	print(str(lifes) + ' lifes left')
	print('word: ' + progressStr)
	print("Failed attempts:" + wrongLettersStr)


while True:
	printProgress()
	print('')
	inputChar = input("Your guess: ")
	upperChar = inputChar.upper()
	guess = upperChar[0]
	check(guess)
	print('')

	if lifes == 0:
		print("Game Over")
		break

	numberOfUnknown = 0
	for letter in progress:
		if letter == "*":
			numberOfUnknown += 1

	if numberOfUnknown == 0:
		print("You Win")
		break
