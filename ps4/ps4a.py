# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    length = len(sequence)
    l_sequence = list(sequence)
    permutations = []
    if length == 1:
        return l_sequence
    else:
        first_char = l_sequence[0]
        l_subsequence = l_sequence
        del(l_subsequence[0])
        sub_sequence = ''.join(l_subsequence)
        sub_permutations = get_permutations(sub_sequence)
        for sub_permutation in sub_permutations:
            l_permutation = []
            for i in range(length):
                l_permutation.append('*')
            for i in range(length):
                l_permutation[i] = first_char
                for j in range(i):
                    l_permutation[j] = sub_permutation[j]
                for j in range(i+1,length):
                    l_permutation[j] = sub_permutation[j-1]
                permutations.append(''.join(l_permutation))
        return permutations 

if __name__ == '__main__':
   #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

    example_input = 'rat'
    print('Input: ',example_input)
    print('Expected Output: ',['rat','rta','art','atr','tra','tar'])
    print('Actual Output: ',get_permutations(example_input))



