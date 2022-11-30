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
        maze[i][j] = 0


def set_cell_distances(maze):
    for i in range(height):
        for j in range(width):
            maze[i][j]["distance"] = 400

    target_squares = create_target_squares()
    set_target_squares(maze, target_squares)

    stack = []
    for target_cell in target_squares:
        stack.append(target_cell)
        

    while len(stack) != 0:
        cell = stack.pop(-1)
        neighbors = get_neighbors(maze, cell)
        # minDist is the minimum distance of the neighbors
        minDist = get_distance(maze, cell)+1
        for neighbor in neighbors:
            k, l = neighbor
            if (maze[k][l]["distance"] == 0):
                continue
            else:
            # If the neighbor has a distance larger than the current cell distance + 1
                if get_distance(maze, neighbor) > minDist:
                    # Then set the distance to the current cell distance + 1, and add neighbor to stack
                    set_distance(maze, neighbor, minDist)
                    stack.append(neighbor)



def get_neighbors(maze, cell):
    i, j = cell
    neighbors = []
    row_cells = [-1, 0, 1, 0]
    col_cells = [0, 1, 0, -1]
    
    for k in range(4):
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
