#For testing Bresenham algorithm implementation.
# Permits instant adjusting of point positions and shows result.
# Uses curses to display.
import curses
import bresenham #File bresenham.py

#curses version of print_grid.
def print_grid(grid, screen):
    for y, ln in enumerate(grid):
        for x, ch in enumerate(ln):
            screen.addstr(y, x, ch)

def main(screen):
    key = ""
    point1 = [0,0]
    point2 = [8,8]
    while True:
        grid = [[' ' for x in range(0, curses.COLS)] for x in range(0,
            curses.LINES-1)]
        bresenham.bresenham(point1, point2, grid)
        screen.clear()
        print_grid(grid, screen)
        screen.addstr(curses.LINES-1, 0, "A"+str(point1)+" B"+str(point2))
        key = screen.getkey()
        if key=="w" and point1[1]>0:
            point1[1] -= 1
        elif key=="s" and point1[1]<curses.LINES-2:
            point1[1] += 1
        elif key=="a" and point1[0]>0:
            point1[0] -= 1
        elif key=="d" and point1[0]<curses.COLS-1:
            point1[0] += 1
        elif key=="KEY_UP" and point2[1]>0:
            point2[1] -= 1
        elif key=="KEY_DOWN" and point2[1]<curses.LINES-2:
            point2[1] += 1
        elif key=="KEY_LEFT" and point2[0]>0:
            point2[0] -= 1
        elif key=="KEY_RIGHT" and point2[0]<curses.COLS-1:
            point2[0] += 1
        elif key=="q":
            break

curses.wrapper(main)
