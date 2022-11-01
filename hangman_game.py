import random

def stickmanDraw(missedLetters):
    print("\n" * 2)

    if(missedLetters == 0):
        print("+---+")
        print("|   |")
        print("|   O")
        print("|  /|\\")
        print("|  / \\")
        print("|")
        print("=========")

    elif(missedLetters == 1):
        print("+---+")
        print("|   |")
        print("|   O")
        print("|  /|\\")
        print("|  / ")
        print("|")
        print("=========")

    elif(missedLetters == 2):
        print("+---+")
        print("|   |")
        print("|   O")
        print("|  /|\\")
        print("|")
        print("|")
        print("=========")

    elif(missedLetters == 3):
        print("+---+")
        print("|   |")
        print("|   O")
        print("|  /|")
        print("|")
        print("|")
        print("=========")

    elif(missedLetters == 4):
        print("+---+")
        print("|   |")
        print("|   O")
        print("|   |")
        print("|")
        print("|")
        print("=========")

    elif(missedLetters == 5):
        print("+---+")
        print("|   |")
        print("|   O")
        print("|")
        print("|")
        print("|")
        print("=========")
        
    elif(missedLetters == 6):
        print("+---+")
        print("|   |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("=========")

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)    
    return wordList[wordIndex]

def findCorrectLetterPosition(correctLetters, secretWord, blanks):
    numberOfLetters = secretWord.count(correctLetters[-1])
    changePosition = -1
    
    for j in range(numberOfLetters):
        changePosition = secretWord.find(correctLetters[-1], changePosition + 1)
        blanks[changePosition] = correctLetters[-1]

    return blanks

def displayBoard(missedLetters, correctLetters, secretWord, blanks):
    stickmanDraw(missedLetters)
    print("Wrong guesses: %d" % (len(missedLetters)))

    if (len(missedLetters) > 0 or len(correctLetters) > 0):
        print("Guessed Letters: [%s]" % (','.join(missedLetters + correctLetters)))

    if(len(correctLetters) > 0 and correctLetters[-1] in secretWord):
        blanks = findCorrectLetterPosition(correctLetters, secretWord, blanks)

    print("\n" * 1)
    print(' '.join(blanks))
    print("\n" * 1)

def getGuess(alreadyGuessed):
    while True:
        guess = input("Guess a letter: ").lower()
        print("\n" * 40)

        if (len(guess) != 1):
            print("Please enter one letter!")

        elif (guess in alreadyGuessed):
            print("You have already guessed that letter. Choose again.")
        
        elif (guess not in 'abcdefghijklmnopqrstuvwxyz'):
            print("Please, enter one LETTER.")
        
        else:
            return guess

def playAgain():
    print("\n" * 5)
    gameIsDone = input("Do you want to play again? (yes or no)").lower().startswith("y")
    return gameIsDone

wordList = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel',
         'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer',
         'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog',
         'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole',
         'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl',
         'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat',
         'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk',
         'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad',
         'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

print("H A N G M A N  GAME")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(wordList)
blanks = ['-'] * len(secretWord)
gameIsDone = False

while (not gameIsDone):
    displayBoard(missedLetters, correctLetters, secretWord, blanks)
    guess = getGuess(missedLetters + correctLetters)

    if (guess in secretWord):
        correctLetters = correctLetters + guess
        foundAllLetters = True
        
        for i in range(len(secretWord)):
            if (secretWord[i] not in correctLetters):
                foundAllLetters = False
                break

        if (foundAllLetters):
            print("Congratulations! The secret word is %s!" % (secretWord))
            print("You won!!!!")
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess
    
        if (len(missedLetters) > 6): 
            displayBoard(missedLetters, correctLetters, secretWord, blanks)
            print("You have run out of guesses!")
            print("After %d missed guesses and %d correct guesses, the word was %s" % (len(missedLetters), len(correctLetters), secretWord))
            gameIsDone = True
    
    if (gameIsDone): 
        if(playAgain()):
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord = getRandomWord(wordList)
            blanks = ['-'] * len(secretWord)

        else:
            break
