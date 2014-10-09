step = dict(S = (1, 0), N = (-1, 0), E = (0, 1), W = (0, -1))

def get_start(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if maze[i][j] == '0':
                return (i, j)

def is_finish(x, y, maze):
    return maze[x][y] == '1'

def is_wall(x, y, maze):
    return maze[x][y] == 'X'

def print_maze(m):
    print m[0]

    maze = m[1]
    s = ""
    decorations = {'0' : "o ", '1' : "O ", 'X' : "XX", ' ' : "  ",
                   'N' : " ^", 'S' : "v ", 'E' : " >", 'W' : "< "}
    for row in maze:
        for cell in row:
            s += decorations[cell]
        s += '\n'
    print s

maze0 = ("Minimal maze", (
    "01",))

maze1 = ("First maze", (
    "0         X",
    " XXXXXX XX",
    " X        ",
    " X XXXXXX ",
    " X X      ",
    "   XX XXX ",
    " X    X XX",
    " XX X     ",
    " X  XXXXX ",
    "   XX    1"))

maze2 = ("Empty maze", (
    "0         ",
    "          ",
    "          ",
    "          ",
    "          ",
    "         1"))

maze3 = ("Up and down maze", (
    "0X   X    ",
    " X X X XX ",
    " X X X X  ",
    " X X X X X",
    " X X X X  ",
    " X X X XX ",
    " X X X X  ",
    " X X X X X",
    " X X X X  ",
    "   X   XX1"))

maze4 = ("Dotted maze", (
    "0  X   X  ",
    " X   X   X",
    "   X   X  ",
    " X   X   X",
    "   X   X  ",
    " X   X   X",
    "   X   X  ",
    " X   X   X",
    "   X   X  ",
    " X   X   1"))

maze5 = ("Need left maze", (
    "0   X     ",
    " XX X XXX ",
    " XX X X X ",
    "      XXX ",
    "XXXXX X   ",
    "    XXX XX",
    " XX       ",
    " XX XXXXX ",
    "        XX",
    " X X XX  1"))

maze6 = ("The big dead end", (
    "0         ",
    "XX XXXX XX",
    "          ",
    " XXX XXXXX",
    "  X       ",
    "X XXXXXX X",
    "     X    ",
    "XXXX X  X ",
    "     XXXXX",
    " XXX     1"))