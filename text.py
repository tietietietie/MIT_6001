#############################
#测试tuples是否支持in operator
#############################
# my_tuple = (1,2,3,4,5)
# if 1 in my_tuple:
#     print('yes')

###############################
#test the functions as argumens
###############################

# def func_a():
#     print ('inside func_a')
# def func_c(z):
#     print ('inside func_c')
#     return z()
# print (func_c(func_a)) 

############################
#test the functions of pset2
############################
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
import string
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
    flag = True
    unguessed_letters = []
    my_word = my_word.replace(' ','')
    if len(my_word) == len(other_word):
      for i in range(len(my_word)):
        if (my_word[i] in string.ascii_letters) and (my_word[i] != other_word[i] or my_word[i] in unguessed_letters):
          flag = False
          break
        elif my_word[i] not in string.ascii_letters:
          unguessed_letters.append(other_word[i])
    else:
      flag = False
    return flag
# match_with_gaps("a_ _ _ _","apple")
# secret_word = 'apple'
# letters_guessed = ['e','i','k','p','r','s']
# print(get_available_letters(letters_guessed))
# print(float('nan'))
# a = [1,2,3]
# print(sum(a))

#----------------------------------
# test function substitute_hand
#----------------------------------
import random
def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    new_hand = hand
    if hand[letter] > 0:
        num_letter = hand[letter]
        del(new_hand[letter])
        all_letters = (list('qwertyuiopasdfghjklzxcvbnm'))
        for key in hand.keys():
            if hand[key] > 0 and key != '*':
                all_letters.remove(key)
        chosen_letter = random.choice(all_letters)
        new_hand[chosen_letter] = new_hand.get(chosen_letter,0) + num_letter
    return new_hand
hand = {'a':1, 'c':1, 'f':3, 'i':1, '*':1, 't':1, 'x':1}
print(substitute_hand(hand,'f'))