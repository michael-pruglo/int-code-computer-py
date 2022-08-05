import unittest
from IntCodeImpl import IntCode


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
        self.assertEqual(ic.get_val(), mem_after[0])

    def exec_check_val(self, mem_before, expected):
        ic = IntCode()
        ic.set_mem(mem_before)
        ic.exec()
        self.assertEqual(ic.get_val(), expected)

    def test_opcode1(self):
        self.exec_check_mem([1,0,0,0,99], [2,0,0,0,99])
        self.exec_check_mem([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])

    def test_opcode2(self):
        self.exec_check_mem([2,3,0,3,99], [2,3,0,6,99])
        self.exec_check_mem([2,4,4,5,99,0], [2,4,4,5,99,9801])

    def test_opcodes12(self):
        self.exec_check_mem([1,9,10,3,2,3,11,0,99,30,40,50], [3500,9,10,70,2,3,11,0,99,30,40,50])
        self.exec_check_val(
            [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,6,23,1,23,6,27,1,13,27,31,2,13,31,35,1,5,35,39,2,39,13,43,1,10,43,47,2,13,47,51,1,6,51,55,2,55,13,59,1,59,10,63,1,63,10,67,2,10,67,71,1,6,71,75,1,10,75,79,1,79,9,83,2,83,6,87,2,87,9,91,1,5,91,95,1,6,95,99,1,99,9,103,2,10,103,107,1,107,6,111,2,9,111,115,1,5,115,119,1,10,119,123,1,2,123,127,1,127,6,0,99,2,14,0,0],
            12490719
        )
        self.exec_check_val(
            [1,20,3,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,6,23,1,23,6,27,1,13,27,31,2,13,31,35,1,5,35,39,2,39,13,43,1,10,43,47,2,13,47,51,1,6,51,55,2,55,13,59,1,59,10,63,1,63,10,67,2,10,67,71,1,6,71,75,1,10,75,79,1,79,9,83,2,83,6,87,2,87,9,91,1,5,91,95,1,6,95,99,1,99,9,103,2,10,103,107,1,107,6,111,2,9,111,115,1,5,115,119,1,10,119,123,1,2,123,127,1,127,6,0,99,2,14,0,0],
            19690720
        )

    def test_stop_at_99(self):
        pass


def run():
    unittest.main()


if __name__ == '__main__':
    run()
