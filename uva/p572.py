from sys import stdin

class Deposit:
    
    def __init__(self, contains_oil):
        self.contains_oil = contains_oil
        self.visited = False

class Board:

    def __init__(self, number_of_rows, number_of_columns):
        self.board = []
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns

    def add_row(self, lst):
        self.board.append(lst)

    def reset_board(self):
        self.board = []

    def print_board(self):
        """Debugging function"""
        for row in self.board:
            for dep in row:
                if dep.contains_oil:
                    print("@", end='')
                else:
                    print("#", end='')
            print("")

    def count_deposits(self):
        """Returns the number of deposits within in the Board"""
        number_of_deposits = 0
        
        for row_nr in range(self.number_of_rows):
            for column_nr in range(self.number_of_columns):
                if self.board[row_nr][column_nr].contains_oil and not self.board[row_nr][column_nr].visited:
                    self.recursive_deposit_search(row_nr, column_nr)
                    number_of_deposits += 1
        return number_of_deposits

    def recursive_deposit_search(self, y, x):
        """Recursively searches all oil-containing neighbours,
        marking them visited"""
        self.board[y][x].visited = True
        
        cases = ((-1,-1), (-1,0), (-1,1),
                 (0,-1), (0,1),
                 (1,-1), (1,0), (1,1))

        for diff in cases:
            new_x = x + diff[0]
            new_y = y + diff[1]
            
            if self.check_bounds(new_x, new_y) and self.board[new_y][new_x].contains_oil and not self.board[new_y][new_x].visited:
                self.recursive_deposit_search(new_y, new_x)

    def check_bounds(self, x, y):
        return x >= 0 and x < self.number_of_columns and y >= 0 and y < self.number_of_rows


lines_left = 0
board = False

for line in stdin:
    if lines_left == 0:
        if board:
            print(board.count_deposits())

        read_line = line.strip().split()
        
        lines_left, row_length = int(read_line[0]), int(read_line[1])
        board = Board(lines_left, row_length)
        
    else:
        board.add_row([Deposit(True) if x == '@' else Deposit(False) for x in line.strip().split()[0]])
        lines_left -= 1
    
        

