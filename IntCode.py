class IntCode:
    def __init__(self):
        self.mem = []

    def set_mem(self, data):
        self.mem = data

    def get_mem(self):
        return self.mem

    def exec(self, start_address=0):
        i = start_address
        while True:
            opcode = self.mem[i]
            if opcode==99:
                break

            elif opcode==1:
                a = self.mem[self.mem[i+1]]
                b = self.mem[self.mem[i+2]]
                self.mem[self.mem[i+3]] = a+b
                i += 4

            elif opcode==2:
                a = self.mem[self.mem[i+1]]
                b = self.mem[self.mem[i+2]]
                self.mem[self.mem[i+3]] = a*b
                i += 4
