import unittest

from Engine.physics.motion import ConstantAccelerationMotion


class ConstantAccelerationMotionTest(unittest.TestCase):

    def test_correct_position(self):
        motion = ConstantAccelerationMotion(0, 0, 10)
        motion.move_time = 1


        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
