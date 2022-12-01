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

    # Setting all cells to have large distance
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

        # minDist is the minimum distance of the neighbors (in Manhattan distance)
        minDist = get_distance(maze, cell)+1

        for neighbor in neighbors:
            # If the neighbor has a distance larger than the current cell + 1
            if (get_distance(maze, neighbor) == 0):
                continue
            else:
                if get_distance(maze, neighbor) > minDist:
                    # Then set the distance to the current cell + 1, and add neighbor to stack
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
    horizontal_direction = [-1, 0, 1, 0]
    vertical_direction = [0, 1, 0, -1]

    for k in range(4):
        # If the walls value contains a specific bit (ex: 2, North)
        if maze[i][j]["walls"] & 2**k:
            # Wall
            continue
        else:
            # Open
            neighbors.append(
                (i+horizontal_direction[k], j+vertical_direction[k]))

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

    minimum_distance = get_distance(maze, current_cell)
    minimum_distance_cell = current_cell

    neighbors = get_neighbors(maze, current_cell)

    for neighbor in neighbors:
        if get_distance(maze, neighbor) < minimum_distance:
            minimum_distance = get_distance(maze, neighbor)
            minimum_distance_cell = neighbor

    return minimum_distance, minimum_distance_cell

# TODO work on wall detection (update later when working with sensors to detect walls)
def wall_detection(maze, unexplored_maze, current_cell):
    '''
    Detects walls of the maze by using a base maze for the MM to explore,
    and an unexplored maze for the MM to store.
    
    Arguments:
        maze: the base maze that the MM explores
        unexplored_maze: the maze the robot stores
        current_cell: the current cell to detect walls at
    '''
    i, j = current_cell
    horizontal_direction = [1, 0, -1, 0]
    vertical_direction = [0, -1, 0, 1]
    
    # Adding apropiate walls to surrounding cells
    for k in range(4):
        #Make sure we dont go over the edge
        if i+horizontal_direction[k]<0 or i+horizontal_direction[k]>=height or j+vertical_direction[k]<0 or j+vertical_direction[k]>=width:
            continue
        unexplored_maze[i+horizontal_direction[k]][j+vertical_direction[k]]["walls"] |= (maze[i+horizontal_direction[k]][j+vertical_direction[k]]["walls"] & 2**k)
    #Setting wall for current cell
    unexplored_maze[i][j]["walls"] = maze[i][j]["walls"] 

    

def floodfill(maze, current_position, target_cells):
    queue = []
    queue.append(current_position)

    while current_position not in target_cells:
        _, min_dist_cell = get_minimum_of_neighbors(maze, cell)

        while len(queue) != 0:
            cell = queue.pop(0)
            min_dist, _ = get_minimum_of_neighbors(maze, cell)
            neighbors = get_neighbors(maze, cell)
            if get_distance(maze, cell) < min_dist:
                set_distance(maze, cell, get_distance(cell)+1)
                queue.append()
            else:
                continue

            print_maze(maze, current_position)


if __name__ == "__main__":
    # The maze itself
    test_maze = create_maze(height, width)
    read_maze(test_maze, "maze2.txt")
    
    unexplored_maze = create_maze(height, width)
    set_cell_distances(test_maze)
    print_maze(test_maze)

    # solution = create_maze(height, width)
    # read_maze(solution, "maze1.txt")

    # maze = create_maze(height, width)
