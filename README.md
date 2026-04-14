
---

🧠 Hybrid Ternary–Binary CPU Emulator

A conceptual CPU emulator that simulates a dual-radix architecture combining:

🔺 Balanced ternary computation (-1, 0, +1)

🔵 Binary execution passthrough (standard integer logic)

🔀 Hybrid execution mode (mixed radix routing)


This project is an experimental sandbox for exploring non-binary computation models alongside traditional binary systems.


---

🚀 Concept Overview

Modern processors (including architectures like RISC-V) are fundamentally binary.

This emulator explores a hypothetical extension:

> A CPU where each instruction can dynamically select its number system:



T mode → ternary-native arithmetic

B mode → binary execution fast-path

H mode → hybrid computation (ternary + binary normalization)



---

⚙️ Architecture Model

🧩 Core Components

1. Ternary ALU

Operates using balanced trits:

-1, 0, +1

Supports:

ADD

SUB

MUL (clamped ternary logic)



---

2. Binary Execution Unit

Standard integer ALU supporting:

ADD

SUB

MUL

AND / OR


Used for:

fast-path execution

legacy compatibility simulation



---

3. Hybrid Execution Layer

Bridges both systems:

converts binary → ternary

executes ternary operation

normalizes result back to binary



---

4. Register File

A shared register bank:

stores integer values

interpreted as ternary or binary depending on mode



---

🧾 Instruction Set

Each instruction has the form:

(mode, operation, src_a, src_b, dest)

Modes

Mode	Description

T	Ternary execution
B	Binary execution
H	Hybrid execution



---

Supported Operations

Ternary

ADD

SUB

MUL


Binary

ADD

SUB

MUL

AND

OR


Hybrid

ADD

SUB

MUL



---

🧪 Example Program

Instruction(mode="T", op="ADD", a=0, b=1, dest=2)
Instruction(mode="B", op="ADD", a=0, b=1, dest=3)
Instruction(mode="H", op="ADD", a=0, b=1, dest=4)
Instruction(mode="T", op="MUL", a=2, b=1, dest=5)


---

🧠 Why This Exists

This emulator is a research playground for:

🔬 Alternative computation systems

ternary logic machines

non-binary arithmetic models


⚡ Heterogeneous execution

mixing multiple number systems at runtime


🧩 Future architectures

radix-switching CPUs

mixed-logic ALUs

hybrid symbolic–numeric compute models



---

🔮 Design Inspiration

While conventional CPUs are binary-based, experimental architectures explore alternatives:

ternary logic systems (balanced computing states)

FPGA reconfigurable logic

GPU-style parallel execution domains


This project sits in the conceptual space between:

classical CPU design

speculative computer architecture

research into non-binary computing systems



---

🧪 Running the Emulator

python emulator.py

Expected output:

register dump after executing mixed-mode instructions



---

📦 File Structure

emulator.py     # Hybrid CPU implementation
README.md       # This file


---

🧭 Future Extensions

🔧 ISA Expansion

LOAD / STORE

JMP / BRANCH

CALL / RET


🧠 Compiler Layer

high-level language → hybrid instructions


⚡ True ternary memory model

trit-packed storage system


🖥 Visualization

step-by-step execution debugger

register state timeline


🔀 Advanced idea

A full radix-aware compute scheduler that dynamically selects:

binary

ternary

hybrid execution per instruction



---

⚠️ Disclaimer

This is a conceptual emulator, not a physical CPU implementation.
It is intended for architecture exploration and experimental computation research.


---
