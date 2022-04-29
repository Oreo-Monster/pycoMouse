#Implemntation of Flood Fill algorrim for 
#solving maze

#Storing the maze in a 2D array


height, width = 11, 11
wallDictionary = {'NORTH':1, 'EAST':2, 'SOUTH':4, 'WEST':8}


def create_maze(height, width):
    maze = [[[0,0] for x in range(width)] for x in range(height)]
    for i in range(height):
        maze[i][0][1] |= 8
        maze[i][-1][1] |= 2
    for j in range(width):
        maze[0][j][1] |= 1
        maze[-1][j][1] |= 4
            
    return  maze

#Walls are represented in maze[i][j][1], with the following code
#We will conside the first 4 bits of the integer to represent the walls
#0 for no wall, 1 for wall
#first bit is north wall
#second bit is east wall
#third bit is south wall
#fourth bit is west wall
#Use bit operations to add walls
#For example, if we want to add a wall to the north wall, we can do
#maze[i][j][1] |= 1
#Another example, adding a wall to the west
#maze[i][j][1] |= 8
#This function will decode the wall information and return a list of walls
#If no walls return []
#If wall to north or south, return [NORTH, SOUTH]

def decode_walls(maze, cell):
    i, j = cell
    walls = []
    decode = ["NORTH", "EAST", "SOUTH", "WEST"]
    for k in range(4):
        if maze[i][j][1] & 2**k:
            walls.append(decode[k])
    return walls

#The fifth bit is the visited boolean
#If the cell has been visited, set to 1
#If the cell has not been visited, set to 0
#This function will set the visited boolean to 1
def set_visited(maze, cell):
    i, j = cell
    maze[i][j][1] |= 16

#This function will set cell to not visited
def set_unvisited(maze, cell):
    i, j = cell
    maze[i][j][1] &= ~16

def set_distance(maze, cell, dist):
    maze[cell[0]][cell[1]][0] = dist

def get_distance(maze, cell):
    return maze[cell[0]][cell[1]][0]

def clear_visited(maze):
    for i in range(height):
        for j in range(width):
            set_unvisited(maze, (i, j))


'''
Adds wall(s) to the given cell

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


def add_wall_neighbor(maze, cell, wall):
    i, j = cell
    try:
        if wall == "NORTH":
            maze[i-1][j][1] |= 4
        elif wall == "SOUTH":
            maze[i+1][j][1] |= 1
        elif wall == "EAST":
            maze[i][j+1][1] |= 8
        elif wall == "WEST":
            maze[i][j-1][1] |= 2
    except IndexError:
        pass
    


'''
Sets the target cell to have distance 0
and recalculates the distance for every other
cell in the maze, taking into account walls

Parameters:
maze: the maze
target: tuple indecies of the target cell
'''
def set_target(maze, target):
    #Setting all cells to have large distance
    for i in range(height):
        for j in range(width):
            maze[i][j][0] = 10000

    #Setting the target cell to have distance 0
    maze[target[0]][target[1]][0] = 0
    #Starting the stack, will hold tuples of indecies of cells
    stack = []
    stack.append(target)

    while len(stack) != 0:
        cell = stack.pop(-1)
        neighbors = get_neighbors(maze, cell)
        #minDist is the minimum distance of the neighbors
        minDist = get_distance(maze, cell)+1
        for neighbor in neighbors:
            #If the neighbor has a distance larger than the current cell + 1
            if get_distance(maze, neighbor) > minDist:
                #Then set the distance to the current cell + 1, and add neighbor to stack
                set_distance(maze, neighbor, minDist)
                stack.append(neighbor)

'''
Finds the minimum distance in negihbors of the given cell

Parameters:
maze: the maze
cell: the cell to find the minimum distance negihbors of (tuple of indecies)

Returns:
The minimum distance in neighbors of the given cell, and a list of the neighbors
'''
def get_min_neighbors(maze, cell, ignoreVisited=False):
    i, j = cell
    neighbors = []
    min_dist = 10000
    direction = -1
    i_addition = [-1, 0, 1, 0]
    j_addition = [0, 1, 0, -1]
    for k in range(4):
        if maze[i][j][1] & 2**k:
            #Wall
            continue
        else:
            #Open
            if ignoreVisited and maze[i+i_addition[k]][j+j_addition[k]][1] & 16:
                #Visited
                continue
            if maze[i+i_addition[k]][j+j_addition[k]][0] < min_dist:
                min_dist = maze[i+i_addition[k]][j+j_addition[k]][0]
                direction = k
                neighbors.append((i+i_addition[k], j+j_addition[k]))
    return min_dist, direction, neighbors



def walldetect(maze,compmaze, pos):
    '''update to detect walls simulation style'''
    i,j=pos
    i_add = [1,0,-1,0]
    j_add = [0,-1,0,1]
    for k in range(4):
        if i+i_add[k]<0 or i+i_add[k]>=height or j+j_add[k]<0 or j+j_add[k]>=width:
            continue
        maze[i+i_add[k]][j+j_add[k]][1] |= (compmaze[i+i_add[k]][j+j_add[k]][1] & 2**k)
    # maze[i][j-1][1] |= (compmaze[i][j-1][1] & 2) 
    # maze[i][j+1][1] |= (compmaze[i][j+1][1] & 8) 
    # maze[i+1][j][1] |= (compmaze[i+1][j][1] & 1) 
    # maze[i-1][j][1] |= (compmaze[i-1][j][1] & 4) 
    maze[i][j][1] = compmaze[i][j][1] 
    return


def get_neighbors(maze, cell):
    '''
    Will return a list of neighbors of a cell taking into account walls
    Takes the maze as first argument
    Takes the tuple of the cells index as second argument
    returns a list of tuples of the neighbors
    '''
    i, j = cell
    neighbors = []
    i_addition = [-1, 0, 1, 0]
    j_addition = [0, 1, 0, -1]
    for k in range(4):
        if maze[i][j][1] & 2**k:
            #Wall
            continue
        else:
            #Open
            neighbors.append((i+i_addition[k], j+j_addition[k]))

    return neighbors

'''
Updates the maze to reflect the walls of the current cell
using flood fill algrorithm

Parameters:
maze: the maze
cell: the cell where new walls were placed (tuple of indecies)
'''
def update(cell,maze):
    stack = []
    stack.append(cell)
    while len(stack) != 0:
        currentCell = stack.pop(-1)
        minDist, _, neighbors = get_min_neighbors(maze, currentCell)
        print(f"minDist of cell {currentCell}: {minDist}")
        if minDist+1 < get_distance(maze, currentCell):
            set_distance(maze, currentCell, minDist+1)
            stack.extend(neighbors)

    return




#funtion for printing out maze with distances and walls
#There will be a + at each corner of cell
#Walls will be represented by a | or ---
#The distance to the target will be printed in the cell
def print_maze(maze, pos=(-1,-1)):
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
                BottomLineSTR += "|"
            else:
                BottomLineSTR += " "

            if (i,j) == pos:
                BottomLineSTR += "^"
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

def read_maze(maze, filename):
    '''
    Reads a maze from a text file
    Returns a maze
    '''
    with open(filename) as f:
        for line in f:
            line = line.split(",")
            add_wall(maze, (int(line[0].strip()), int(line[1].strip())), line[2].strip())


def backtrack(maze, pos, path):
    neighbors = []
    i_addition = [-1, 0, 1, 0]
    j_addition = [0, 1, 0, -1]
    while len(neighbors) == 0:
        direction = path.pop(-1)
        pos = (pos[0]-i_addition[direction], pos[1]-j_addition[direction])
        minDist, new_direction, neighbors = get_min_neighbors(maze, pos, ignoreVisited=True)
        print_maze(maze, pos)
        print(pos)
        print("backtracking")
        input()
    print("finished backtracking, new direction is: ", new_direction)
    return new_direction, pos


def floodfill():
    i_addition = [-1, 0, 1, 0]
    j_addition = [0, 1, 0, -1]

    solution = create_maze(height, width)
    read_maze(solution, "maze1.txt")
    print_maze(solution)

    maze = create_maze(height, width)
    target = (height-1, width-1)
    set_target(maze, target)
    pos = (0,0)

    path = []

    while pos != target:
        #Read walls at current position from solution
        walldetect(maze, solution, pos)

        #set current position to visited
        set_visited(maze, pos)

        #Update the maze to reflect the walls of the current cell
        update(pos, maze)
        #Find the next cell to move to
        minDist, direction, neighbors = get_min_neighbors(maze, pos, ignoreVisited=True)

        if len(neighbors) == 0:
            direction, pos = backtrack(maze, pos, path)

        #Move to the next cell
        pos = (pos[0]+i_addition[direction], pos[1]+j_addition[direction])
        #add direction to path
        path.append(direction)
        print_maze(maze, pos)
        print(pos)
        input()






if __name__ == "__main__":

    floodfill()

