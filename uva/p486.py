import sys

"""Expandable solution which could be applied to larger
problems easily."""

symbol_functions = {"zero": lambda n: n+0, "one":lambda n: n+1,
           "two":lambda n: n+2, "three":lambda n: n+3,
           "four":lambda n: n+4,"five":lambda n: n+5,
           "six":lambda n: n+6, "seven":lambda n: n+7,
           "eight":lambda n: n+8, "nine":lambda n: n+9,
           "ten":lambda n: n+10, "eleven":lambda n: n+11,
           "twelve":lambda n: n+12, "thirteen":lambda n: n+13,
           "fourteen":lambda n: n+14, "fifteen":lambda n: n+15,
           "sixteen":lambda n: n+16, "seventeen":lambda n: n+17,
           "eighteen":lambda n: n+18, "nineteen":lambda n: n+19,
           "twenty":lambda n: n+20, "thirty":lambda n: n+30,
           "forty":lambda n: n+40, "fifty":lambda n: n+50,
           "sixty":lambda n: n+60, "seventy":lambda n: n+70,
           "eighty":lambda n: n+80, "ninety":lambda n: n+90,
           
           "hundred":lambda n: n*100, "thousand":lambda n: n*1000,
           "million":lambda n: n*1000000}

symbol_separators = set(["thousand", "million"])

def get_digits_from_line(words):
    """ Takes a list of words, representing numbers,
    and returns the words' sum"""
    sub_sums = []
    sub_sum = 0
    negative = 1
    if words[0] == "negative":
        negative = -1
        words.pop(0)
    while words:
        word = words.pop(0)
        sub_sum = symbol_functions[word](sub_sum)
        if word in symbol_separators or not words:
            sub_sums.append(sub_sum)
            sub_sum = 0

    return sum(sub_sums) * negative

for line in sys.stdin:
    words = line.split()
    if words:
        print(get_digits_from_line(words))
    
