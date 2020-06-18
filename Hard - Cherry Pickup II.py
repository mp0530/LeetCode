# Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents the number of cherries that you can collect.

# You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) , and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

# Return the maximum number of cherries collection using both robots  by following the rules below:

# From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
# When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
# When both robots stay on the same cell, only one of them takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in the grid.

class Solution:
    def cherryPickup(self, grid):
        y = len(grid)
        x = len(grid[0])
        # dp[row][robot1][robot2]
        dp = [[[-100000 for _ in range(x+2)] for _ in range(x+2)] for _ in range(y)] # +2 for extra rows at front and back
        for i in range(1,x+1):
            for j in range(1,x+1):
                dp[-1][i][j] = grid[-1][i-1] + grid[-1][j-1] if i!= j else 0
        for row in reversed(range(y-1)): # start from row-2
            for a in range(1,x+1): # only concern possible rows
                for b in range(1,x+1):
                    dp[row][a][b] = max(dp[row+1][a-1][b-1],dp[row+1][a-1][b],dp[row+1][a-1][b+1],\
                                       dp[row+1][a][b-1],dp[row+1][a][b],dp[row+1][a][b+1],\
                                       dp[row+1][a+1][b-1],dp[row+1][a+1][b],dp[row+1][a+1][b+1]) +\
                                       grid[row][a-1] + (grid[row][b-1] if a != b else 0)
        return dp[0][1][-2] 

# Thought: this is an obvious Dynamic Programming problem, but the implement is difficult that makes this question "Hard".
# There are two robots that affect the total cherry counts, so we have to make a dp[row][robot1][robot2] that records
# every possibility of cherry counts in a row. For each dp, it is affected by 9 possible counts from the previous row:
# [robot1-1:robot1+2]*[robot2-1:robot2+2] is 9. I use bottom-up solution for this and return dp[0][1][-2] which is the robot1
# at position 0 and robot2 at position -1. I added 2 extra column with large negative numbers to deal with out of bound possiblity.
# Overall, this is a pretty efficient code. Time complexity is O(9*len(grid)*len(grid[0])^2) or O(9*n*m^2)
