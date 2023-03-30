import random

def hangman():
    list_of_words = ['hangman', 'india', 'virat', 'dell', 'laptop']
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ""
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')
    while len(word) > 0 :
        main_word = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_"

        if main_word == word :
            print(main_word)
            print("You won")
            break
        print("guess the word", main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1

            if turns == 9 :
                print("9 turns are left")
                print("----------------")
            elif turns == 8 :
                print("8 turns are left")
                print("----------------")
                print("       O         ")
            elif turns == 7 :
                print("7 turns are left")
                print("----------------")
                print("       O        ")
                print("       |        ")
            elif turns == 6 :
                print("6 turns are left")
                print("----------------")
                print("       O        ")
                print("       |        ")
                print("      /         ")
            elif turns == 5 :
                print("5 turns are left")
                print("----------------")
                print("       O        ")
                print("       |        ")
                print("      / \        ")
            elif turns == 4 :
                print("4 turns are left")
                print("----------------")
                print("      \O        ")
                print("       |        ")
                print("      / \       ")
            elif turns == 3 :
                print("3 turns are left")
                print("----------------")
                print("      \O/       ")
                print("       |        ")
                print("      / \       ")
            elif turns == 2 :
                print("2 turns are left")
                print("----------------")
                print("      \O/   |     ")
                print("       |        ")
                print("      / \       ")
            elif turns == 1 :
                print("only 1 turn left!! hangman on his last breath")
                print("----------------")
                print("      \O/_|       ")
                print("       |        ")
                print("      / \       ")
            elif turns == 0 :
                print("You let a good man die")
                print("----------------")
                print("       O_|       ")
                print("      /|\        ")
                print("      / \       ")
                break

name = input("Enter your name :")
print(f"Welcome,{name}")
print("-----------------------------")
print("try to guess the word in less than 10 attempts")
hangman()
