"""
CMSC 14200, Spring 2025
Homework #1, Task 4C (tests)

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from task4 import Card


def test_task4_no_overlapping_features() -> None:
    """
    Write a test that creates two cards with no overlapping feature names.
    Check that conflicting_features returns the correct value (which is
    the empty dictionary).
    """
    raise NotImplementedError("TODO: test_no_overlapping_features")


def test_task4_no_conflicting_features() -> None:
    """
    Write a test that creates two cards with one common feature and
    no conflicting features. Check that conflicting_features returns
    the correct value (which is the empty dictionary).
    """
    raise NotImplementedError("TODO: test_no_conflicting_features")


def test_task4_one_conflicting_feature() -> None:
    """
    Write a test that creates two cards with two common feature names,
    called "shape" and "number". The two cards should have the same value,
    "square", for "shape". That is, {"shape": "square"} is a common feature.
    For "number", the two cards should have different values, "1" and "7".
    Check that conflicting_features returns a dictionary that maps "number"
    to a pair with "1" and "7".
    """
    raise NotImplementedError("TODO: test_one_conflicting_feature")


def test_task4_two_conflicting_features() -> None:
    """
    Write a test that creates two cards with three conflicting features,
    and check that conflicting_features returns the correct value.
    """
    raise NotImplementedError("TODO: test_two_conflicting_features")
