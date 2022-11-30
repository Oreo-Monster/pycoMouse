import os

height, width = 16, 16
wallDictionary = {'NORTH': 1, 'EAST': 2, 'SOUTH': 4, 'WEST': 8}

def create_maze(height, width):
    maze = [[{"distance": 0, "walls": 0, "visited": False} for x in range(width)] for x in range(height)]
    #Adding walls around the maze
    for i in range(height):
        maze[i][0]["walls"] |= 8
        maze[i][-1]["walls"] |= 2
    for j in range(width):
        maze[0][j]["walls"] |= 1
        maze[-1][j]["walls"] |= 4
            
    return maze

#function for printing out maze with distances and walls
#There will be a + at each corner of cell
#Walls will be represented by a | or ---
#The distance to the target will be printed in the cell
def print_maze(maze, pos=(-1,-1)):
    for i in range(height):
        ToplineSTR = "+"
        BottomLineSTR = ""
        mouse = "^"
        for j in range(width):
            if maze[i][j]["walls"] & 1:
                ToplineSTR += "----"
            else:
                ToplineSTR += "    "

            ToplineSTR  += "+"
            if maze[i][j]["walls"] & 8:
                BottomLineSTR += "|"
            else:
                BottomLineSTR += " "

            if (i,j) == pos:
                BottomLineSTR += mouse
            else:
                BottomLineSTR += " "
            
            BottomLineSTR += str(maze[i][j]["distance"])

            if maze[i][j]["visited"]:
                BottomLineSTR += "*"
            else:
                BottomLineSTR += " "

            if maze[i][j]["distance"] < 10:
                BottomLineSTR += " "
            else:
                BottomLineSTR += ""

            if j == width-1:
                if maze[i][j]["walls"] & 2:
                    BottomLineSTR += "|"
                    
        print(ToplineSTR)
        print(BottomLineSTR)
    
    bottom = "+"
    for i in range(width):
        if maze[-1][i]["walls"] & 4:
            bottom += "----+"
        else:
            bottom += "    +"
    print(bottom)
   

def read_maze(maze, filename):
    '''
    Reads a maze from a text file
    Returns a maze
    '''
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, filename)) as f:
        for line in f:
            line = line.split(",")
            x = int(line[0].strip())
            y = int(line[1].strip())
            wall = line[2].strip()
            
            add_wall(maze, (x, y), wall)

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
            maze[i][j]["walls"] |= wallDictionary[w]
            add_wall_neighbor(maze, cell, w)
    else:
        maze[i][j]["walls"] |= wallDictionary[wall]
        add_wall_neighbor(maze, cell, wall)

#Helper function to make sure walls are added correctly
def add_wall_neighbor(maze, cell, wall):
    i, j = cell

    if wall == "NORTH":
        maze[i-1][j]["walls"] |= 4
    elif wall == "SOUTH":
        maze[i+1][j]["walls"] |= 1
    elif wall == "EAST":
        maze[i][j+1]["walls"] |= 8
    elif wall == "WEST":
        maze[i][j-1]["walls"] |= 2

if __name__ == "__main__":
    maze = create_maze(height, width)
    print(maze)