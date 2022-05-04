import curses
from rubik._backend import *
COLORS = { 'o' : 202,
           'y' : 11,
           'w' :15,
           'r' : 196,
           'b' :21,
           'g' : 46,
           }

def display_face(face,xoffset,yoffset,screen):
    for li,line in enumerate(face):
            for ci,char in enumerate(line):
                assert char in COLORS , f'unknown character : {char!r}'
                color = COLORS[char]
                screen.addstr(yoffset+li,xoffset+ci,char, curses.color_pair(color))
    screen.addstr(yoffset+li+1,0," "*9)
#calls display_face() with appopriate offset
def display(cube,screen):
    display_face(cube[5],3,0,screen)
    display_face(cube[1],3,4,screen)
    display_face(cube[0],3,8,screen)

# does the real thing
def wrap(screen):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    for color in COLORS.values():
        curses.init_pair(color, color, -1)
    cube = Cube()
    while True:
        display(cube,screen)
        char = screen.getch()
        cube.scramble()
#Just a wrapper for wrap()
def main(): 
    curses.wrapper(wrap)
