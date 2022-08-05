import unittest
from IntCode import IntCode


class IntCodeTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_ctor(self):
        ic = IntCode()
        mlist = [1,2,3]
        ic.set_mem(mlist)
        self.assertEqual(ic.get_mem(), mlist)


def run():
    unittest.main()


if __name__ == '__main__':
    run()
