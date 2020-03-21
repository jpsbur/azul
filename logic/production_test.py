import unittest

import util
import production

from util import Tile


class TestProduction(unittest.TestCase):
    def test_is_correct_move(self):
        p = production.Production(3)
        self.assertTrue(p.is_correct_move(
            [Tile.RED, Tile.BLUE, Tile.BLUE, Tile.WHITE], Tile.BLUE))
        self.assertTrue(p.is_correct_move(
            [Tile.RED, Tile.BLUE, Tile.BLUE, Tile.WHITE], Tile.RED))
        self.assertTrue(p.is_correct_move(
            [Tile.RED, Tile.BLUE, Tile.BLUE, Tile.WHITE], Tile.WHITE))
        self.assertFalse(p.is_correct_move(
            [Tile.RED, Tile.BLUE, Tile.BLUE, Tile.WHITE], Tile.FIRST_MOVE))
        self.assertFalse(p.is_correct_move(
            [Tile.RED, Tile.BLUE, Tile.BLUE, Tile.WHITE], Tile.ORANGE))
        self.assertFalse(p.is_correct_move(
            [Tile.RED, Tile.BLUE, Tile.BLUE, Tile.WHITE], Tile.BLACK))


    def test_take(self):
        p = production.Production(3)
        # Make one move: take the only red tile out of four
        self.assertEqual(
            p.take([Tile.RED, Tile.BLUE, Tile.BLUE, Tile.WHITE], Tile.RED),
            [Tile.RED])
        self.assertEqual(p.center, [Tile.BLUE, Tile.BLUE, Tile.WHITE])
        # Try to make an incorrect move to take 0 tiles
        self.assertRaises(
            util.InvalidMoveError, p.take,
            [Tile.RED, Tile.BLUE, Tile.BLUE, Tile.WHITE], Tile.BLACK)
        self.assertEqual(p.center, [Tile.BLUE, Tile.BLUE, Tile.WHITE])
        # Take another two tiles, this time blue
        self.assertEqual(
            p.take([Tile.RED, Tile.BLUE, Tile.BLUE, Tile.WHITE], Tile.BLUE),
            [Tile.BLUE, Tile.BLUE])
        self.assertEqual(
            p.center, [Tile.BLUE, Tile.BLUE, Tile.WHITE, Tile.RED, Tile.WHITE])
        # Take the white tiles and the first move tiles
        self.assertEqual(
            p.take(
                [Tile.RED, Tile.WHITE, Tile.FIRST_MOVE, Tile.WHITE],
                Tile.WHITE),
            [Tile.WHITE, Tile.FIRST_MOVE, Tile.WHITE])
        self.assertEqual(
            p.center,
            [Tile.BLUE, Tile.BLUE, Tile.WHITE, Tile.RED, Tile.WHITE, Tile.RED])


unittest.main()
