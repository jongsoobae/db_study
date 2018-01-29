from simple_memory import SimMem


class SimTable(object):
    def __init__(self):
        self.fields = ('id', 'name')
        self.memory = SimMem()
    
    def add(self, name):
        mem = self.memory
        mem.new_node(' ')
        for c in name:
            mem.new_node(c)
        self.memory = mem

    def search_exact(self, value):
        mem = self.memory.memory

        db_values = ''.join(v for k, v in mem.items()).split()
        if value in db_values:
            return value
 
    def foot_print(self):
        self.memory.foot_print()

if __name__ == '__main__':
    t = SimTable()

    t.add('abcd')
    t.add('ab')
    t.add('name!!!')

    print t.search_exact('name!!')

    t.foot_print()
