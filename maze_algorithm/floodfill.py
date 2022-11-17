from time import sleep
from maze import *

#Implemntation of Flood Fill algorrim for 
#solving maze

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
ignoreVisited: if true, will ignore cells that have been visited

Returns:
The minimum distance of the neighboring cells,
the direction of the minimum distance, returned as an int
0 for north, 1 for east, 2 for south, 3 for west
These ints can be used in i_addition and j_addition
'''
def get_min_neighbors(maze, cell, ignoreVisited=False):
    i, j = cell
    neighbors = []
    min_dist = 10000
    direction = -1
    i_addition = [-1, 0, 1, 0]
    j_addition = [0, 1, 0, -1]
    tied_cells = [] #List of cells with the same distance as the minimum distance
    for k in range(4):
        if maze[i][j][1] & 2**k:
            #Wall
            continue
        else:
            #Open
            if ignoreVisited and maze[i+i_addition[k]][j+j_addition[k]][1] & 16:
                #Visited
                continue
            else:
                neighbors.append((i+i_addition[k], j+j_addition[k]))

            if maze[i+i_addition[k]][j+j_addition[k]][0] < min_dist: #new minimum distance
                min_dist = maze[i+i_addition[k]][j+j_addition[k]][0]
                direction = k
                tied_cells = []
            if maze[i+i_addition[k]][j+j_addition[k]][0] == min_dist:
                #Same distance
                tied_cells.append((i+i_addition[k], j+j_addition[k]))

    return min_dist, direction, neighbors, tied_cells



def walldetect(maze,compmaze, pos):
    '''update to detect walls simulation style'''
    i,j=pos
    i_add = [1,0,-1,0]
    j_add = [0,-1,0,1]
    # Adding apropiate walls to surrounding cells
    for k in range(4):
        #Make sure we dont go over the edge
        if i+i_add[k]<0 or i+i_add[k]>=height or j+j_add[k]<0 or j+j_add[k]>=width:
            continue
        maze[i+i_add[k]][j+j_add[k]][1] |= (compmaze[i+i_add[k]][j+j_add[k]][1] & 2**k)
    #Setting wall for current cell
    maze[i][j][1] = compmaze[i][j][1] 



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
        minDist, _, neighbors, _ = get_min_neighbors(maze, currentCell)
        if minDist+1 < get_distance(maze, currentCell):
            set_distance(maze, currentCell, minDist+1)
            stack.extend(neighbors)

    return

def backtrack(maze, pos, path):
    if len(path) == 0:
        return None, pos, None
    neighbors = []
    i_addition = [-1, 0, 1, 0]
    j_addition = [0, 1, 0, -1]
    while len(neighbors) == 0 and len(path) != 0:
        direction = path.pop(-1)
        pos = (pos[0]-i_addition[direction], pos[1]-j_addition[direction])
        minDist, new_direction, neighbors, tied_cell = get_min_neighbors(maze, pos, ignoreVisited=True)
        print_maze(maze, pos)
        sleep(1)
    
    return new_direction, pos, tied_cell


def floodfill(maze, solution, pos, target):
    i_addition = [-1, 0, 1, 0]
    j_addition = [0, 1, 0, -1]

    set_target(maze, target)
    
    path = []
    unexplored = []

    while pos != target:
        #Read walls at current position from solution
        walldetect(maze, solution, pos)

        #set current position to visited
        set_visited(maze, pos)

        #Update the maze to reflect the walls of the current cell
        update(pos, maze)
        #Find the next cell to move to
        _, direction, neighbors, tied_cells = get_min_neighbors(maze, pos, ignoreVisited=True)

        if len(neighbors) == 0:
            direction, pos, tied_cells = backtrack(maze, pos, path)
            if len(path) == 0: #If we cant go back, we are done
                break

        unexplored.extend(tied_cells) #cells that may lead to better path

        #Move to the next cell
        pos = (pos[0]+i_addition[direction], pos[1]+j_addition[direction])
        #add direction to path
        path.append(direction)
        print_maze(maze, pos)
        sleep(1)

    return pos, unexplored


def move_to_target(maze, pos, target):
    i_addition = [-1, 0, 1, 0]
    j_addition = [0, 1, 0, -1]
    set_target(maze, target)
    while pos != target:

        _, direction, _, _ = get_min_neighbors(maze, pos, ignoreVisited=False)

        pos = (pos[0]+i_addition[direction], pos[1]+j_addition[direction])

        print_maze(maze, pos)
        sleep(1)
    return pos



if __name__ == "__main__":

    solution = create_maze(height, width)
    read_maze(solution, "maze1.txt")

    maze = create_maze(height, width)
    target = (height-1, width-1)

    pos = (0,0)

    pos, unexplored = floodfill(maze, solution, pos, target)

    while unexplored != []:
        #Get to unexplored cell
        current_cell = unexplored.pop(0)
        _, direction, neighbors, tied_cells = get_min_neighbors(maze, current_cell, ignoreVisited=True)
        if len(neighbors) != 0:
            pos = move_to_target(maze, pos, current_cell)
            pos, tmp = floodfill(maze, solution, pos, target)
            unexplored.extend(tmp)


