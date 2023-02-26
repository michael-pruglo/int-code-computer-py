import enum
from collections import deque


class IntCode:
    def __init__(self, program:list[int]=None, input:list[int]=None) -> None:
        self.mem = [] if program is None else program.copy()
        self.input = deque(input or [])
        self.output = []
        self.ptr = 0
        self.rel_base = 0

    class ExecutionError(RuntimeError):
        pass

    def get(self) -> tuple[list[int], list[int]]:
        return self.mem, self.output

    def exec(self) -> None:
        while self.ptr < len(self.mem):
            opcode, args = self._parse_command()

            if   opcode == 1: self._mem_resize(args[2]); self.mem[args[2]] = args[0] + args[1]
            elif opcode == 2: self._mem_resize(args[2]); self.mem[args[2]] = args[0] * args[1]
            elif opcode == 3:
                if self.input:
                    self._mem_resize(args[0])
                    self.mem[args[0]] = self.input.popleft()
                else:
                    return
            elif opcode == 4: self.output.append(args[0])
            elif (opcode == 5 and args[0]) or (opcode == 6 and not args[0]):
                self._mem_resize(args[1])
                self.ptr = args[1]
                continue
            elif opcode == 7: self._mem_resize(args[2]); self.mem[args[2]] = int(args[0] < args[1])
            elif opcode == 8: self._mem_resize(args[2]); self.mem[args[2]] = int(args[0] == args[1])
            elif opcode == 9: self.rel_base += args[0]
            elif opcode == 99: return

            self.ptr += 1

        raise IntCode.ExecutionError(f"Reached the end of memory without terminating")

    def _parse_command(self) -> tuple[int, list[int]]:
        OPERATION_SIGNATURES = {
            1: "110",
            2: "110",
            3: "0",
            4: "1",
            5: "11",
            6: "11",
            7: "110",
            8: "110",
            9: "1",
            99: "",
        }
        instruction = self.mem[self.ptr]
        opcode = instruction % 100
        if opcode not in OPERATION_SIGNATURES:
            raise IntCode.ExecutionError(f"cannot parse command @{self.ptr}: {instruction}")

        args = []
        instruction //= 100
        for arg_constraint in OPERATION_SIGNATURES[opcode]:
            self.ptr += 1
            args.append(self._get_argument(arg_constraint, instruction % 10))
            instruction //= 10
        assert instruction == 0

        return opcode, args

    def _get_argument(self, arg_constraint, param_mode) -> int:
        class ParamMode(enum.IntEnum):
            POSITION = 0
            IMMEDIATE = 1
            RELATIVE = 2

        if param_mode == ParamMode.IMMEDIATE:
            assert arg_constraint == '1'
            addr = self.ptr
        elif param_mode == ParamMode.POSITION:
            addr = self.ptr if arg_constraint == '0' else self.mem[self.ptr]
        elif param_mode == ParamMode.RELATIVE:
            addr = self.mem[self.ptr] + self.rel_base
            if arg_constraint == '0':
                return addr
        else:
            raise IntCode.ExecutionError(f"Unknown operation parameter mode @{self.ptr-1}: mode {param_mode}")

        self._mem_resize(addr)
        return self.mem[addr]

    def _mem_resize(self, idx) -> None:
        if len(self.mem) <= idx:
            self.mem += [0] * (idx-len(self.mem)+1)


def run_intcode_program(program=None, input=None):
    ic = IntCode(program, input)
    ic.exec()
    return ic.get()
