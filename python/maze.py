import random
import matplotlib.pyplot as plt

def scale(k): return 2 * k + 1

def create_maze(rows, cols, plot=False):
    visited = [[0] * cols for i in range(rows)]
    maze = [[0] * scale(cols) for i in range(scale(rows))]

    # show walls
    #for y in range(scale(rows)):
    #    for x in range(scale(cols)):
    #        if y % 2 == 1 and x % 2 == 1:
    #            maze[y][x] = 1

    stack = []
    start_y, start_x = (random.randrange(rows), random.randrange(cols))
    stack.append((start_y, start_x, scale(start_y), scale(start_x)))
    maze[scale(start_y)][scale(start_x)] = 1

    if plot:
        fig, ax = plt.subplots()
        ax.set_title(f'{rows}x{cols} maze')
        ax.axis('off')
        plt.tight_layout()
        img = ax.imshow(maze, interpolation='nearest', cmap=plt.cm.nipy_spectral)

    while stack:
        y, x, y2, x2 = stack.pop() # DFS; pop(0) -> BFS

        if visited[y][x]:
            if plot:
                ax.set_title(f'{rows}x{cols} maze, stack size: {len(stack)}')
                img.set_data(maze)
                plt.pause(0.0001)
            continue

        maze[scale(y)][scale(x)] = maze[y2][x2] = 1
        visited[y][x] = 1

        if plot:
            ax.set_title(f'{rows}x{cols} maze, stack size: {len(stack)}')
            img.set_data(maze)
            plt.pause(0.01)

        neighbors = [(y, max(0, x-1)), (y, min(cols-1, x+1)), (max(0, y-1), x), (min(rows-1, y+1), x)]
        random.shuffle(neighbors)
        for (yn, xn) in neighbors:
            if visited[yn][xn]:
                continue
            y2, x2 = (scale(max(y, yn)) - 1, scale(x)) if xn == x else (scale(y), scale(max(x, xn)) - 1)
            stack.append((yn, xn, y2, x2))

    if plot:
        plt.savefig('maze-dfs-gen.pdf', bbox_inches='tight', pad_inches=0.0)
        plt.show()

    return maze


def solve_maze(maze, rows, cols, start, goal, plot=False):
    h, w = rows, cols
    start_y, start_x = start
    goal_y, goal_x = goal
    maze[scale(start_y)][scale(start_x)] = .25
    maze[scale(goal_y)][scale(goal_x)] = .25
    visited = set()

    if plot:
        fig, ax = plt.subplots()
        ax.set_title(f'{rows}x{cols} maze')
        ax.axis('off')
        plt.tight_layout()
        img = ax.imshow(maze, interpolation='nearest', cmap=plt.cm.nipy_spectral)

    stack = []
    stack.append((start_y, start_x, scale(start_y), scale(start_x)))

    while stack:
        y, x, y2, x2 = stack.pop() # DFS; pop(0) -> BFS
        if (y, x) in visited:
            continue
        maze[scale(y)][scale(x)] = maze[y2][x2] = .5
        visited.add((y, x))

        if plot:
            ax.set_title(f'{rows}x{cols} maze, stack size: {len(stack)}')
            img.set_data(maze)
            plt.pause(0.0001)

        neighbors = []
        if maze[scale(y)][scale(x) - 1] > 0: neighbors.append((y, max(0, x-1)))
        if maze[scale(y)][scale(x) + 1] > 0: neighbors.append((y, min(cols-1, x+1)))
        if maze[scale(y) - 1][scale(x)] > 0: neighbors.append((max(0, y-1), x))
        if maze[scale(y) + 1][scale(x)] > 0: neighbors.append((min(rows-1, y+1), x))
        random.shuffle(neighbors)
        for (yn, xn) in neighbors:
            if (yn, xn) in visited:
                continue
            if xn == goal_x and yn == goal_y:
                y2, x2 = (scale(max(y, yn)) - 1, scale(x)) if xn == x else (scale(y), scale(max(x, xn)) - 1)
                maze[y2][x2] = .5
                if plot:
                    ax.set_title(f'{rows}x{cols} maze, stack size: {len(stack)}')
                    img.set_data(maze)
                    plt.pause(0.0001)
                    plt.savefig('maze-dfs-solve.pdf', bbox_inches='tight', pad_inches=0.0)
                    plt.show()
                return

            y2, x2 = (scale(max(y, yn)) - 1, scale(x)) if xn == x else (scale(y), scale(max(x, xn)) - 1)
            stack.append((yn, xn, y2, x2))


maze = create_maze(10, 20, True)
solve_maze(maze, 10, 20, (0, 0), (9, 6), True)
