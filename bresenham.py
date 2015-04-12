#Implementation of Bresenham's algorithm for rendering straight lines.
# Places rendered 'pixels' on a grid provided (assumes all needed coordinates exist).
def y_bresenham(point1, point2, grid):
    if point1[1]>point2[1]:
        tmp = point1
        point1 = point2
        point2 = tmp
    dx = point2[0]-point1[0]
    dy = point2[1]-point1[1]
    assert(dy>abs(dx))
    x = point1[0]
    error = 0
    if dx>=0:
        for y in range(point1[1], point2[1]+1):
            grid[y][x] = "#"
            error += dx
            if error*2 >= dy:
                error -= dy
                x += 1
    else:
        for y in range(point1[1], point2[1]+1):
            grid[y][x] = "#"
            error += dx
            if error*2 <= -dy:
                error += dy
                x -= 1
def x_bresenham(point1, point2, grid):
    if point1[0]>point2[0]:
        tmp = point1
        point1 = point2
        point2 = tmp
    dx = point2[0]-point1[0]
    dy = point2[1]-point1[1]
    assert(dy<=dx)
    y = point1[1]
    error = 0
    if dy>=0:
        for x in range(point1[0], point2[0]+1):
            grid[y][x] = "#"
            error += dy
            if error*2 >= dx:
                error -= dx
                y += 1
    if dy<0:
        for x in range(point1[0], point2[0]+1):
            grid[y][x] = "#"
            error += dy
            if error*2 <= -dx:
                error += dx
                y -= 1

def bresenham(point1, point2, grid):
    if abs(point1[1]-point2[1])>abs(point1[0]-point2[0]):
        y_bresenham(point1, point2, grid)
    else:
        x_bresenham(point1, point2, grid)

#Testing...
def print_grid(grid):
    for ln in grid:
        for ch in ln:
            print(ch, end='')
        print()

if __name__=="__main__":
    grid = [[' ' for x in range(0, 9)] for x in range(0, 9)]
    bresenham([0, 0], [8,8], grid)
    bresenham([0, 8], [8,0], grid)
    bresenham([0, 5], [8,3], grid)
    bresenham([8, 5], [0,3], grid)
    print_grid(grid)
