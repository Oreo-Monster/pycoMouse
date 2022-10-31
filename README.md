# pycoMouse

This is an open source Micromouse project.

# Build Guide

Instructions for building the mouse are provided [here](BuildGuide.md). 3D printed parts files will be add soon. 

# Code

mouse_library/ contains files needed to run the pyco mouse. Copy the directory into the pico storage and modify code to do what you want. If gp-16 is connected is pulled high on boot, the mouse will be in write mode, where files can be written to the internal storage. If not, the internal storage is read only. This will be useful if you want to log data during tests.

A library for controlling the mouse is provided in the mouse_library/code.py file. There are functions for moving forward, and turning left and right. As of now, the movements are not repeatable and the turns tend to go too far. 

# Maze Algorithm

We are using the floodfill algorithm to solve the maze. All code is in maze_algorithm. 
