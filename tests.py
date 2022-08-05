import unittest
from IntCodeImpl import IntCode


class IntCodeTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_ctor(self):
        ic = IntCode()
        mlist = [1,2,3]
        ic.set_mem(mlist)
        self.assertEqual(mlist, ic.get_mem())

    def exec_check_mem(self, mem_before, mem_after):
        ic = IntCode()
        ic.set_mem(mem_before)
        ic.exec()
        self.assertEqual(mem_after, ic.get_mem())
        self.assertEqual(mem_after[0], ic.get_val())

    def exec_check_val(self, mem_before, expected):
        ic = IntCode()
        ic.set_mem(mem_before)
        ic.exec()
        self.assertEqual(expected, ic.get_val())

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

    def test_opcode3(self):
        ic = IntCode()
        ic.set_mem([3,7,1,7,7,0,99,0])
        ic.set_input([4])
        ic.exec()
        self.assertEqual([8,7,1,7,7,0,99,4], ic.get_mem())
        self.assertEqual(8, ic.get_val())

    def test_opcode4(self):
        ic = IntCode()
        ic.set_mem([4,1,99])
        ic.exec()
        self.assertEqual([4,1,99], ic.get_mem())
        self.assertEqual([1], ic.get_output())

    def test_opcodes34(self):
        ic = IntCode()
        ic.set_mem([3,0,4,0,99])
        ic.set_input([18])
        ic.exec()
        self.assertEqual([18], ic.get_output())

    def test_opmode4(self):
        ic = IntCode()
        ic.set_mem([104,2,99])
        ic.exec()
        self.assertEqual([104,2,99], ic.get_mem())
        self.assertEqual([2], ic.get_output())

    def test_opmode1(self):
        ic = IntCode()
        ic.set_mem([1101,100,-1,4,0])
        ic.exec()
        self.assertEqual([1101,100,-1,4,99], ic.get_mem())

    def test_opmode2(self):
        ic = IntCode()
        ic.set_mem([1002,4,3,4,33])
        ic.exec()
        self.assertEqual([1002,4,3,4,99], ic.get_mem())

    def test_opmodes1234(self):
        ic = IntCode()
        ic.set_mem([3,225,1,225,6,6,1100,1,238,225,104,0,1102,46,47,225,2,122,130,224,101,-1998,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1102,61,51,225,102,32,92,224,101,-800,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,61,64,225,1001,118,25,224,101,-106,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,33,25,225,1102,73,67,224,101,-4891,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,14,81,225,1102,17,74,225,1102,52,67,225,1101,94,27,225,101,71,39,224,101,-132,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1002,14,38,224,101,-1786,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1,65,126,224,1001,224,-128,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,81,40,224,1001,224,-121,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,374,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,479,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,539,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,614,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226])
        ic.set_input([1])
        ic.exec()
        self.assertEqual([0,0,0,0,0,0,0,0,0,12896948], ic.get_output())

    def test_opcode6p(self):
        for val in [0, 167]:
            ic = IntCode()
            ic.set_mem([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
            ic.set_input([val])
            ic.exec()
            self.assertEqual([int(val!=0)], ic.get_output())

    def test_opcode5i(self):
        for val in [0, 55]:
            ic = IntCode()
            ic.set_mem([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])
            ic.set_input([val])
            ic.exec()
            self.assertEqual([int(val!=0)], ic.get_output())

    def test_opcode7p(self):
        for val in [7, 10]:
            ic = IntCode()
            ic.set_mem([3,9,7,9,10,9,4,9,99,-1,8])
            ic.set_input([val])
            ic.exec()
            self.assertEqual([int(val<8)], ic.get_output())

    def test_opcode7i(self):
        for val in [6, 14]:
            ic = IntCode()
            ic.set_mem([3,3,1107,-1,8,3,4,3,99])
            ic.set_input([val])
            ic.exec()
            self.assertEqual([int(val<8)], ic.get_output())

    def test_stop_at_99(self):
        pass


def run():
    unittest.main()


if __name__ == '__main__':
    run()
