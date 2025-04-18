"""
CMSC 14200, Spring 2025
Homework #4, Task #1

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from graph import GridGraph


def load_maze_grid(filename: str) -> list[list[str]]:
    """
    Read a file that contains a maze specification and
    return a 2D-list representation of the maze.

    Input:
       filename (str): The file to load, assumed to
       represent a valid maze

    Returns:
       list[list[str]]: 2D-list matrix of the maze
    """
    # YOUR CODE GOES HERE
    raise NotImplementedError


def construct_grid_graph(grid: list[list[str]]) -> GridGraph:
    """
    Given a 2D representation of a maze, induce the grid graph object

    Input:
        grid (list[list[str]]): The input maze

    Returns:
        GridGraph: The induced grid graph object
    """
    # YOUR CODE GOES HERE
    raise NotImplementedError
