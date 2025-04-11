"""
CMSC 14200, Spring 2025
Homework #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import pytest

from image import Image, Loc, Color
from graph import ImageGraph


### TASK 2 TESTS ###


def test_task2_neighbors_corners() -> None:
    """
    Load the image represented by assets/grid.ppm, and
    check that `neighbors` returns the correct answer
    for each of the four corner pixels (top-left, top-right,
    bottom-right, and bottom-left).
    """
    raise NotImplementedError("TODO")


def test_task2_neighbors_edges() -> None:
    """
    Load the image represented by assets/grid.ppm, and
    check that `neighbors` returns the correct answer
    for one non-corner pixel on each of the four edges
    of the image (left, top, right, bottom).
    """
    raise NotImplementedError("TODO")


def test_task2_neighbors_interior() -> None:
    """
    Load the image represented by assets/grid.ppm, and
    check that `neighbors` returns the correct answer
    for three distinct interior pixels (i.e, excluding
    corner and edge pixels).
    """
    raise NotImplementedError("TODO")


### TASK 4 TESTS ###


def test_task4_compute_all_regions_count() -> None:
    """
    For each of the three sample images
    (assets/{example, grid, shapes.ppm}), call
    compute_all_regions and check that the number
    of regions and total number of pixels inside
    the regions are correct.
    """
    raise NotImplementedError("TODO")


def test_task4_compute_all_regions_count_blue() -> None:
    """
    For each of the three sample images
    (assets/{example, grid, shapes.ppm}), call
    compute_all_regions and check that the number
    of blue regions are correct.
    """
    raise NotImplementedError("TODO")


def test_task4_compute_all_regions_count_colors() -> None:
    """
    For each of the three sample images
    (assets/{example, grid, shapes.ppm}), call
    compute_all_regions and check that the number
    of regions for each color in the image is
    correct.
    """
    raise NotImplementedError("TODO")
