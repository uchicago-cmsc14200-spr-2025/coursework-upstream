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

from image import Image, Color, Loc
from typing import TypedDict

Region = TypedDict(
    "Region",
    {"color": Color, "pixels": set[Loc], "outline": set[Loc]},
)


class ImageGraph:
    """
    Class for a graph over an image where adjacent pixels are neighbors
    """

    def __init__(self, image: Image):
        """
        Constructor

        Inputs:
            image (Image): the image over which to build the graph
        """
        raise NotImplementedError("TODO")

    def neighbors(self, location: Loc) -> set[Loc]:
        """
        Determines the pixels adjacent to a given pixel in the graph.
        Adjacency is defined by being immediately above, below, to the
        left, or to the right.

        Inputs:
            location (Loc): the pixel whose immediate neighbors to find

        Returns (set[Loc]): the set of immediate neighbors
        """
        raise NotImplementedError("TODO")

    def compute_region(self, start: Loc) -> Region:
        """
        Determines the region of contiguous pixels surrounding the given
        starting pixel with the same color, then returns (i) its color,
        (ii) the set of pixels in the region, and (iii) the set of pixels
        on the border between this region and other-colored regions or the
        edge of the image. Contiguity is defined by being directly above,
        below, to the left, or to the right.

        Inputs:
            start (Loc): a pixel in the region to outline

        Returns (Region): the color, interior, and outline of the region
        """
        raise NotImplementedError("TODO")

    def compute_all_regions(self) -> list[Region]:
        """
        Determine a list of all regions in the image. Each of the
        regions should be as large as possible, as prescribed and
        implemented by `compute_region`.

        Returns (list[Region]): the order of regions does not matter
        """
        raise NotImplementedError("TODO")
