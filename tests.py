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

    def exec_check_mem(self, mem_before, mem_after):
        ic = IntCode()
        ic.set_mem(mem_before)
        ic.exec()
        self.assertEqual(ic.get_mem(), mem_after)

    def test_opcode1(self):
        self.exec_check_mem([1,0,0,0,99], [2,0,0,0,99])
        self.exec_check_mem([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])

    def test_opcode2(self):
        self.exec_check_mem([2,3,0,3,99], [2,3,0,6,99])
        self.exec_check_mem([2,4,4,5,99,0], [2,4,4,5,99,9801])

    def test_stop_at_99(self):
        pass


def run():
    unittest.main()


if __name__ == '__main__':
    run()
