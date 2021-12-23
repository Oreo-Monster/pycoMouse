'''
bot functions:
#forward
#backward
#left
#right
#proximity
N/S(up/down)
E/W(right/left)
add golden thread alg
grid = []
PER UNIT FUNCTION CHECK(grid creation to keep track and add rows col): 
row addition(always north based to extend from start)
if dirdetector == N and bot.getrow > len(grid):
    grid.append(newrow)
(left/right cases :should probably have it catch OOI error)
if dirdetector == E and bot.getrow > len(grid):
    grid.append(newrow)
if dirdetector == W and bot.getrow < 0:
    grid.insert(newrow,0)
if front sensor prox.val: 
    grid[row - 1][col] = 0
if not frontsensor:
    if not left sensor and is rightsensor:
        grid[row][col-1] = 1
        grid[row][col+1] = 0
        turn right(90)
    elif not right sensor and is leftsensor:
        grid[row][col-1] = 1
        grid[row][col+1] = 0
        turn right(90)
    elif not right sensor and not left sensor:
        grid[row-1][col] = 1
        turn((-)180)
        
    else:
        grid[row-1][col] = 0
        fd()
'''