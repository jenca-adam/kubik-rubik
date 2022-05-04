import curses
from rubik._backend import *
from rubik._backend.helpers.ctrl import *
from rubik._backend.helpers.string import switch
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
    display_face(cube[5],8,0,screen)
    display_face(np.rot90(np.transpose(cube[1])),8,4,screen)
    display_face(cube[0],8,8,screen)
    display_face(np.rot90(cube[2],3),4,8,screen)
    display_face(np.rot90(cube[3]),12,8,screen)
    display_face(cube[4],8,12,screen)

# does the real thing
def wrap(screen):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    for color in COLORS.values():
        curses.init_pair(color, color, -1)
    cube = Cube()
    moves=0
    last=''
    while True:
        display(cube,screen)
        screen.addstr(16,0,f"Moves: {moves}; Last: {last}")
        char = screen.getch()
        if char == 32:
            cube.scramble()
        if char == 27:
            screen.clear()
            return
        last=switch(char,transs)
        if last:
            moves+=1
            cube.transform(last)
        else:
            try: 
                k = CtrlKey(chr(char))
            except:
                continue
            if k.xc in transs:
                cube.transform(k.xc+"'")


#Just a wrapper for wrap()
def main(): 
    curses.wrapper(wrap)
