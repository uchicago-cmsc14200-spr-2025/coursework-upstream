"""
CMSC 14200, Spring 2025
Homework #4, Task #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import heapq
from graph import GridGraph, Vertex
from typing import TypeAlias


DijkstraTable: TypeAlias = dict[Vertex, tuple[int, Vertex | None]]


def shortest_paths(graph: GridGraph, origin: Vertex) -> DijkstraTable:
    """
    Find the shortest path from the origin to every other reachable destination
    in the graph

    Inputs:
       graph (GridGraph): the grid graph
       origin (Vertex): the starting node

    Returns:
      DijkstraTable: Shortest distances from origin to every other vertex,
      along with the previous vertex along the shortest path.
    """

    # YOUR CODE HERE
    raise NotImplementedError


def trace_path(
    table: DijkstraTable, destination: Vertex
) -> tuple[list[Vertex], int]:
    """
    Given a dictionary of single-source shortest path distances and previous
    nodes, reconstruct the shortest path from origin to destination, as well
    as its distance.
    """

    # YOUR CODE HERE
    raise NotImplementedError
