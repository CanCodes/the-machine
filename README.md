# **The** Machine

I've gone ahead and wrote the machine we have on our book.

## Usage

1. Install the required packages using `pip3 install -r requirements.txt` (Make sure you have pip installed on your system)
2. run `python3 cpu.py`

## Registers

The Machine has 16 general-purpose registers (0 to F)

- Each register can hold one byte

## Memory

This machine has a whopping 512 Bytes of memory! There are 256 cells in the memory and each of them hold can hold two bytes (16-bits). They are numbered from 00 to FF (in hexadecimal)

## Machine Instructions

- Each Instruction is 2 bytes (16-bits) long.
- The first 4 bits provide the op-code.
- The last 12 bits make up the operand field.

You can find the instructions on the book or the pdf.

## ⚠️ Notes

- **The opcode 6 is completely ignored** due to the fact that 8-bit floating point literally has no real use case in our lifes. (See [This StackOverflow Comment](https://stackoverflow.com/a/40507235))
- The machine I wrote here only executes instructions from the commandline. This makes the JUMP instruction worthless. Make sure you understand what that instruction means.
- You can view the machine's registers and memory cells using the `D000` instruction. **I MADE THIS INSTRUCTION UP IT DOES NOT EXIST ON THE GIVEN INSTRUCTIONS LIST!**
- I didn't get a chance to test everything, feel free to create an issue or a pr if anything buggy happens.
