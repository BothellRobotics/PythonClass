import random

#Create Welcome message Ask player A to enter a word
hangman_display = ["",
                    "       _______________        " ,
                    "       |              | " ,
                    "       |              | " ,
                    "       |              O " ,
                    "       |            \ | / " ,
                    "       |             \|/ " ,
                    "       |              | " ,
                    "       |              | " ,
                    "       |             / \ " ,
                    "       |            /   \ " ,
                    "       |   " ,
                    "       |   " ,
                    "       |   " ,
                    "_______|_________________________ "
]

print("\n".join(hangman_display[0 : len(hangman_display)]))
print("\n")
print("Welcome to Hangman Game!!!")

secret_word_clue = {
    "Taylor Swift", "Famous Female Pop Singer",
    "Java", "Number one programming language",
    "Albert Einstein", "A famous American Scientist",
    "Barack Obama", "A well known American President",
    "The White House", "A famous building in Washington DC"
}

rand = random.randint(0, len(secret_word_clue) + 1)


#If player B guesses correct letter, fill in the letter at that position

#If player A guesses wrong letter, start building hangman

#If the hangman is complete, player A wins

#Player B wins, if  word  guessed correctly before the hangman formed

