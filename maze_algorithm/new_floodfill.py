from time import sleep
from maze import *


# This function will set visited to true
def set_visited(maze, cell):
    i, j = cell
    maze[i][j]["visited"] = True


# This function will set visited to false
def set_unvisited(maze, cell):
    i, j = cell
    maze[i][j]["visited"] = False


def set_distance(maze, cell, dist):
    i, j = cell
    maze[i][j]["distance"] = dist


def get_distance(maze, cell):
    i, j = cell
    return maze[i][j]["distance"]


def clear_visited(maze):
    for i in range(height):
        for j in range(width):
            set_unvisited(maze, (i, j))


def create_target_squares():
    target_squares = [(height//2, width//2), (height//2-1, width//2),
                      (height//2-1, width//2-1), (height//2, width//2-1)]
    return target_squares


def set_target_squares(maze, target_squares):
    for targetCell in target_squares:
        i, j = targetCell
        maze[i][j]["distance"] = 0
        
        
def create_stack_with_targets(target_squares):
    stack = []
    for targetCell in target_squares:
        stack.append(targetCell)
    return stack


def set_cell_distances(maze):
    '''
    Sets the target cell to have distance 0
    and recalculates the distance for every other
    cell in the maze, taking into account walls

    Parameters:
    maze: the maze
    target: tuple indecies of the target cell
    '''
    #Setting all cells to have large distance
    for i in range(height):
        for j in range(width):
            maze[i][j]["distance"] = 5000

    # Creating target squares of the maze
    target_squares = create_target_squares()
    
    # Setting the target squares to have distance 0
    set_target_squares(maze, target_squares)
    
    # Starting the stack, will hold tuples of indecies of target cells
    stack = create_stack_with_targets(target_squares)

    while len(stack) != 0:
        cell = stack.pop(-1)
            
        neighbors = get_neighbors(maze, cell)
        #minDist is the minimum distance of the neighbors
        minDist = get_distance(maze, cell)+1
        for neighbor in neighbors:
            #If the neighbor has a distance larger than the current cell + 1
            if (get_distance(maze, neighbor) == 0): 
                continue
            else:
                if get_distance(maze, neighbor) > minDist:
                    #Then set the distance to the current cell + 1, and add neighbor to stack
                    set_distance(maze, neighbor, minDist)
                    stack.append(neighbor)


def get_neighbors(maze, cell):
    i, j = cell
    neighbors = []
    row_cells = [-1, 0, 1, 0]
    col_cells = [0, 1, 0, -1]
    
    for k in range(4):
        # If the walls value contains a specific bit (ex: 2, North)
        if maze[i][j]["walls"] & 2**k:
            #Wall
            continue
        else:
            #Open
            neighbors.append((i+row_cells[k], j+col_cells[k]))

    return neighbors


if __name__ == "__main__":
    testMaze = create_maze(height, width)
    set_cell_distances(testMaze)
    print_maze(testMaze)
    
    # solution = create_maze(height, width)
    # read_maze(solution, "maze1.txt")

    # maze = create_maze(height, width)
