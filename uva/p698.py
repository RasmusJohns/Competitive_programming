import sys


def lower_case(letter):
    return (ord(letter) > 96 and ord(letter) < 123)

def upper_case(letter):
    return (ord(letter) > 64 and ord(letter) < 91)

def digit(letter):
    return (ord(letter) > 47 and ord(letter) < 58)

def parse(line, line_number):
    """ Parses a line, counting all the occurences of words
    in list "looking_for""""
    potential_word = ""
    for letter in line:
        if upper_case(letter):
            letter = letter.lower()
        if lower_case(letter) or digit(letter):
            potential_word += letter
        else:
            if potential_word in looking_for:
                count[potential_word].append(line_number)
            potential_word = ""
    if potential_word in looking_for:
        count[potential_word].append(line_number)

def format_output():
    """ Formatting. So much ugly code just to format the output string"""
    sorted_keys = sorted(count.keys())
    line = ""
    consecutive = 0
    for key in sorted_keys:
        key_list = count[key]
        last_val = -1
        if len(count[key]) > 0:
                
            if key_list:
                last_val = key_list[0]
            while key_list:
                current_val = key_list.pop(0)

                if current_val != last_val:
                    if current_val == last_val + 1:                        
                        consecutive += 1
                    else:
                        if consecutive == 0:
                            line += ", " + str(last_val)
                        else:
                            line += ", " + str(last_val - consecutive)+"-"+str(last_val)
                            consecutive = 0
                last_val = current_val
            if consecutive == 0:
                if last_val != -1:
                    line += ", " + str(last_val)
            else:
                line += ", " + str(last_val - consecutive)+"-"+str(last_val)
            for i in range(0, looking_for.count(key)):
                print(key.upper(), line.strip(", "))
            line = ""
            last_val = -1
            consecutive = 0

mode = "READ_INDEX"
looking_for = []
count = dict()
line_number = 1
case_number = 1

for line in sys.stdin:
    if line == "\n":
        if mode == "READ_TEXT":
            print("Case", case_number)
            format_output()
            print()
            looking_for = []
            count = dict()
            case_number += 1
            line_number = 1
            mode = "READ_INDEX"
        else:
            mode = "READ_TEXT"
    elif mode == "READ_INDEX":
        line = line.strip().lower()
        if len(line) < 23:
            looking_for.append(line)
            count[line] = []
    elif mode == "READ_TEXT":
        parse(line, line_number)
        line_number += 1
    
