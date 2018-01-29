import redis
import pickle


class Node(object):
    """
    memory node
    """
    def __init__(self, value):
        self.value = value


class SimMem(object):
    """
    memory simulator
    """
    def __init__(self, max_size=20):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=11)
        self.address = 0
        mem = {}
        for idx in range(max_size):
            mem[idx] = ' '
        
        self.memory = mem

    def _next_addr(self):
        self.address = self.address + 1
        return self.address

    def new_node(self, value):
        mem = self.memory
        mem[self._next_addr()] = value
        self.memory = mem

    @property
    def memory(self):
        return pickle.loads(self.redis.get('memory'))

    @memory.setter
    def memory(self, mem):
        self.redis.set('memory', pickle.dumps(mem))

    @property
    def address(self):
        return int(self.redis.get('address'))

    @address.setter
    def address(self, value):
        self.redis.set('address', value)

    def foot_print(self):
        for i, v in self.memory.items():
            if v:
                print i, ': ', v


if __name__ == '__main__':
    sim = SimMem()
    sim.new_node(1)
    sim.new_node(1)
    sim.new_node(1)
    sim.foot_print()
