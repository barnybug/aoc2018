#!/usr/bin/env python

from collections import defaultdict
from itertools import count
import re

colours = {
    '#': (0, 0, 0),
    '|': (128, 128, 255),
    '~': (64, 64, 255),
    '.': (255, 255, 255),
}

def draw_image(grid):
    from PIL import Image
    xs = [x for x,y in grid.keys()]
    ys = [y for x,y in grid.keys()]
    mx = min(xs)
    my = min(ys)

    img = Image.new( 'RGB', (max(xs)-mx+1, max(ys)-my+1), "white")
    pixels = img.load()

    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # For every row
            pixels[i,j] = colours[grid[i+mx,j+my]]

    scale = 1
    img = img.resize((img.size[0]*scale, img.size[1]*scale), Image.NEAREST)
    img.save('x.png')

def create_grid(lines):
    grid = defaultdict(lambda: '.')
    for line in lines:
        m = re.match(r'x=(\d+), y=(\d+)..(\d+)', line)
        if m:
            x, y1, y2 = map(int, m.groups())
            for y in range(y1, y2+1):
                grid[x,y] = '#'
        else:
            m = re.match(r'y=(\d+), x=(\d+)..(\d+)', line)
            y, x1, x2 = map(int, m.groups())
            for x in range(x1, x2+1):
                grid[x,y] = '#'
    return grid

def inject(grid, x, y, bottom):
    queue = [(x,y)]
    while queue:
        x, y = queue.pop()
        # 'drip'
        while y <= bottom and grid[x,y+1] not in '#~':
            grid[x,y] = '|'
            y += 1
        if y > bottom:
            continue

        # trapped?
        right, left = None, None
        for i in count(x):
            grid[i,y] = '|'
            if grid[i+1,y] in '#~':
                right = i
                break
            if grid[i+1,y+1] not in '#~':
                br = (i+1, y)
                if grid[br] != '|' and br not in queue:
                    queue.append(br)
                    # draw_image(grid)
                break

        for i in count(x, -1):
            grid[i,y] = '|'
            if grid[i-1,y] in '#~':
                left = i
                break
            if grid[i-1,y+1] not in '#~':
                bl = (i-1, y)
                if grid[bl] != '|' and bl not in queue:
                    queue.append(bl)
                    # draw_image(grid)
                break

        if left and right:
            # trapped
            for i in range(left, right+1):
                grid[i, y] = '~'
            if (x, y-1) not in queue:
                queue.append((x, y-1))

    draw_image(grid)

def parts(filename):
    grid = create_grid(open(filename))
    my = min(y for _, y in grid.keys())
    bottom = max(y for _,y in grid.keys())
    inject(grid, 500, 1, bottom)

    part1 = sum(1 for (x, y), c in grid.items() if c in '|~' and y >= my)
    part2 = sum(1 for (x, y), c in grid.items() if c in '~')
    return part1, part2

def part1(filename):
    return parts(filename)[0]

def part2(filename):
    return parts(filename)[1]

if __name__ == '__main__':
    print(part1('input17.txt'))
    print(part2('input17.txt'))
