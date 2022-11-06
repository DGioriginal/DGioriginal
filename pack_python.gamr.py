from tkinter import Tk, Button
from PIL import ImageTk
from tkinter import *
from time import sleep
import pygame
from random import choice, random, randrange
from turtle import *
from math import *
from freegames import floor, vector, square
import tkinter
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter.filedialog import *
from time import sleep
from random import randint
from tkinter import scrolledtext
whiler = True
def strike_ball():
    ball = vector(-200, -200)
    speed = vector(0, 0)
    score=0
    targets = []        

    def tap(x, y):
        if not inside(ball):
            ball.x = -199
            ball.y = -199
            speed.x = (x + 200) / 25
            speed.y = (y + 200) / 25


    def inside(xy):
        return -200 < xy.x < 200 and -200 < xy.y < 200


    def draw():
        clear()

        for target in targets:
            goto(target.x, target.y)
            dot(20, 'black')

        if inside(ball):
            goto(ball.x, ball.y)
            dot(10, 'red')

        update()


    def move():
        if randrange(40) == 0:
            y = randrange(-150, 150)
            target = vector(200, y)
            targets.append(target)

        for target in targets:
            target.x -= 0.5

        if inside(ball):
            speed.y -= 0.35
            ball.move(speed)

        dupe = targets.copy()
        targets.clear()

        for target in dupe:
            if abs(target - ball) > 13:
                targets.append(target)

        draw()

        for target in targets:
            if not inside(target):
                return

        ontimer(move, 50)


    setup(420, 420, 370, 0)
    hideturtle()
    up()
    tracer(False)
    onscreenclick(tap)
    move()
    done()


def tron_twopl():
    p1xy = vector(-100, 0)
    p1aim = vector(4, 0)
    p1body = set()

    p2xy = vector(100, 0)
    p2aim = vector(-4, 0)
    p2body = set()


    def inside(head):
        return -200 < head.x < 200 and -200 < head.y < 200


    def draw():
        p1xy.move(p1aim)
        p1head = p1xy.copy()

        p2xy.move(p2aim)
        p2head = p2xy.copy()

        if not inside(p1head) or p1head in p2body:
            print('Player blue wins!')
            return

        if not inside(p2head) or p2head in p1body:
            print('Player red wins!')
            return

        p1body.add(p1head)
        p2body.add(p2head)

        square(p1xy.x, p1xy.y, 3, 'red')
        square(p2xy.x, p2xy.y, 3, 'blue')
        update()
        ontimer(draw, 50)


    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: p1aim.rotate(90), 'a')
    onkey(lambda: p1aim.rotate(-90), 'd')
    onkey(lambda: p2aim.rotate(90), 'Left')
    onkey(lambda: p2aim.rotate(-90), 'Right')
    draw()
    done()



def ping_pong():
    def value():
        return (3 + random() * 2) * choice([1, -1])


    
    ball = vector(0, 0)
    aim = vector(value(), value())
    state = {1: 0, 2: 0}


    def move(player, change):
        state[player] += change


    def rectangle(x, y, width, height):
        up()
        goto(x, y)
        down()
        begin_fill()
        for count in range(2):
            forward(width)
            left(90)
            forward(height)
            left(90)
        end_fill()


    def draw():
        clear()
        rectangle(-200, state[1], 10, 50)
        rectangle(190, state[2], 10, 50)

        ball.move(aim)
        x = ball.x
        y = ball.y

        up()
        goto(x, y)
        dot(10)
        update()

        if y < -200 or y > 200:
            aim.y = -aim.y

        if x < -185:
            low = state[1]
            high = state[1] + 100

            if low <= y <= high:
                aim.x = -aim.x
            else:
                return

        if x > 185:
            low = state[2]
            high = state[2] + 100

            if low <= y <= high:
                aim.x = -aim.x
            else:
                return

        ontimer(draw, 50)


    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: move(1, 25), 'w')
    onkey(lambda: move(1, -25), 's')
    onkey(lambda: move(2, 20), 'Up')
    onkey(lambda: move(2, -20), 'Down')
    draw()
    done()


def simon_sayss():
    pattern = []
    guesses = []
    tiles = {
        vector(0, 0): ('red', 'dark red'),
        vector(0, -200): ('blue', 'dark blue'),
        vector(-200, 0): ('green', 'dark green'),
        vector(-200, -200): ('yellow', 'khaki'),
    }


    def grid():
        square(0, 0, 200, 'dark red')
        square(0, -200, 200, 'dark blue')
        square(-200, 0, 200, 'dark green')
        square(-200, -200, 200, 'khaki')
        update()


    def flash(tile):
        glow, dark = tiles[tile]
        square(tile.x, tile.y, 200, glow)
        update()
        sleep(0.5)
        square(tile.x, tile.y, 200, dark)
        update()
        sleep(0.5)


    def grow():
        tile = choice(list(tiles))
        pattern.append(tile)

        for tile in pattern:
            flash(tile)

        print('Pattern length:', len(pattern))
        guesses.clear()


    def tap(x, y):
        onscreenclick(None)
        x = floor(x, 200)
        y = floor(y, 200)
        tile = vector(x, y)
        index = len(guesses)

        if tile != pattern[index]:
            exit()

        guesses.append(tile)
        flash(tile)

        if len(guesses) == len(pattern):
            grow()

        onscreenclick(tap)


    def start(x, y):
        grow()
        onscreenclick(tap)


    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    grid()
    onscreenclick(start)
    done()

def pacman_game():

    state = {'score': 0}
    path = Turtle(visible=False)
    writer = Turtle(visible=False)
    aim = vector(5, 0)
    pacman = vector(-40, -80)
    ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
    ]
    tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]

    def square(x, y):
        path.up()
        path.goto(x, y)
        path.down()
        path.begin_fill()

        for count in range(4):
            path.forward(20)
            path.left(90)

        path.end_fill()


    def offset(point):
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index


    def valid(point):
        index = offset(point)

        if tiles[index] == 0:
            return False

        index = offset(point + 19)

        if tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0


    def world():
        bgcolor('black')
        path.color('blue')

        for index in range(len(tiles)):
            tile = tiles[index]

            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

                if tile == 1:
                    path.up()
                    path.goto(x + 10, y + 10)
                    path.dot(2, 'white')


    def move():
        writer.undo()
        writer.write(state['score'])

        clear()

        if valid(pacman + aim):
            pacman.move(aim)

        index = offset(pacman)

        if tiles[index] == 1:
            tiles[index] = 2
            state['score'] += 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

        up()
        goto(pacman.x + 10, pacman.y + 10)
        dot(20, 'yellow')

        for point, course in ghosts:
           if valid(point + course):
                point.move(course)
                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'red')
           else:
                options = [
                    vector(5, 0),
                    vector(-5, 0),
                    vector(0, 5),
                    vector(0, -5),
                ]
                plan = choice(options)
                course.x = plan.x
                course.y = plan.y

        update()

        for point, course in ghosts:
            if abs(pacman - point) < 20:
                return

        ontimer(move, 100)


    def change(x, y):
        if valid(pacman + vector(x, y)):
            aim.x = x
            aim.y = y


    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    writer.goto(160, 160)
    writer.color('white')
    writer.write(state['score'])
    listen()
    onkey(lambda: change(5, 0), 'd')
    onkey(lambda: change(-5, 0), 'a')
    onkey(lambda: change(0, 5), 'w')
    onkey(lambda: change(0, -5), 's')
    world()
    move()
    done()
window = Tk()
window.title('Pack Python-Game')
computer = Canvas(window, height = 900, width = 1200)
packman = ImageTk.PhotoImage(file="pacman.png")
pingg_pong = ImageTk.PhotoImage(file="ping_pong.png")
simon_says = ImageTk.PhotoImage(file="simon-says.png")
tron = ImageTk.PhotoImage(file="tron.png")
ballstrike= ImageTk.PhotoImage(file="ballstrike.png")
bt1= Button(computer, image=packman, command=pacman_game)
bt1.grid(column=0, row=50)
bt2 = Button(computer, image=pingg_pong, command=ping_pong)
bt2.grid(column=0, row=60)
bt3 = Button(computer, image=simon_says, command=simon_sayss)
bt3.grid(column=5, row=50)
bt4 = Button(computer, image=tron, command=tron_twopl)
bt4.grid(column=5, row=60)
bt5 = Button(computer, image=ballstrike, command=strike_ball)
bt5.grid(column=20, row=50)
computer.pack()
