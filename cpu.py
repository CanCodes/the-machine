import os
import numpy as np

registers = [0x0] * 16
memory = [0x00] * 256


def rotate(num: int, amount: int) -> int:
    sNum = format(num, "08b")
    return int(f"0b{sNum[-amount:] + sNum[:-amount]}", 2)


while True:
    inst = int(input("Give me instruction: "), 16)
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
        break
    elif opCode == 0xD:
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
