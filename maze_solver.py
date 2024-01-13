import turtle
from collections import deque

def window_object():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Pac-Man Game")
    wn.setup(1300, 700)
    return wn

def maze():
    maze_turtle = turtle.Turtle()
    maze_turtle.shape("square")
    maze_turtle.color("white")
    maze_turtle.penup()
    maze_turtle.speed(0)
    return maze_turtle

def pacman():
    pacman_turtle = turtle.Turtle()
    pacman_turtle.shape("circle")
    pacman_turtle.color("yellow")
    pacman_turtle.penup()
    pacman_turtle.speed(2)
    return pacman_turtle

def food():
    food_turtle = turtle.Turtle()
    food_turtle.shape("square")
    food_turtle.color("red")
    food_turtle.penup()
    food_turtle.speed(0)
    return food_turtle

walls = []
path = []
food_positions = []  # New list to store food positions
start_x, start_y = 0, 0
end_x, end_y = 1, 1

grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+e              +                                 +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+                            +               ++   +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+   ++++  +  +++++++ ++++++++  +++++++++++++  ++  +",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ ++++ ++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ ++++++++++     ++          ++    ++++   +",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
]

def setup_maze(grid, maze_turtle, pacman_turtle):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze_turtle.goto(screen_x, screen_y)
                maze_turtle.stamp()
                walls.append((screen_x, screen_y))

            if character == "e":
                pacman_turtle.goto(screen_x, screen_y)
                start_x, start_y = screen_x, screen_y

            if character == " " or character == "e":
                path.append((screen_x, screen_y))



def draw_path(path, pacman_turtle):
    pacman_turtle.penup()
    pacman_turtle.color("yellow")
    for x, y in path:
        pacman_turtle.goto(x, y)
        pacman_turtle.stamp()
        


def bfs(maze, start, end):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        x, y = current
        neighbors = [(x + 24, y), (x - 24, y), (x, y + 24), (x, y - 24)]

        for neighbor in neighbors:
            if neighbor in maze and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    return None



if __name__ == "__main__":
    wn = window_object()
    maze_turtle = maze()
    pacman_turtle = pacman()
    setup_maze(grid, maze_turtle, pacman_turtle,)
    start = (start_x, start_y)
    end = (end_x, end_y)
    solution = bfs(path, start, (588, -264))
    if solution:
        draw_path(solution, pacman_turtle)
        wn.exitonclick()

    turtle.done()