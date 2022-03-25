#Implemntation of Flood Fill algorrim for 
#solving maze

#Storing the maze in a 2D numpy array
import enum
import numpy as np

height, width = 11, 11
maze = np.zeros((height, width,2), dtype=int)

#Each cell will store a visited boolean and a distance to target cell

#Fill the maze with distances, where the target in the middle is 0
for i in range(height):
    for j in range(width):
        if i == height//2 and j == width//2:
            maze[i][j][0] = 0
        else:
            #calc number of steps to target
            maze[i][j][0] = abs(i-height//2) + abs(j-width//2)

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

def decode_walls(maze, i, j):
    walls = []
    #Check north 
    if maze[i][j][1] & 1:
        walls.append("NORTH")
    #Check east wall
    if maze[i][j][1] & 2:
        walls.append("EAST")
    #Check south wall
    if maze[i][j][1] & 4:
        walls.append("SOUTH")
    #Check west wall
    if maze[i][j][1] & 8:
        walls.append("WEST")
    return walls

#The fifth bit is the visited boolean
#If the cell has been visited, set to 1
#If the cell has not been visited, set to 0
#This function will set the visited boolean to 1
def set_visited(maze, i, j):
    maze[i][j][1] |= 16

#This function will set cell to not visited
def set_unvisited(maze, i, j):
    maze[i][j][1] &= ~16


#Check for each wall if there is a wall there
#If not, set a temp distance to the adjecent open cell
#If there is a wall, set the distance to infinity
#return the minimum distance
def get_distance_to_target(maze, i, j):
    dist = np.array[(4)]
    i_addition = [-1, 0, 1, 0]
    j_addition = [0, -1, 0, 1]
    for k in range(4):
        if maze[i][j][1] & 2**k:
            #Wall
            dist[k] = np.inf
        else:
            #Open
            dist[k] = maze[i+i_addition[k]][j+j_addition[k]][0]+1
    return np.min(dist)
    
    




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
                ToplineSTR += " ---"
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
        
        print(ToplineSTR)
        print(BottomLineSTR)

#Walls are represented in maze[i][j][1], with the following code
#We will conside the first 4 bits of the integer to represent the walls
#0 for no wall, 1 for wall
#first bit is north wall
#second bit is east wall
#third bit is south wall
#fourth bit is west wall
#This function will place random walls
def randomWalls(maze):
    for i in range(height):
        for j in range(width):
            maze[i][j][1] = np.random.randint(0,16)
            if i == 0 or i == height-1:
                maze[i][j][1] |= 1
            if j == 0 or j == width-1:
                maze[i][j][1] |= 8
            






print_maze(maze)