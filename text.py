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
secret_word = 'apple'
letters_guessed = ['e','i','k','p','r','s']
print(get_available_letters(letters_guessed))