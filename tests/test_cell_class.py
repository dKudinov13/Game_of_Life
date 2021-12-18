import unittest
from cell_class import *

class test_cell_class(unittest.TestCase):
    def test_new_cell_not_alive(self):
        c = Cell(0,0,0)
        assert c.alive == False

    def test_new_cell_zero_alive_neighbours(self):
        c = Cell(0,0,0)
        assert c.alive_neighbours == False

    def test_dead_cell_colour_white(self):
        c = Cell(0,0,0)
        assert (c.image == (0,0,0), False)

    def test_alive_cell_colour_black(self):
        c = Cell(0,0,0)
        assert (c.image == (0,0,0), True)

    def test_new_cell_neighbours(self):
        c = Cell(0,0,0)

        neighbour1 = Cell(0,1,0)
        neighbour1.alive = True
        neighbour2 = Cell(0, 1, 1)
        neighbour2.alive = True
        neighbour3 = Cell(0, -1, -1)
        neighbour3.alive = True
        neighbour4 = Cell(0, 1, -1)
        neighbour4.alive = False

        c.neighbours = [neighbour1, neighbour2, neighbour3, neighbour4]
        c.live_neighbours()
        assert c.alive_neighbours == 3
