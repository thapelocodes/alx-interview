#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ Calculates the perimeter of a single island in a grid. """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += j - 1 < 0 or grid[i][j - 1] == 0
                perimeter += i - 1 < 0 or grid[i - 1][j] == 0
                perimeter += j + 1 == len(grid[i]) or grid[i][j + 1] == 0
                perimeter += i + 1 == len(grid) or grid[i + 1][j] == 0

    return perimeter
