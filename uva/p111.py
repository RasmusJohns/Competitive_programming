from sys import stdin

def LCS(Y, X, cnt):
    """ Gets the longest common subseq of Y and X.
    Y and X are of length cnt"""
    
    memoize = [[0 for x in range(MAX_CNT)] for y in range(MAX_CNT)]

    for y in range(1, cnt + 1):
        for x in range(1, cnt + 1):
            if X[x] == Y[y]:
                memoize[y][x] = memoize[y - 1][x - 1] + 1
            else:
                memoize[y][x] = max(memoize[y][x - 1], memoize[y - 1][x])

    return memoize[cnt][cnt]

def convert_indata(num_lst, cnt):
    """ Re-arranges the data to fit memoization """
    lst = [0] * (cnt+1)
    for i in range(cnt + 1):
        lst[int(num_lst[i-1])] = i
    return lst

MAX_CNT = 21
i = 0
correct_number_lst = []
count = 0

for line in stdin:
    if i != 0:
        number_lst = line.strip().split(" ")
        number_lst = convert_indata(number_lst, count)
        if i == 1:
            correct_number_lst = number_lst
        else:
            print(LCS(correct_number_lst, number_lst, count))
    else:
        count = int(line)
    i = i + 1
