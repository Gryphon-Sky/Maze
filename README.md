Maze

====

Script that finds a route through the maze.

Rules:
AI begins at certain point and trying to find an exit. If it smash into a wall, it lose. The maze is presented as a list of strings.
Legend: 'X' is a wall, ' ' is part of the path, '0' is the entry point and '1' is exit.
There must be one (and one only) entry point and at least one exit. They both must be on the edge of maze.

AI can move in only four directions — South (down (1,0)), North (up (-1,0)), East (right (0,1)), West (left (0, -1)). The route is described as a string consisting of different characters: 'S'=South, 'N'=North, 'E'=East, and 'W'=West. 

====

Written on Python 2.7.8
https://www.python.org/

Based on "Open Labyrinth" Check iO mission. Most mazes and main test are from there as well
http://www.checkio.org/mission/open-labyrinth/