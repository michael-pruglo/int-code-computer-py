from collections import deque


class IntCode:
    def __init__(self):
        self.mem = []
        self.input = deque()
        self.output = []

    def set_mem(self, data):
        self.mem = data.copy()

    def get_mem(self):
        return self.mem

    def get_val(self):
        return self.mem[0]

    def set_input(self, data):
        self.input = deque(data)

    def get_output(self):
        return self.output

    def exec(self, start_address=0, verbose=False):
        i = start_address
        step = 0
        while True:
            instruction = self.mem[i]
            opcode = instruction%100
            step += 1

            if opcode==99:
                op_color = "36"
                if verbose:
                    print(f"\033[0;{op_color}m #{step:<4} @{i:<3}: 99 exit\033[0;0m")
                break

            elif opcode==1:
                a_addr = i+1 if instruction//100%10 else self.mem[i+1]
                a = self.mem[a_addr]

                b_addr = i+2 if instruction//1000%10 else self.mem[i+2]
                b = self.mem[b_addr]

                assert(instruction//10000 == 0)
                dest = self.mem[i+3]

                op_color = "32"
                if verbose:
                    print(f"\033[0;{op_color}m #{step:<4} @{i:<3}: 1 add m[{a_addr}]={a}  +  m[{b_addr}]={b}  into m[{dest}]")
                    self.print_mem({tuple(range(i, i+4)):f"\033[4;{op_color}m", (a_addr, b_addr):f"\033[7;{op_color}m"})

                self.mem[dest] = a + b

                if verbose:
                    self.print_mem({(dest, None): f"\033[7;{op_color}m"})
                    print('\n')
                i += 4

            elif opcode==2:
                a_addr = i+1 if instruction//100%10 else self.mem[i+1]
                a = self.mem[a_addr]

                b_addr = i+2 if instruction//1000%10 else self.mem[i+2]
                b = self.mem[b_addr]

                assert(instruction//10000 == 0)
                dest = self.mem[i+3]

                op_color = "34"
                if verbose:
                    print(f"\033[0;{op_color}m #{step:<4} @{i:<3}: 2 mul m[{a_addr}]={a}  *  m[{b_addr}]={b}  into m[{dest}]")
                    self.print_mem({tuple(range(i,i+4)):f"\033[4;{op_color}m", (a_addr,b_addr):f"\033[7;{op_color}m"})

                self.mem[dest] = a * b

                if verbose:
                    self.print_mem({(dest,None):f"\033[7;{op_color}m"})
                    print('\n')
                i += 4

            elif opcode==3:
                assert(instruction//10 == 0)
                dest = self.mem[i+1]

                op_color = "33"
                if verbose:
                    print(f"\033[0;{op_color}m #{step:<4} @{i:<3}: 3 input into m[{dest}]")
                    self.print_mem({(i,i+1):f"\033[4;{op_color}m", (dest,None):f"\033[7;{op_color}m"})

                self.mem[dest] = self.input.popleft()

                if verbose:
                    self.print_mem({(dest,None):f"\033[7;{op_color}m"})
                    print('\n')
                i += 2

            elif opcode==4:
                assert(instruction//1000 == 0)
                dest = i+1 if instruction//100%10 else self.mem[i+1]

                op_color = "35"
                if verbose:
                    print(f"\033[0;{op_color}m #{step:<4} @{i:<3}: 4 output m[{dest}]")
                    self.print_mem({(i,i+1):f"\033[4;{op_color}m", (dest,None):f"\033[7;{op_color}m"})

                self.output.append(self.mem[dest])

                if verbose:
                    self.print_mem({(dest,None):f"\033[7;{op_color}m"})
                    print('\n')
                i += 2

            elif opcode==5:
                a_addr = i+1 if instruction//100%10 else self.mem[i+1]
                a = self.mem[a_addr]

                dest = self.mem[i+2] if instruction//1000%10 else self.mem[self.mem[i+2]]
                assert(instruction//10000 == 0)

                op_color = "37"
                if verbose:
                    print(f"\033[0;{op_color}m #{step:<4} @{i:<3}: 5 jnz {a}  to  {dest}")
                    self.print_mem({(i,i+1,i+2):f"\033[4;{op_color}m", (dest if a else None,None):f"\033[7;{op_color}m"})
                    self.print_mem({(dest,None):f"\033[7;{op_color}m"})
                    print('\n')

                if a:
                    i = dest
                else:
                    i += 3

            elif opcode==6:
                a_addr = i+1 if instruction//100%10 else self.mem[i+1]
                a = self.mem[a_addr]

                dest = self.mem[i+2] if instruction//1000%10 else self.mem[self.mem[i+2]]
                assert(instruction//10000 == 0)

                op_color = "30"
                if verbose:
                    print(f"\033[0;{op_color}m #{step:<4} @{i:<3}: 6 jz {a}  to  {dest}")
                    self.print_mem({(i,i+1,i+2):f"\033[4;{op_color}m", (dest if not a else None,None):f"\033[7;{op_color}m"})
                    self.print_mem({(dest,None):f"\033[7;{op_color}m"})
                    print('\n')

                if not a:
                    i = dest
                else:
                    i += 3

            elif opcode==7:
                a_addr = i+1 if instruction//100%10 else self.mem[i+1]
                a = self.mem[a_addr]

                b_addr = i+2 if instruction//1000%10 else self.mem[i+2]
                b = self.mem[b_addr]

                dest = i+3 if instruction//10000%10 else self.mem[i+3]
                assert(instruction//100000 == 0)

                op_color = "31"
                if verbose:
                    print(f"\033[0;{op_color}m #{step:<4} @{i:<3}: 7 lt m[{dest}] = {a} < {b}")
                    self.print_mem({tuple(range(i,i+4)):f"\033[4;{op_color}m", (a_addr,b_addr):f"\033[7;{op_color}m"})

                self.mem[dest] = int(a<b)

                if verbose:
                    self.print_mem({(dest,None): f"\033[7;{op_color}m"})
                    print('\n')
                i += 4

            else:
                raise Exception(f"unknown opcode @{i}: {opcode}")

    def print_mem(self, color_map:dict[tuple,str]):
        COLOR_DEFAULT = "\033[0;37m"
        print("input:  ", list(self.input))
        print("output: ", self.output)
        print("memory: ", end='')
        for mem_pos,mem_val in enumerate(self.get_mem()):
            curr_color = COLOR_DEFAULT
            for pos,mapped_color in color_map.items():
                if mem_pos in pos:
                    curr_color = mapped_color

            print(f"{curr_color}{mem_val}{COLOR_DEFAULT}, ", end='')
        print()
