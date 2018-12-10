import collections

from grid import DenseGrid, SparseGrid

def test_empty_grid():
    g = DenseGrid()
    assert str(g) == ''

def test_grid_set():
    g = DenseGrid()
    g[1,1] = 'A'
    assert str(g) == 'A'

    g[2,1] = 'B'
    assert str(g) == 'AB'
    
    g[2,2] = 'C'
    assert str(g) == 'AB\n.C'

    g[-1,1] = 'Z'
    assert str(g) == 'Z.AB\n...C'

def test_grid_set():
    g = SparseGrid()
    g[1,1] = 'A'
    assert str(g) == 'A'

    g[2,1] = 'B'
    assert str(g) == 'AB'
    
    g[2,2] = 'C'
    assert str(g) == 'AB\n.C'

    g[-1,1] = 'Z'
    assert str(g) == 'Z.AB\n...C'

def test_grid_area():
    g = SparseGrid()
    g[1,1] = 'A'
    assert g.area() == 1

    g[2,1] = 'B'
    assert g.area() == 2
    
    g[2,2] = 'C'
    assert g.area() == 4

    g[-1,1] = 'Z'
    assert g.area() == 8

def test_grid_count():
    g = SparseGrid()
    g[1,1] = 'A'
    g[2,2] = 'A'
    g[2,1] = 'B'

    assert g.count() == collections.Counter({'A': 2, 'B': 1})
