import unittest

from approvaltests.approvals import verify


from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from approvaltests.storyboard import Storyboard


class RegressionTest(unittest.TestCase):
    def setUp(self):
        self.reporter = None #Use the first difftool found on your system
        #self.reporter = GenericDiffReporterFactory().get("DiffMerge")
        #Download DiffMerge at https://sourcegear.com/diffmerge/



    def test_single_square_dies(self):
        s = Storyboard()
        #create a board with 1,2 alive
        #advance the board
        #verify that the board is empty


        verify(s, self.reporter)


