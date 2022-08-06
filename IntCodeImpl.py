from collections import deque


class IntCode:
    def __init__(self, program=[], input=[]):
        self.mem = program.copy()
        self.input = deque(input)
        self.output = []

    def get(self):
        return self.mem, self.output

    def parse_command(self, ptr):
        instruction = self.mem[ptr]
        opcode = instruction % 100
        signature = {
            1: "110",
            2: "110",
            3: "0",
            4: "1",
            5: "11",
            6: "11",
            7: "110",
            8: "110",
            99: "",
        }[opcode]

        args = []
        instruction //= 100
        for arg_constraint in signature:
            ptr += 1
            if instruction % 10:
                assert arg_constraint == '1'
                addr = ptr
            else:
                addr = ptr if arg_constraint == '0' else self.mem[ptr]
            args.append(self.mem[addr])
            instruction //= 10
        assert instruction == 0

        return opcode, args

    def exec(self):
        i = 0
        while i < len(self.mem):
            opcode, args = self.parse_command(i)

            if   opcode == 1: self.mem[args[2]] = args[0] + args[1]
            elif opcode == 2: self.mem[args[2]] = args[0] * args[1]
            elif opcode == 3: self.mem[args[0]] = self.input.popleft()
            elif opcode == 4: self.output.append(args[0])
            elif opcode == 5:
                if args[0]:
                    i = args[1]; continue
            elif opcode == 6:
                if not args[0]:
                    i = args[1]; continue
            elif opcode == 7: self.mem[args[2]] = int(args[0] < args[1])
            elif opcode == 8: self.mem[args[2]] = int(args[0] == args[1])
            elif opcode == 99: break
            else:
                raise Exception(f"unknown opcode @{i}: {opcode}")

            i += 1+len(args)


def run_intcode_program(program=[], input=[]):
    ic = IntCode(program, input)
    ic.exec()
    return ic.get()