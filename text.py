'''
测试tuples是否支持in operator
'''
# my_tuple = (1,2,3,4,5)
# if 1 in my_tuple:
#     print('yes')

'''
test functions as arguments
'''
# def func_a():
#     print ('inside func_a')
# def func_c(z):
#     print ('inside func_c')
#     return z()
# print (func_c(func_a)) 

'''
test the is_word_guessed function
'''
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
secret_word = 'apple'
letters_guessed = ['e','i','k','p','r','s']
print(is_word_guessed(secret_word,letters_guessed))