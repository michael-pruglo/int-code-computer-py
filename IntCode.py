class IntCode:
    def __init__(self):
        self.mem = []

    def set_mem(self, data):
        self.mem = data

    def get_mem(self):
        return self.mem
