import unittest
import src.how_many_tracks as hmt


class HowManyTracksTest(unittest.TestCase):
    """
    This class tests the how_many_tracks module
    """

    def test_calc(self):
        self.assertEquals(0, hmt.calc())
        self.assertEquals(36, hmt.calc(straight_pieces=2, curved_pieces=8))

