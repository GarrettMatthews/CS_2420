"""
File: maze.py
Project 7.9

Determine the solution to a maze problem.
Uses a gid to represent the maze.  This grid is input from
a text file.  Uses a stack-based backtracking algorithm.
"""

from grid import Grid
from arraystack import ArrayStack

def main():
    maze = getMazeFromFile()
    print(maze)
    (startRow, startCol) = findStartPos(maze)
    success = getOut(startRow, startCol, maze)
    if success:
        print("Maze solved:")
        print(maze)
    else:
        print("No path out of this maze")
    
def getMazeFromFile():
    """Reads the maze from a text file and returns a grid that
    represents it."""
    name = input("Enter a file name for the maze: ")
    fileObj = open(name, 'r')
    firstLine = list(map(int, fileObj.readline().strip().split()))
    rows = firstLine[0]
    columns = firstLine[1]
    maze = Grid(rows, columns, "*")
    for row in range(rows):
        line = fileObj.readline().strip()
        column = 0
        for ch in line:
            maze[row][column] = ch
            column += 1
    return maze

def findStartPos(maze):
    """Returns the position of the start symbol in the grid."""
    for row in range(maze.getHeight()):
        for column in range(maze.getWidth()):
            if maze[row][column] == 'P':
                return (row, column)
    return (-1, -1)
                
def getOut(row, column, maze):
    """(row,column) is the position of the start symbol in the maze.
    Returns True if the maze can be solved or False otherwise."""
    # States are tuples of coordinates of cells in the grid.
    
            # Try NORTH
            if row != 0 and not maze[row - 1][column] in ('*', '.'):
                stack.push((row - 1, column))             
            # Try SOUTH
                         
            # Try EAST
                        
            # Try WEST
            
    

if __name__ == "__main__": main()
