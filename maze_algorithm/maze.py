import os

height, width = 11, 11
wallDictionary = {'NORTH':1, 'EAST':2, 'SOUTH':4, 'WEST':8}


def create_maze(height, width):
    maze = [[[0,0] for x in range(width)] for x in range(height)]
    #Adding walls around the maze
    for i in range(height):
        maze[i][0][1] |= 8
        maze[i][-1][1] |= 2
    for j in range(width):
        maze[0][j][1] |= 1
        maze[-1][j][1] |= 4
            
    return maze


'''
function for printing out maze with distances and walls
There will be a + at each corner of cell
Walls will be represented by a | or ---
The distance to the target will be printed in the cell
'''
def print_maze(maze, pos=(-1,-1)):
    for i in range(height):
        ToplineSTR = "+"
        BottomLineSTR = ""
        mouse = "^"
        for j in range(width):
            if maze[i][j][1] & 1:
                ToplineSTR += "----"
            else:
                ToplineSTR += "    "

            ToplineSTR  += "+"
            if maze[i][j][1] & 8:
                BottomLineSTR += "|"
            else:
                BottomLineSTR += " "

            if (i,j) == pos:
                BottomLineSTR += mouse
            else:
                BottomLineSTR += " "
            
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
   

'''
Reads a maze from a text file
Returns a maze
'''
def read_maze(maze, filename):
    
    # ref: https://stackoverflow.com/questions/4060221/how-to-reliably-open-
    # a-file-in-the-same-directory-as-the-currently-running-scrip
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(__location__, filename)) as f:
        for line in f:
            line = line.split(",")
            add_wall(maze, (int(line[0].strip()), int(line[1].strip())), line[2].strip())

'''
Adds wall(s) to the given cell with an input file

Parameters:
maze: the maze
cell: the cell to add the wall to (tuple of indecies)
wall: the wall to add (string, NORTH, SOUTH, EAST, WEST)
Wall can be a list of walls as well
'''
def add_wall(maze, cell, wall):
    i, j = cell
    
    if isinstance(wall, list):
        for w in wall:
            maze[i][j][1] |= wallDictionary[w]
            add_wall_neighbor(maze, cell, w)
    else:
        maze[i][j][1] |= wallDictionary[wall]
        add_wall_neighbor(maze, cell, wall)

#Helper function to make sure walls are added correctly
def add_wall_neighbor(maze, cell, wall):
    i, j = cell

    if wall == "NORTH":
        maze[i-1][j][1] |= 4
    elif wall == "SOUTH":
        maze[i+1][j][1] |= 1
    elif wall == "EAST":
        maze[i][j+1][1] |= 8
    elif wall == "WEST":
        maze[i][j-1][1] |= 2
