# run.py

from mpc.engine import GrillTagEngine
from mpc.types import GTProgram, GTQueue

def load_bits(path):
    with open(path) as f:
        return [int(c) for c in f.read().strip()]

if __name__ == "__main__":
    engine = GrillTagEngine()

    program_bits = load_bits("programs/grill_1802_phase0.gt")
    queue_bits   = load_bits("queues/alt_1802_phase1.txt")

    engine.load_program(GTProgram(program_bits))
    engine.load_queue(GTQueue(queue_bits))

    trace = engine.run()

    print(f"Total steps: {len(trace.steps)}")
    print(f"Final queue: {trace.steps[-1].queue if trace.steps else []}")
