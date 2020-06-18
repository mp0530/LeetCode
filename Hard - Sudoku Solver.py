# Building a Sudoku !!!
# Guess is needed!
# Backtracking!

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def block(board): # solve using 3 by 3 grids
            remain = False
            for y in range(3):
                for x in range(3):
                    s = [str(a) for a in range(1,10)]
                    for j in range(y*3,(y+1)*3):
                        for i in range(x*3,(x+1)*3):
                            if type(board[j][i]) == str:
                                try:
                                    s.remove(board[j][i])
                                except:
                                    return 0
                    s = set(s)
                    for j in range(y*3,(y+1)*3):
                        for i in range(x*3,(x+1)*3):
                            if type(board[j][i]) == set:
                                board[j][i] = board[j][i].copy() & s
                                if len(board[j][i]) == 1:
                                    board[j][i] = board[j][i].pop()
                                elif len(board[j][i]) == 0:
                                    return 0
                                else:
                                    remain = True
            return [remain]
                                
        def row(board): # solve by rows
            remain = False
            for y in range(9):
                s = [str(i) for i in range(1,10)]
                for x in range(9):
                    if type(board[y][x]) == str:
                        try:
                            s.remove(board[y][x])
                        except:
                            return 0
                s = set(s)
                for x in range(9):
                    if type(board[y][x]) == set:
                        board[y][x] = board[y][x].copy() & s
                        if len(board[y][x]) == 1:
                            board[y][x] = board[y][x].pop()
                        elif len(board[y][x]) == 0:
                            return 0
                        else:
                            remain = True
            return [remain]
        
        def col(board): # solve by columns
            remain = False
            for x in range(9):
                s = [str(i) for i in range(1,10)]
                for y in range(9):
                    if type(board[y][x]) == str and board[y][x] != ".":
                        try:
                            s.remove(board[y][x])
                        except:
                            return 0
                s = set(s)
                for y in range(9):
                    if type(board[y][x]) == set:
                        board[y][x] = board[y][x].copy() & s
                        if len(board[y][x]) == 1:
                            board[y][x] = board[y][x].pop()
                        elif board[y][x] == 0:
                            return 0
                        else:
                            remain = True
                    elif board[y][x] == ".":
                        board[y][x] = s
                        if len(s) > 1:
                            remain = True
            return [remain]

        def main(board): # initiate
            while True:
                bb = deepcopy(board)
                
                c = col(board)
                if not c:
                    return False
                if not c[0]:
                    return True
                
                r = row(board)
                if not r:
                    return False
                if not r[0]:
                    return True
                
                b = block(board)
                if not b: # check if guess is wrong
                    return False # return to the for loop in guess
                if not b[0]:
                    return True

                if board == bb: # need to guess
                    return guess(board)
        res = []
        def guess(board): # implement backtracking
            for y in range(9):
                for x in range(9):
                    if type(board[y][x]) != str and len(board[y][x]) == 2: # find the cell w/ 2 possible answer
                        s = list(board[y][x])
                        s.sort(reverse = True)
                        res.append(deepcopy(board))
                        for i in s: # pick one of two
                            board1 = deepcopy(board)
                            board[y][x] = i
                            if main(board):
                                return True # return true if lucky
                            for i in range(len(board)):
                                board[i] = board1[i] # go for second trial
                        else:
                            return False # if both are wrong (because there is wrong guess before this guess)
        main(board)
        
# This approach uses basic sudoku way of solving initially, but if either columns, rows, blocks give us more imformation, we 
# have to guess an answer unfortunately. This is when dfs backtracking come into place. I tried to find pick one of two (#108)
# This gives us the fastest possible way of returning the solved sudoku.
