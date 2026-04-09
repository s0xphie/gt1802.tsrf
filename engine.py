# mpc/engine.py

from .protocol import GrillTagMPC
from .types import GTProgram, GTQueue, GTStep, GTTrace

class GrillTagEngine(GrillTagMPC):

    def __init__(self):
        self.program = []
        self.queue = []
        self.ip = 0  # instruction pointer

    def load_program(self, program: GTProgram):
        self.program = program.bits
        self.ip = 0

    def load_queue(self, queue: GTQueue):
        self.queue = queue.bits.copy()

    def step(self) -> GTStep:
        if not self.queue:
            return GTStep(done=True)

        cmd_bit = self.program[self.ip]
        head = self.queue.pop(0)

        if cmd_bit == 0:  # command 10
            if head == 1:
                self.queue.append(0)
        else:             # command 11
            if head == 1:
                self.queue.extend([1,0])

        self.ip = (self.ip + 1) % len(self.program)

        return GTStep(done=False, head=head, cmd=cmd_bit, queue=self.queue.copy())

    def run(self, max_steps=None) -> GTTrace:
        trace = []
        steps = 0

        while self.queue:
            if max_steps and steps >= max_steps:
                break
            trace.append(self.step())
            steps += 1

        return GTTrace(trace)
