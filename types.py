# mpc/types.py

from dataclasses import dataclass
from typing import List

@dataclass
class GTProgram:
    bits: List[int]

@dataclass
class GTQueue:
    bits: List[int]

@dataclass
class GTStep:
    done: bool
    head: int = None
    cmd: int = None
    queue: List[int] = None

@dataclass
class GTTrace:
    steps: List[GTStep]
