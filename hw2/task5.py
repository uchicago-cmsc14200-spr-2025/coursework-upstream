"""
CMSC 14200, Spring 2025
Homework #2, Task #5

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import math
import pygame
import sys

from task2 import BST
import task4


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

MAX_TREE_HEIGHT = 5

NODE_RADIUS = 10
LEAF_IMG_SIZE = 30


class TreeTrimmer:
    """
    A GUI application for drawing and trimming full trees.

    The application starts by drawing a full binary tree of height
    `MAX_TREE_HEIGHT` (i.e. `5`). Only the structure of the tree is
    displayed, not the values.

    When the user clicks on a tree node, it is "trimmed": the visual
    effect is that the subtree rooted at that node disappears.

    When the tree becomes completely empty, the application displays
    a message urging the user to conserve trees.

    Pressing the "q" key at any time quits the application.
    """

    cell_centers: list[tuple[int, tuple[int, int]]]
    tree: BST

    surface: pygame.Surface
    clock: pygame.time.Clock

    def __init__(self) -> None:
        """Initialize the GUI application"""
        self.reset_model()
        pygame.init()
        pygame.display.set_caption("Tree Trimmer")
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run_event_loop()

    ### INIT MODEL #########################################

    def reset_model(self) -> None:
        """Initialize the application state"""
        self.compute_tree_paper_cell_centers()
        self.tree = task4.full_tree(MAX_TREE_HEIGHT)

    ### Task 5: Step 4 ###

    def compute_tree_paper_cell_centers(self) -> None:
        """
        Compute the center position for every cell in
        the tree paper of height `MAX_TREE_HEIGHT`. Each
        cell is identified by its integer tree index. These
        are all saved in the `self.cell_centers` attribute.
        """
        pass # TODO

    ### CONTROLLER #########################################

    def run_event_loop(self) -> None:
        while True:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                ### Task 5: Step 1 ###

                # Add a conditional that checks if the "q" key
                # was pressed. If so, quit the application.
                #
                # elif event.type == pygame.KEYUP:
                #     TODO

                ### Task 5: Step 4 ###

                # Check whether the mouse has been clicked
                # within the node drawn at the center of a
                # tree paper cell.  If so, call the `trim_tree`
                # function with the index corresponding to this cell.
                #
                # elif event.type == pygame.MOUSEBUTTONUP:
                #     for i, (cx, cy) in self.cell_centers:
                #         TODO
                #         if TODO:
                #             try:
                #                 self.tree = task4.trim_tree(self.tree, i)
                #             except:
                #                 pass

                else:
                    pass

            self.draw_window()
            self.clock.tick(24)

    ### VIEW ###############################################

    def draw_window(self) -> None:
        self.draw_tree_paper()
        self.draw_tree_at_index(self.tree, 0)
        self.display_empty_tree_warning()
        pygame.display.update()

    ### Task 5: Step 2 ###

    def draw_tree_paper(self) -> None:
        """
        Draws blank "tree paper"" for a binary tree of height
        `MAX_TREE_HEIGHT` (i.e. 5). Visually, each row should be
        equally tall. The first row should have a single cell
        that spans the entire width of the window. The second
        row should have two equally sized cells that span the
        window. The third row should have four such cells, and
        so on.

        To achieve this visual effect, you can choose to draw
        either rectangles or line segments.

        Refer to the helper methods `row_height` and `col_width`.
        """
        pass # TODO

    def row_height(self) -> float:
        """
        Return the size of all rows in the tree paper.
        """
        raise NotImplementedError # TODO

    def col_width(self, row: int) -> float:
        """
        Return the width of each cell in the given row.
        """
        raise NotImplementedError # TODO

    ### Task 5: Step 3 ###

    def draw_tree_at_index(self, t: BST, i: int) -> None:
        """
        Draw a tree at a given tree index in the tree paper.

        If the tree is empty, nothing is drawn.
        If the tree is non-empty, a node is drawn,
        as well as branches to any non-empty children.

        Use the helper methods `draw_node_at`, `draw_line_between`,
        and `location_of_tree_index`.
        """
        pass # TODO

    def location_of_tree_index(self, i: int) -> tuple[int, int]:
        """
        Given a tree index `i`, compute the center `(cx, cy)`
        of the corresponding cell in the tree paper.
        """
        raise NotImplementedError # TODO

    def draw_node_at(self, i: int) -> None:
        """
        Given a tree index `i`, draw a node at the center
        of the corresponding cell in the tree paper.

        Use the helper method `location_of_tree_index`.
        """
        raise NotImplementedError # TODO

    def draw_line_between(self, i: int, j: int) -> None:
        """
        Given two tree indices `i` and `j`, draw a line between
        the centers of the corresponding cells in the tree paper.

        Use the helper method `location_of_tree_index`.
        """
        raise NotImplementedError # TODO

    ### Task 5: Step 5 ###

    def display_empty_tree_warning(self) -> None:
        """
        Display a string message somewhere in the window,
        urging the user not to trim so much next time.
        """
        msg = "Hey, be careful! That's too much trimming!"
        pass # TODO


if __name__ == "__main__":
    TreeTrimmer()
