#Implemntation of Flood Fill algorrim for 
#solving maze

#Storing the maze in a 2D array

height, width = 11, 11

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
    wallDictionary = {'NORTH':1, 'EAST':2, 'SOUTH':4, 'WEST':8}
    if isinstance(wall, list):
        for w in wall:
            maze[i][j][1] |= wallDictionary[w]
    else:
        maze[i][j][1] |= wallDictionary[wall]



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
def get_min_neighbors(maze, cell):
    i, j = cell
    dist = []
    neighbors = []
    i_addition = [-1, 0, 1, 0]
    j_addition = [0, -1, 0, 1]
    for k in range(4):
        if maze[i][j][1] & 2**k:
            #Wall
            continue
        else:
            #Open
            dist.append( maze[i+i_addition[k]][j+j_addition[k]][0])
            neighbors.append((i+i_addition[k], j+j_addition[k]))
    return min(dist), neighbors



def walldetect(maze,compmaze, i,j):
    '''update to detect walls simulation style'''
    maze[i,j-1,1] |= (compmaze[i,j-1,1] & 2) 
    maze[i,j+1,1] |= (compmaze[i,j+1,1] & 8) 
    maze[i+1,j,1] |= (compmaze[i+1,j,1] & 1) 
    maze[i-1,j,1] |= (compmaze[i-1,j,1] & 4) 
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
        minDist, neighbors = get_min_neighbors(maze, currentCell)
        if minDist+1 < get_distance(maze, currentCell):
            set_distance(maze, currentCell, minDist+1)
            stack.extend(neighbors)

    return




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



if __name__ == "__main__":

    maze = create_maze(height, width)

    set_target(maze, (height//2, width//2))

    print_maze(maze)


