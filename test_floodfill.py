from floodfill import *


def test_maze():
    height = 5
    width = 10
    maze = create_maze(height=height, width=width)
    assert len(maze) == height
    for row in maze:
        assert len(row) == width
        for cell in row:
            assert len(cell) == 2
    
    width = 10
    maze = create_maze(height=height, width=width)
    add_wall(maze, 0, 0, "NORTH")
    add_wall(maze, 0, 0, "EAST")
    add_wall(maze, 0, 0, "SOUTH")
    add_wall(maze, 0, 0, "WEST")
    assert maze[0][0][1] == 15
    set_visited(maze, 0, 0)
    assert maze[0][0][1] == 31
    set_unvisited(maze, 0, 0)
    assert maze[0][0][1] == 15
    walls = decode_walls(maze, 0, 0)
    assert walls == ["NORTH", "EAST", "SOUTH", "WEST"]