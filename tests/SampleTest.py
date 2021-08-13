import unittest

from approvaltests.approvals import verify


from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from approvaltests.storyboard import Storyboard


def print_grid(width, height, board):
    t= ""
    for y in range (0  , height):
        for x in range (0, width):
            t+= f"{board(x,y)} "
        t+="\n"
    return t


class RegressionTest(unittest.TestCase):
    def setUp(self):
        self.reporter = None #Use the first difftool found on your system
        #self.reporter = GenericDiffReporterFactory().get("DiffMerge")
        #Download DiffMerge at https://sourcegear.com/diffmerge/



    def test_single_square_dies(self):
        s = Storyboard()
        #create a board with 1,2 alive
        board = lambda x, y: x == 1 and y == 2
        s.add_frame(print_grid(5,4,lambda x,y: "x" if board(x,y) else "."))
        #advance the board
        #verify that the board is empty


        verify(s, self.reporter)


