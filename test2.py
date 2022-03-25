width = 10
height = 10

def create_maze(height, width):
    maze = [[[0,0] for x in range(width)] for x in range(height)]
    for i in range(height):
        maze[i][0][1] |= 8
        maze[i][-1][1] |= 2
    for j in range(width):
        maze[0][j][1] |= 1
        maze[-1][j][1] |= 4
            
    return  maze


def set_target(maze, target):
    
    stack = []

    clear_visited(maze)
    for i in range(height):
        for j in range(width):
            maze[i][j][0] = 10000

    maze[target[0]][target[1]][0] = 0
    stack.append(target)

    i_addition = [-1, 0, 1, 0]
    j_addition = [0, 1, 0, -1]

    while len(stack) != 0:
        i, j = stack.pop()
        set_visited(maze, i, j)
        for k in range(4):
            if maze[i][j][1] & 2**k:
                #Wall
                continue
            else:
                #Open
                #Checking if the distance is shorter then our current
                if maze[i+i_addition[k]][j+j_addition[k]][0] > maze[i][j][0]+1:
                    print(f"updating {i+i_addition[k]}, {j+j_addition[k]} to be {maze[i][j][0]+1}")
                    maze[i+i_addition[k]][j+j_addition[k]][0] = maze[i][j][0]+1
                    stack.append((i+i_addition[k], j+j_addition[k]))



#The fifth bit is the visited boolean
#If the cell has been visited, set to 1
#If the cell has not been visited, set to 0
#This function will set the visited boolean to 1
def set_visited(maze, i, j):
    maze[i][j][1] |= 16

#This function will set cell to not visited
def set_unvisited(maze, i, j):
    maze[i][j][1] &= ~16

def clear_visited(maze):
    for i in range(height):
        for j in range(width):
            set_unvisited(maze, i, j)

#funtion for printing out maze with distances and walls
#There will be a + at each corner of cell
#Walls will be represented by a | or ---
#The distance to the target will be printed in the cell
def print_maze(maze):
    for i in range(height):
        ToplineSTR = "+"
        BottomLineSTR = ""
        for j in range(width):
            if maze[i][j][1] & 1:
                ToplineSTR += "----"
            else:
                ToplineSTR += "    "

            ToplineSTR  += "+"
            if maze[i][j][1] & 8:
                BottomLineSTR += "| "
            else:
                BottomLineSTR += "  "
            
            BottomLineSTR += str(maze[i][j][0])

            if maze[i][j][1] & 16:
                BottomLineSTR += "*"
            else:
                BottomLineSTR += " "

            if maze[i][j][0] < 10:
                BottomLineSTR += " "
            else:
                BottomLineSTR += ""

            if j == width-1:
                if maze[i][j][1] & 2:
                    BottomLineSTR += "|"
        
        print(ToplineSTR)
        print(BottomLineSTR)
    
    bottom = "+"
    for i in range(width):
        if maze[-1][i][1] & 4:
            bottom += "----+"
        else:
            bottom += "    +"
    print(bottom)




maze = create_maze(height=10, width=10)
print_maze(maze)

set_target(maze, (4,8))
print_maze(maze)

for i in range(3, 7):
    maze[4][i][1] |= 1
    maze[5][i][1] |= 4

print_maze(maze)

set_target(maze, (6,6))
print_maze(maze)