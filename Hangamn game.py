import random
import string

words = ['army', 'beautiful', 'became', 'if', 'actually', 'beside', 'between','come','eye','five','fur','imposter', 'problem' ,'revenge' ,'few' ,'circle' ,'district','trade','quota','stop','depressed','disorder','dentist']

#choose a random word from list using random.choice() function
random_word = random.choice(words)

def get_guessed_word(secret_word, letters_guessed):
  string = ""
  for i in secret_word:
      if i in letters_guessed:
          string += i
      else:
          string += "_"
  return string

def is_word_guessed(secret_word, letters_guessed):
    
    # Code here
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True



def get_available_letters(letters_guessed):
    string = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for i in string:
        if i not in letters_guessed:
            temp += i
    return temp    
    
    
def hangman(secret_word):
    #code here
    print ("Welcome to the game, Hangman!")
    print ("I'm thinking of a word that is " + str(len(secret_word)) + " letters long.")
    letters_guessed = ''
    guessesLeft = 6
    print ("------------")
    while True:
        print ("You have " + str(guessesLeft) + " guesses left.")
        print ("Available letters: " + get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ")
        if guess in secret_word and guess not in letters_guessed:
            letters_guessed += guess
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            print ("Oops! You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed += guess
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            guessesLeft -= 1
        print ("------------")
        if guessesLeft <= 0:
            print ("Sorry, you ran out of guesses. The word was " + secret_word + ".")
            break
        if is_word_guessed(secret_word, letters_guessed):
            print ("Congratulations! You've won!")
            break


#check you function
hangman(random_word)