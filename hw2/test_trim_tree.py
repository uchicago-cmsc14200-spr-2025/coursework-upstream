"""
CMSC 14200, Spring 2025
Homework #2, Task 4B

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import pytest
import task4


def test_task4_int_to_path() -> None:
    """
    Check that int_to_path computes the correct paths for
    the first ten indices, 0 through 9.
    """
    raise NotImplementedError # TODO


def test_task4_trim_tree_at_index_0() -> None:
    """
    Create a full tree of height 3, and then trim at index 0.
    Check that the resulting tree is empty.
    """
    raise NotImplementedError # TODO


def test_task4_trim_tree_at_index_2() -> None:
    """
    Create a full tree of height 3, and then trim at index 2.
    Check that the resulting tree has four nodes, that it has
    two leaf nodes (that is, with zero children) in the expected
    places, and that it has no right subtree.
    """
    raise NotImplementedError # TODO


def test_task4_trim_tree_at_index_4() -> None:
    """
    Create a full tree of height 3, and then trim at index 4.
    Check that the resulting tree has six nodes, that it has
    three leaf nodes (that is, with zero children) in the expected
    places, and that it has one node with exactly one child
    (a left child) in the expected place.
    """
    raise NotImplementedError # TODO


def test_task4_trim_tree_at_index_6() -> None:
    """
    Create a full tree of height 3, and then trim at index 6.
    Check that the resulting tree has six nodes, that it has
    three leaf nodes (that is, with zero children) in the expected
    places, and that it has one node with exactly one child
    (a left child) in the expected place.
    """
    raise NotImplementedError # TODO


def test_task4_trim_tree_at_index_7() -> None:
    """
    Create a full tree of height 3, and then trim at index 7.
    Check that this operation raises a ValueError.
    """
    raise NotImplementedError # TODO

    ## To check that a piece of CODE raises a ValueError, write:
    ##
    ## with pytest.raises(ValueError):
    ##    CODE  # this code is expected to raise a ValueError
