from time import sleep
from maze import *


# This function will set visited to true
def set_visited(maze, cell):
    '''
    Sets the visited state of a cell in a maze to True.
    
    Arguments:
        maze: the maze to be used
        cell: tuple of the cell to be checked
    '''
    
    i, j = cell
    maze[i][j]["visited"] = True


# This function will set visited to false
def set_unvisited(maze, cell):
    '''
    Sets the visited state of a cell in a maze to False.
    
    Arguments:
        maze: the maze to be used
        cell: tuple of the cell to be checked
    '''
    
    i, j = cell
    maze[i][j]["visited"] = False


def set_distance(maze, cell, new_distance):
    '''
    Sets the distance of a cell in a maze.
    
    Arguments:
        maze: the maze to be used
        cell: tuple of the cell to be checked
        new_distance: the new distance to be set to
    '''
    
    i, j = cell
    maze[i][j]["distance"] = new_distance


def get_distance(maze, cell): 
    '''
    Gets the distance of a cell in a maze.
    
    Arguments:
        maze: the maze to be used
        cell: tuple of the cell to be checked
    '''
    
    i, j = cell
    return maze[i][j]["distance"]


def clear_visited(maze):
    '''
    Sets each cell's visited state to False.
    
    Arguments:
        maze: the maze to clear
    '''
    
    for i in range(height):
        for j in range(width):
            set_unvisited(maze, (i, j))


def create_target_squares(micromouse_maze):
    '''
    Creates a set of target squares from a given maze.
    
    Arguments:
        micromouse_maze: the maze to create target squares from
    Returns:
        target_squares: a list of target_squares of the input maze.
    '''
    height = len(micromouse_maze)
    width = len(micromouse_maze[0])
    
    target_squares = [(height//2, width//2), (height//2-1, width//2),
                      (height//2-1, width//2-1), (height//2, width//2-1)]
    return target_squares


def set_target_squares(maze, target_squares):
    '''
    Sets the target square distances of a maze to 0.
    
    Arguments:
        maze: the maze to set distances to 0.
        target_squares: list of the target squares of the maze.
    '''
    
    for target_cell in target_squares:
        i, j = target_cell
        maze[i][j]["distance"] = 0


def set_cell_distances(maze):
    '''
    Sets the target squares to have distance 0
    and recalculates the distance for every other
    cell in the maze, taking into account walls of the maze.

    Arguments:
        maze: the maze to set cell distances.
    '''
    
    #Setting all cells to have large distance
    for i in range(height):
        for j in range(width):
            maze[i][j]["distance"] = 5000

    # Creating target squares of the maze
    target_squares = create_target_squares(maze)
    
    # Setting the target squares to have distance 0
    set_target_squares(maze, target_squares)
    
    # Starting the stack, will hold tuples of indices of target cells
    stack = []
    stack = stack.extend(target_squares)

    while len(stack) != 0:
        cell = stack.pop(-1)
            
        neighbors = get_neighbors(maze, cell)
        
        #minDist is the minimum distance of the neighbors (in Manhattan distance)
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
    '''
    Gets the neighbors of a specified cell.

    Arguments:
        maze: the maze containing the cell.
        cell: tuple containing indices of the cell
    Returns:
        neighbors: list of the cell's neighbors.
    '''
    
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


def get_minimum_of_neighbors(maze, current_cell):
    '''
    Gets the neighbor of a specified cell with the smallest distance.

    Arguments:
        maze: the maze containing the cell.
        current_cell: tuple containing indices of the current cell
    Returns:
        minimum_distance: the smallest distance of the minimum neighbor.
        minimum_distance_cell: tuple of the neighbor with smallest distance.
    '''
    
    i, j = current_cell
    minimum_distance = get_distance(current_cell)
    minimum_distance_cell = current_cell
    
    neighbors = get_neighbors(maze, current_cell)
    
    for neighbor in neighbors:
        if get_distance(neighbor) < minimum_distance:
            minimum_distance = get_distance(neighbor)
            minimum_distance_cell = neighbor
            
    return minimum_distance, minimum_distance_cell


def floodfill(maze):
    queue = []
    
    while len(queue) != 0:
        cell = queue.pop(0)
        min_dist, min_dist_cell = get_minimum_of_neighbors(maze, cell)
        
        if get_distance(cell) < min_dist:
            set_distance()
        
        


if __name__ == "__main__":
    testMaze = create_maze(height, width)
    set_cell_distances(testMaze)
    print_maze(testMaze)
    
    # solution = create_maze(height, width)
    # read_maze(solution, "maze1.txt")

    # maze = create_maze(height, width)
