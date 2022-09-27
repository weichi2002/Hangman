import random
import os

class GallowsAndLittleGuy:
    def __init__(self):
        self.__number = 1
        self.__fname = ""


    def __str__(self):

        self.__fname = "man" + str(self.__number) + ".txt"
        fh = open(self.__fname, "r")
        data = fh.readlines()
        fh.close()
        s = ""
        for line in data:
            s += line
        return s


    def add_body_part(self):
        if self.__number < 5:
            self.__number += 1

        

class HangmanGame:

    def __init__(self, debugging_word = ""):

        if debugging_word == "":
            self.__secret = HangmanGame.select_random_word()
            
        else:
            self.__secret = debugging_word.lower()

        self.__board = ["_" for i in range(len(self.__secret))]

        self.__guess = 5
        self.guessed = []

    def __str__(self):
        return str(self.__board)

    def get_guess(self):
        return self.__guess
    
    def get_secret_word(self):
        return self.__secret

    def is_game_over(self):

        if self.__guess == 0:
            return True

        else:    #check every letter in string and return false if a letter does not match
            for i in range(len(self.__board)):
                if self.__board[i] != self.__secret[i]:
                    return False
            
            return True
            
            
    def check_letter_already_guessed(self, letter):
        
        for item in self.guessed:
            if item == letter:
                return True

        return False

    def process_word_guess(self, word):
        
        if word.lower() == self.__secret:
            #updates the board
            for i in range(len(self.__board)):
                self.__board[i] = word[i]
            return True

        else:
            self.__guess -= 1
            return False


    def process_letter_guess(self, letter):

        letter = letter.lower()
        self.guessed.append(letter)

        if letter in self.__secret:
            
            for i in range(len(self.__secret)):
                if letter == self.__secret[i]:
                    self.__board[i] = letter
            return True

        else:
            self.__guess -= 1
            return False
            

    def select_random_word():
        fh = open("american-english-dict.txt", "r")
        words = fh.readlines()
        fh.close()

        searching =  True
        while searching == True:
            num = random.randint(0, len(words))
            words[num] = words[num].strip()
            words[num] = words[num].lower()
            if 2 < len(words[num]) < 8:
                invalid = False
                for letter in words[num]:
                    if 97 > ord(letter) or ord(letter) > 122:
                        invalid = True
                if invalid == False:
                    searching = False
                    random_word =  words[num]

        return random_word

def main():
    

    hg = HangmanGame("")
    lg = GallowsAndLittleGuy()

    print("I am thinking of a", (len(hg.get_secret_word())), "letter word. Can you guess what it is?\nPress enter to continue: ")
    input()
    play = True
    
    while(play):
        
        os.system("clear")
        
        print(lg)
        print(hg)
        print(f"The number of guess remaining: {hg.get_guess()}")
        
        guess = input("Guess a letter or enter \"solve\" to guess the word: ")
        
        
        if len(guess) == 1:
            
            if hg.check_letter_already_guessed(guess):
                print()
                print("You have already guessed this letter: " + guess + "")
                print(f"You have guessed {hg.guessed}")
                print("Press enter to continue: ")
                input()
                
                

            else:
                letter_guess = hg.process_letter_guess(guess)
                if  letter_guess and hg.is_game_over():
                    print()
                    print("That's right, YOU WIN!!!\nThe word is " + hg.get_secret_word().upper())
                    play = False
                    
                elif not letter_guess and hg.is_game_over():
                    print()
                    print("You guessed wrong")
                    print("You lost, the word is " + hg.get_secret_word().upper())
                    play = False
                        
                elif not letter_guess:
                    lg.add_body_part()
                    print()
                    print("That letter is not in the word :(")
                    print("Press enter to continue: ")
                    input()
                   


        elif guess == "solve":
            
            word = input("What do you think the word is?: ")

            if hg.process_word_guess(word) and hg.is_game_over():
                print()
                print("That's right, YOU WIN!!! \n The word is " + hg.get_secret_word().upper())
                play = False


            else:
                if hg.is_game_over() == True:
                    print()
                    print("That's not the right word :(")
                    print("You lost, the word is " + hg.get_secret_word().upper())
                    play = False

                else:
                    print()
                    print("That's not the right word :( ")
                    print("Press enter to continue: ")
                    lg.add_body_part()
                    input()

        else:
            print()
            print("Invalid Input! \nEnter only \"solve\" or a single character ")
            input()
            

if __name__ == "__main__":
    os.system("clear")
    main()