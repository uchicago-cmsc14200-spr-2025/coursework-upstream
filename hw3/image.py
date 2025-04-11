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

from typing import TypeAlias

Loc: TypeAlias = tuple[int, int]
Color: TypeAlias = tuple[int, int, int]

class Image:
    """
    Class for a bitmap image
    """

    width: int
    height: int
    pixels: list[list[Color]]
    
    def __init__(self, filename: str):
        """
        Constructor

        Inputs:
            filename (str): path to a PPM file
        """
        raise NotImplementedError("TODO")
