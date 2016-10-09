import sys


def pascal(n):
    """Prints out n rows of Pascal's triangle.
    It returns False for failure and True for success."""
    row = [1]
    k = [0]
    answer = [[1]]
    for x in range(max(n,0)):
       row=[l+r for l,r in zip(row+k,k+row)]
       answer.append(row)
    return answer

def get_base_word(starting_letter, length):
    """Returns the lowest word of a certain length, based on the words
    starting letter. For instance: 'bc', 'efgh', 'xyz', 'vw' etc."""
    return [ord(starting_letter) + i for i in range(0, length) if ord(starting_letter) + i < 123]

def word_lst_to_word(lst):
    """Debug-function. Converts a list of integers
    to a readable word."""
    for number in lst:
        print(chr(number), end = '')
    print()

def traverse_word(word_lst, goal_lst):
    """Increments a word until it reaches the word's goal state.
    For instance, word_lst 'abc' would be incremented 4 times before it
    reached goal_lst 'abg', thus returning the value 4.
    """
    iteration = 0
    length = len(word_lst) - 1
    temp_length = length
    while word_lst != goal_lst:
        word_lst[length] += 1
         # increment all
        for i in range(length, -1 ,-1):
            if word_lst[i] == ord_limit - 1 - length + i and i > 0:
                word_lst[i-1] += 1
         # set correct alphabetic modulo on all
        temp_length = length
        for i in range(0, length):
            if i < length and word_lst[i+1] == ord_limit - 1- length + i + 1:
                word_lst[i+1] = word_lst[i] + 1
      
        iteration += 1
        
    return iteration


def get_base_sum(word):
    """ Takes a word and find its base value in the
    pascal tree. Speeds up the code a lot."""
    row_sum = sum([x for x in pascal_lst[alphabet-1][:len(word)]])
    column_sum = 0
    for i in range(97, ord(word[0])):
       column_sum += (pascal_lst[alphabet-2- i + 97][len(word)-1])
    return row_sum + column_sum 

def valid_word(word):
    """Checks if a word of is valid"""
    if word.lower() != word:
       return False
    for i in range(0, len(word) - 1):
       if (ord(word[i]) >= ord(word[i+1])):
          return False
    return True

alphabet = 27
ord_limit = 97 + alphabet
pascal_lst = pascal(alphabet)

for line in sys.stdin:
    line = line.strip("\n")

    ## Checks if the given word is valid
    if valid_word(line): 

        ## Gets the sum of the base-word, using pascal's triangle
        get_word_bottom_sum = get_base_sum(line)

        ## Gets the base-word
        base_word = get_base_word(line[0], len(line))

        ## Gets the difference between the base-word and line given to the program
        traverse_sum = traverse_word(base_word, [ord(letter) for letter in line])
        print(traverse_sum + get_word_bottom_sum)
    else:
        print(0)
    
