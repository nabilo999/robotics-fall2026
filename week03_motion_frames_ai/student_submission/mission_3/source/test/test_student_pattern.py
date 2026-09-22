"""Assignment-specific checks for the l_path motion pattern."""
import math
import unittest

from week03_pattern.pattern import build_pattern


class StudentPatternTests(unittest.TestCase):
    def test_l_path_has_the_required_distances_and_turn(self):
        segments = build_pattern("l_path")

        self.assertEqual(len(segments), 3)
        self.assertAlmostEqual(segments[0].linear_x * segments[0].duration, 0.40)
        self.assertAlmostEqual(segments[1].angular_z * segments[1].duration, math.pi / 2, places=4)
        self.assertAlmostEqual(segments[2].linear_x * segments[2].duration, 0.40)

    def test_unknown_pattern_is_rejected(self):
        with self.assertRaises(ValueError):
            build_pattern("not_a_pattern")
