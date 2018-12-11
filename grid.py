import collections

class DenseGrid(object):
    def __init__(self, width=None, height=None, mx=None, my=None, default='.'):
        self.width = width
        self.height = height
        self.mx = mx
        self.my = my
        if self.width:
            self.grid = [
                [default]*self.width
                for _ in range(self.height)
            ]
        else:
            self.grid = []
        self.default = default

    def __setitem__(self, xy, c):
        if self.width is None:
            self.grid = [[c]]
            self.width = 1
            self.height = 1
            self.mx, self.my = xy
            return
        sx, sy = xy

        if (sx < self.mx or sy < self.my or sx >= self.mx + self.width
            or sy >= self.my + self.height):
            mx = min(sx, self.mx)
            my = min(sy, self.my)
            width = max(sx+1, self.mx+self.width) - mx
            height = max(sy+1, self.my+self.height) - my
            grid = [['.'] * width for _ in range(height)]
            for x in range(self.mx, self.mx+self.width):
                for y in range(self.my, self.my+self.height):
                    grid[y-my][x-mx] = self.grid[y-self.my][x-self.mx]
            self.grid = grid
            self.mx = mx
            self.my = my
            self.width = width
            self.height = height

        self.grid[sy-self.my][sx-self.mx] = c

    def __getitem__(self, xy):
        x, y = xy
        if (x < self.mx or y < self.my
            or x > self.mx + self.width
            or y > self.my + self.height):
            return self.default
        return self.grid[y-self.my][x-self.mx]

    def xrange(self):
        return range(self.mx, self.mx+self.width)

    def yrange(self):
        return range(self.my, self.my+self.height)

    def range(self):
        return (
            (x, y)
            for x in self.xrange()
            for y in self.yrange()
        )

    def __str__(self):
        return '\n'.join(''.join(map(str, c)) for c in self.grid)

class SparseGrid(object):
    def __init__(self, d=None, default='.'):
        self.grid = d or {}
        self.default = default

    def __setitem__(self, xy, c):
        self.grid[xy] = c

    def __str__(self):
        if not self.grid:
            return ''
        return '\n'.join(
            ''.join(
                self.grid.get((x,y), self.default)
                for x in self.xrange()
            )
            for y in self.yrange()
        )

    def xrange(self):
        minx = min(x for x, _ in self.grid.keys())
        maxx = max(x for x, _ in self.grid.keys())
        return range(minx, maxx+1)

    def yrange(self):
        miny = min(y for _, y in self.grid.keys())
        maxy = max(y for _, y in self.grid.keys())
        return range(miny, maxy+1)

    def bounds(self):
        minx = min(x for x, _ in self.grid.keys())
        maxx = max(x for x, _ in self.grid.keys())
        miny = min(y for _, y in self.grid.keys())
        maxy = max(y for _, y in self.grid.keys())
        return (minx, miny), (maxx, maxy)

    def area(self):
        (ax, ay), (bx, by) = self.bounds()
        return (bx+1-ax)*(by+1-ay)

    def count(self):
        return collections.Counter(self.grid.values())
