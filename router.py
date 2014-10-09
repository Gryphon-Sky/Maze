import mazes

# helpers

left = dict(S = 'E', N = 'W', E = 'N', W = 'S')
right = dict(S = 'W', N = 'E', E = 'S', W = 'N')

def replace_at(str, i, c):
    return str[:i] + c + str[(i + 1):]
    
def check_forward(p, d, maze):
    cell = get_next_cell(p, d)
    return not mazes.is_wall(cell[0], cell[1], maze)

def check_right(p, d, maze):
    direction = right[d]
    return check_forward(p, direction, maze)

def get_next_cell(p, d):
    s = mazes.step[d]
    return (p[0] + s[0], p[1] + s[1])

def move(p, d, maze, crumbs):
    cell = get_next_cell(p, d)
    if crumbs and p != mazes.get_start(maze):
        maze[p[0]] = replace_at(maze[p[0]], p[1], d)
    return cell

# main methods
    
def prepare_maze(maze):
    # filling form
    max_len = max([len(row) for row in maze])
    for i, row in enumerate(maze):
        if len(row) < max_len:
            maze[i] += "X" * (max_len - len(row))
            
    # surrounding by walls
    for i, row in enumerate(maze):
        maze[i] = "X" + row + "X"
    
    width = max_len + 2
    horizontal_wall = "X" * width
    maze.insert(0, horizontal_wall)
    maze.append(horizontal_wall)

def choose_direction(p, maze):
    # we are using right-handed method,
    # so the wall must be to right of us in the beginning
    d = 'N'
    while check_right(p, d, maze):
        d = right[d]
    return d
    
def find_route(name, maze, crumbs):
    prepare_maze(maze)
    
    p = mazes.get_start(maze)
    d = choose_direction(p, maze)
    
    result = ""

    while not mazes.is_finish(p[0], p[1], maze):
        if check_right(p, d, maze):
            # Move right
            d = right[d]
            p = move(p, d, maze, crumbs)
            result += d
        elif check_forward(p, d, maze):
            # Move forward
            p = move(p, d, maze, crumbs)
            result += d
        else:
            # Turn left
            d = left[d]

    if crumbs:
        mazes.print_maze((name, maze))
            
    return result