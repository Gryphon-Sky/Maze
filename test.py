import mazes

def check(m):
    name = m[0]
    maze = m[1]
    
    start_found = False
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == '0' or cell == '1':
                assert i == 0 or i == (len(maze) - 1) or \
                       j == 0 or j == (len(row) - 1), \
                       name + ": start or end isn't on a edge!"
                if cell == '0':
                    assert not start_found, name + ": more then one start!"
                    start_found = True

import router

def check_route(maze, crumbs):
    #copy maze
    m = [row[:] for row in maze[1]]
    
    route = router.find_route(maze[0], m, crumbs)

    p = mazes.get_start(maze[1])

    for i, d in enumerate(route):
        move = mazes.step.get(d, None)
        if not move:
            print maze[0], ": Wrong symbol in route"
            return False
        p = p[0] + move[0], p[1] + move[1]
        if mazes.is_finish(p[0], p[1], maze[1]):
            return True
        if mazes.is_wall(p[0], p[1], maze[1]):
            print maze[0], ": Player faced the wall"
            return False
    print maze[0], ": Player did not reach exit"
    return False

def test(maze, crumbs):
    check(maze)
    check_route(maze, crumbs)

test(mazes.maze0, False)
test(mazes.maze1, False)
test(mazes.maze2, False)
test(mazes.maze3, False)
test(mazes.maze4, False)
test(mazes.maze5, False)
test(mazes.maze6, True)

print("The tests are done.")