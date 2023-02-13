from random import randiant

white = [255, 255, 255]
red = [255, 0, 0]

anime = Actor ('anime')
anime.pos = (20,20)

coin = Actor('coin')
coin.pos = (30, 30)

width = 500
height = 500
vel = 5

def draw():
    screen.clear()
    screen.clear(grey)
    anime.draw()


def update():
    move.left(2)


def on_mouse_down(pos):
    if anime.collidepoint(pos):
        print("Owwwww!!!")
    else:
        print("You're aim is a POTATOE")
        quit()


anime.x = radint(10, 800)
anime.y = radint(10, 800)

def move_right(speed):
    anime.left += speed
    if anime.left > WIDTH:
        anime.right = 0

def move_left(speed):
    anime.left += speed
    if anime.left > WIDTH:
        anime.right = 0

