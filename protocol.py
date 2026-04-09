# mpc/protocol.py

from typing import List, Optional
from .types import GTProgram, GTQueue, GTTrace, GTStep

class GrillTagMPC:
    """
    Canonical MPC interface for Grill Tag simulation.
    """

    def load_program(self, program: GTProgram) -> None:
        """Load a Grill Tag program (raw bits or run-length encoded)."""
        raise NotImplementedError

    def load_queue(self, queue: GTQueue) -> None:
        """Load the initial queue."""
        raise NotImplementedError

    def step(self) -> GTStep:
        """Execute one Grill Tag command."""
        raise NotImplementedError

    def run(self, max_steps: Optional[int] = None) -> GTTrace:
        """Run until queue empty or max_steps reached."""
        raise NotImplementedError
