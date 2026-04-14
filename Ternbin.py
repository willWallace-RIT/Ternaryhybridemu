""" Ternary + Binary Hybrid CPU Emulator (Educational Prototype)

This emulator simulates a simplified hybrid architecture:

Ternary core: balanced ternary values (-1, 0, +1)

Binary passthrough unit: standard integer/binary operations

Instruction routing: T (ternary), B (binary), H (hybrid)


This is NOT hardware accurate, but a conceptual execution model. """

from dataclasses import dataclass from typing import List, Union, Tuple

Trit = int  # must be -1, 0, or 1

----------------------------

Utility: ternary arithmetic

----------------------------

def clamp_trit(x: int) -> Trit: if x > 1: return 1 if x < -1: return -1 return x

def ternary_add(a: Trit, b: Trit) -> Trit: return clamp_trit(a + b)

def ternary_mul(a: Trit, b: Trit) -> Trit: return clamp_trit(a * b)

----------------------------

Instruction model

----------------------------

@dataclass class Instruction: mode: str   # 'T', 'B', or 'H' op: str     # operation a: int b: int = 0 dest: int = 0

----------------------------

Hybrid CPU Emulator

----------------------------

class HybridCPU: def init(self, num_registers: int = 8): # ternary register file (shadowed binary ints allowed) self.reg = [0 for _ in range(num_registers)]

# ------------------------
# Binary execution unit
# ------------------------
def binary_exec(self, op: str, a: int, b: int) -> int:
    if op == "ADD":
        return a + b
    elif op == "SUB":
        return a - b
    elif op == "MUL":
        return a * b
    elif op == "AND":
        return a & b
    elif op == "OR":
        return a | b
    else:
        raise ValueError(f"Unknown binary op {op}")

# ------------------------
# Ternary execution unit
# ------------------------
def ternary_exec(self, op: str, a: Trit, b: Trit) -> Trit:
    if op == "ADD":
        return ternary_add(a, b)
    elif op == "MUL":
        return ternary_mul(a, b)
    elif op == "SUB":
        return ternary_add(a, -b)
    else:
        raise ValueError(f"Unknown ternary op {op}")

# ------------------------
# Hybrid execution unit
# ------------------------
def hybrid_exec(self, op: str, a: int, b: int) -> int:
    """
    Hybrid mode splits work:
    - arithmetic core in ternary
    - final normalization in binary
    """
    ta = clamp_trit(a)
    tb = clamp_trit(b)

    # ternary compute
    t_result = self.ternary_exec(op, ta, tb)

    # binary normalization (expand back)
    return int(t_result)

# ------------------------
# Instruction execution
# ------------------------
def step(self, instr: Instruction):
    a = self.reg[instr.a]
    b = self.reg[instr.b]

    if instr.mode == "B":
        result = self.binary_exec(instr.op, a, b)

    elif instr.mode == "T":
        result = self.ternary_exec(instr.op, clamp_trit(a), clamp_trit(b))

    elif instr.mode == "H":
        result = self.hybrid_exec(instr.op, a, b)

    else:
        raise ValueError("Invalid mode")

    self.reg[instr.dest] = result

# ------------------------
# Run program
# ------------------------
def run(self, program: List[Instruction]):
    for instr in program:
        self.step(instr)

def dump(self):
    return self.reg

----------------------------

Example program

----------------------------

if name == "main": cpu = HybridCPU()

# Load values
cpu.reg[0] = 1
cpu.reg[1] = -1

program = [
    Instruction(mode="T", op="ADD", a=0, b=1, dest=2),
    Instruction(mode="B", op="ADD", a=0, b=1, dest=3),
    Instruction(mode="H", op="ADD", a=0, b=1, dest=4),
    Instruction(mode="T", op="MUL", a=2, b=1, dest=5),
]

cpu.run(program)

print("Registers:")
for i, v in enumerate(cpu.dump()):
    print(i, v)
