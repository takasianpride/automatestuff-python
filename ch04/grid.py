#! /usr/bin/python3
# _*_ coding: utf-8 _*_

def print_grid(list):
    width = len(grid)
    height = len(grid[0])
    for y in range(height):
        for x in range(width):
            print(grid[x][y], end='')
        print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print_grid(grid)
