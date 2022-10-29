#hangman game design
def hangman(word): 
    charCount = len(word)
    wrongCount = 0
    correctCount = 0
    hangmanParts = 6
    #didnt rlly need the boolean here, although couldve done while win = false for loop
    win = False
    #made a list for the word because strings are immutable and lists would be easier
    #to work with. I tried slicing strings but it got messy
    wordList = list(word)
    hangVisual = ["    |    ",
                  "        ",
                  "        ",
                  "        ",
                  "        ",
                  ]

    print("Welcome to hangman!")
    gameScore = ["_"] * charCount
    
    print("The word has " + str(charCount) + " letters. \n")
    #join method makes the score easier to read
    print(" ".join(gameScore))

    while wrongCount < hangmanParts: 
        guess = input("\nGuess: ")
        if guess in wordList:
            correctCount += 1
            #used join method to output each stage of the hangman on a new line
            print("\n".join(hangVisual[0:wrongCount]))
            print("Correct!")
            correctIndex = wordList.index(guess)
            gameScore[correctIndex] = guess
            #line below replaces the correct index in the string with $ so the user can guess duplicate letters
            wordList[correctIndex] = '$'
            print(" ".join(gameScore))
            if correctCount == charCount:
                print("You win!")
                break
        elif guess not in wordList: 
            wrongCount += 1
            #did this to make it more similar to the real game
            if wrongCount == 1:
                hangVisual[1] = "    O    "
            elif wrongCount == 2:
                hangVisual[2] = "    |    "
            elif wrongCount == 3:
                hangVisual[2] = "    |\   "
            elif wrongCount == 4:
                hangVisual[2] = "   /|\   "
            elif wrongCount == 5:
                hangVisual[3] = "     \   "
            elif wrongCount == 6:
                hangVisual[3] = "   / \    "
            print("\n".join(hangVisual[0:wrongCount]))
            print("""Incorrect! \nIncorrect guesses: """ + str(wrongCount))
            print(" ".join(gameScore))
            if wrongCount == hangmanParts:
                print("You lose!")
                break

word = input("Enter a word for hangman:")
hangman(word)
