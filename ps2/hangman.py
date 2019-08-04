# Problem Set 2, hangman.py
# Name:ADF 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split() #return list
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    def remove_letter (letter,alist):
        for i in range(len(alist)):
            if letter == alist[i]:
                alist[i]='A'
        return alist
    secret_word_list=list(secret_word)
    for letter in letters_guessed:
        if letter in secret_word_list:
            remove_letter(letter,secret_word_list)
    for secret_letter in secret_word_list:
        if secret_letter != 'A':
            return False
    return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = list(secret_word)
    for i in range(len(guessed_word)):
      if guessed_word[i] not in letters_guessed:
        guessed_word[i] = '_ '
    guessed_word_string = ''.join(guessed_word)
    return guessed_word_string




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alllowercase_string = string.ascii_lowercase
    alllowercase_list = list(alllowercase_string)
    for letter in alllowercase_string:
      if letter in letters_guessed:
        alllowercase_list.remove(letter)
    available_letters = "".join(alllowercase_list)
    return available_letters
    
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to game Hangman!")
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    guesses_remaining = 6
    warning_remaining = 3
    letters_guessed = []
    print('You have',warning_remaining,'warnings left.')
    while True:
      print('-------------')
      print('You have',guesses_remaining,'guesses left.')
      print('Available letters:',get_available_letters(letters_guessed))
      letter = input('Please guess a letter:')
      if letter in string.ascii_uppercase:
        letter = str.lower(letter)
      if not str.isalpha(letter):
        if warning_remaining != 0:
          warning_remaining -= 1
          print("Oops! This is not a valid letter. You have",warning_remaining,'warnings left:',get_guessed_word(secret_word,letters_guessed))
        else:
          guesses_remaining -=1
          print('Oops! This is a not valid letter. You hanve no warnings left so you lose one guess:',get_guessed_word(secret_word,letters_guessed))
      elif letter in letters_guessed:
        if warning_remaining != 0:
          warning_remaining -=1
          print("Oops! You've already guessed that letter. You have",warning_remaining,'warnings left:',get_guessed_word(secret_word,letters_guessed))
        else:
          guesses_remaining -= 1
          print("Oops! You've already guessed that letter. You have no warning left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
      elif letter not in secret_word:
        letters_guessed.append(letter)
        if letter in 'aeio':
          guesses_remaining -= 2
        else:
          guesses_remaining -= 1
        print("Oops! That letter is not in my word.")
        print("Please guess a letter:",get_guessed_word(secret_word,letters_guessed))
      else:
        letters_guessed.append(letter)
        print('Good guess:',get_guessed_word(secret_word,letters_guessed))
      def get_socre():
        unique_letters = []
        for i in secret_word:
          if i not in unique_letters:
            unique_letters.append(i)
        return guesses_remaining * len(unique_letters)
      if is_word_guessed(secret_word,letters_guessed):
        print('-----------')
        print('Congratulations, you won!')
        print('Your total score for this game is:',get_socre())
        break
      elif guesses_remaining <= 0:
        print('-------------')
        print('Sorry, you ran out of the guesses. The word was',secret_word)
        break





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = 'else'
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
