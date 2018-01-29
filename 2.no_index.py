from simple_memory import SimMem


class SimTable(object):
    def __init__(self):
        self.fields = ('id', 'name')
        self.memory = SimMem()
    
    def add(self, name):
        mem = self.memory
        for c in name:
            mem.new_node(c)
        self.memory = mem
    
    def foot_print(self):
        self.memory.foot_print()

if __name__ == '__main__':
    t = SimTable()

    t.add('abcd')
    t.add('ab')
    t.add('name!!!')

    t.foot_print()
