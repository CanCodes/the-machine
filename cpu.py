import os
import numpy as np
import sys

registers = [0x0] * 16
memory = [0x00] * 256

VOLE_USAGE = \
"""
python cpu.py [source]

    [source] OPTIONAL
      if empty
          runs Vole REP
      else
          interprets the source file
""" \
.lstrip()

VOLE_GREETING = \
"""
Welcome to Vole Machine Language REPL v1.1
Type .help for instructions
""" \
.lstrip()

VOLE_HELP = \
"""
.help    print help page
.manual  read vole instructions manual
.debug   enter debug mode
.exit    exit vole REPL
""" \
.lstrip()

VOLE_MANUAL = \
"""
Vole is a virtual machine language created for educational purposes.

0x1 RXY LOAD the register R with the bit pattern found in the 
memory cell whose address is XY.

0x2 RXY LOAD the register R with the bit pattern XY.

0x3 RXY STORE the bit pattern found in register R in the memory 
cell whose address is XY.

0x4 0RS MOVE the bit pattern found in register R to register S.

0x5 RST ADD the bit patterns in registers S and T as though they 
were two’s complement representations and leave the 
result in register R.

0x6 RST ADD the bit patterns in registers S and T as though they 
represented values in floating-point notation and leave 
the floating-point result in register R.

0x7 RST OR the bit patterns in registers S and T and place the 
result in register R.

0x8 RST AND the bit patterns in registers S and T and place the 
result in register R.

0x9 RST XOR the bit patterns in registers S and T and place the 
result in register R.

0xA R0X ROTATE the bit pattern in register R one bit to the right 
X times. Each time, place the bit that started at the low-
order end at the high-order end.

0xC 000 HALT execution.
""" \
.lstrip()


def rotate(num: int, amount: int) -> int:
    sNum = format(num, "08b")
    return int(f"0b{sNum[-amount:] + sNum[:-amount]}", 2)

def debug_tui():
    os.system('clear' if os.name not in ("nt", "dos") else "cls")
    while True:
        controls = input(
            " You've entered the visualization zone.\n"
            "   Enter M to view the Memory zone.\n"
            "   Enter R to view the Registers zone.\n"
            "   Enter Q to quit the visualization zone.\n:"
        )
        if controls.lower() == "q":
            os.system('clear' if os.name not in ("nt", "dos") else "cls")
            break
        elif controls.lower() == "m":
            print(
                "\n".join([f"{format(i, 'x').upper()}. {format(val, '#04x')}" for i, val in enumerate(memory)]))
        elif controls.lower() == "r":
            print(
                "\n".join([f"{format(i, 'x').upper()}. {format(val, '#04x')}" for i, val in enumerate(registers)]))

def interpret_instruction(inststr):
    inst = 0
    inststr = inststr.strip()

    if inststr == ".help":
        print(VOLE_HELP)
        return 0
    if inststr == ".manual":
        print(VOLE_MANUAL)
        return 0
    if inststr == ".debug":
        debug_tui()
        return 0
    if inststr == ".exit":
        return 1

    try:
        inst = int(inststr, 16)
    except:
        print(f"Bad instruction {inststr}")
        return 0

    opCode = (inst & 0xF000) >> 12
    r = (inst & 0x0F00) >> 8

    n = inst & 0x000F
    nn = inst & 0x00FF
    nnn = inst & 0x0FFF

    y = (inst & 0x00F0) >> 4
    x = inst & 0x000F

    if opCode == 0x1:
        registers[r] = memory[nn]
        print(f"LOAD R{format(registers[r], '#x')} with {memory[nn]} ({nn})")
    elif opCode == 0x2:
        registers[r] = nn
        print("LOAD R{0:#x} with {1:#x}".format(r, nn))
    elif opCode == 0x3:
        memory[nn] = registers[r]
        print(f"STORE {format(registers[r], '#x')} in {nn}")
    elif opCode == 0x4:
        registers[x] = registers[y]
        print(f"MOVE register {format(y, '#x')} to register {format(x, '#x')}")
    elif opCode == 0x5:
        a = registers[x]
        b = registers[y]
        registers[r] = np.sum((a, b), dtype=np.int8)
        print(
            f"ADD register {format(x, '#x')} ({np.binary_repr(a, 8)}) to register {format(y, '#x')} ({np.binary_repr(b, 8)}) and save to register {format(r, '#x')} ({np.binary_repr(registers[r], 8)}) -> {np.int8(registers[r])})")
    elif opCode == 0x6:
        print("No.")
    elif opCode == 0x7:
        a = registers[x]
        b = registers[y]
        registers[r] = a | b
        print(
            f"OR register {format(x, '#x')} or register {format(y, '#x')} and save to register {format(r, '#x')} ({format(registers[r], '#x')})")
    elif opCode == 0x8:
        a = registers[x]
        b = registers[y]
        registers[r] = a & b
        print(
            f"AND register {format(x, '#x')} and register {format(y, '#x')} and save to register {format(r, '#x')} ({format(registers[r], '#x')})")
    elif opCode == 0x9:
        a = registers[x]
        b = registers[y]
        registers[r] = a ^ b
        print(
            f"XOR register {format(x, '#x')} xor register {format(y, '#x')} and save to register {format(r, '#x')} ({format(registers[r], '#x')})")
    elif opCode == 0xA:
        registers[r] = rotate(registers[r], x)
        print(
            f"ROTATE rotated register {format(r, '#x')} {format(x, '#x')} times to the right ({format(registers[r], '#x')})")
    elif opCode == 0xB:
        print("This is a command-line based CPU emulation, we don't store the instructions on the memory. Therefore "
              "you can't jump to that memory cell.")
    elif opCode == 0xC:
        print("HALT")
        return 1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Enter REPL mode
        print(VOLE_GREETING)
        while True:
            retval = interpret_instruction(input("vole> "))
            if retval == 1:
                break

    if "--help" in sys.argv:
        print(VOLE_USAGE)
    else:
        source_file = sys.argv[1]
        print(f"Loading instructions from {source_file}")
