class IntCode:
    def __init__(self):
        self.mem = []

    def set_mem(self, data):
        self.mem = data

    def get_mem(self):
        return self.mem

    def get_val(self):
        return self.mem[0]

    def exec(self, start_address=0, verbose=False):
        i = start_address
        iter = 0
        while True:
            opcode = self.mem[i]
            iter += 1

            if opcode==99:
                if verbose: print("99 exit")
                break

            elif opcode==1:
                a_addr = self.mem[i+1]
                a = self.mem[a_addr]
                b_addr = self.mem[i+2]
                b = self.mem[b_addr]
                dest = self.mem[i+3]

                op_color = "32"
                if verbose:
                    print(f"\033[0;{op_color}m #{iter:<4} @{i:<3}: 1 add m[{a_addr}]={a}  +  m[{b_addr}]={b}  into m[{dest}]")
                    self.print_mem({tuple(range(i, i+4)):f"\033[4;{op_color}m", (a_addr, b_addr):f"\033[7;{op_color}m"})

                self.mem[dest] = a + b

                if verbose:
                    self.print_mem({(dest, None): f"\033[7;{op_color}m"})
                    print('\n')
                i += 4

            elif opcode==2:
                a_addr = self.mem[i+1]
                a = self.mem[a_addr]
                b_addr = self.mem[i+2]
                b = self.mem[b_addr]
                dest = self.mem[i+3]

                op_color = "34"
                if verbose:
                    print(f"\033[0;{op_color}m #{iter:<4} @{i:<3}: 2 mul m[{a_addr}]={a}  *  m[{b_addr}]={b}  into m[{dest}]")
                    self.print_mem({tuple(range(i,i+4)):f"\033[4;{op_color}m", (a_addr,b_addr):f"\033[7;{op_color}m"})

                self.mem[dest] = a * b

                if verbose:
                    self.print_mem({(dest,None):f"\033[7;{op_color}m"})
                    print('\n')
                i += 4

            else:
                raise f"unknown opcode @{i}: {opcode}"

    def print_mem(self, color_map:dict[tuple,str]):
        COLOR_DEFAULT = "\033[0;37m"
        for mem_pos,mem_val in enumerate(self.get_mem()):
            curr_color = COLOR_DEFAULT
            for pos,mapped_color in color_map.items():
                if mem_pos in pos:
                    curr_color = mapped_color

            print(f"{curr_color}{mem_val}{COLOR_DEFAULT}, ", end='')
        print()
