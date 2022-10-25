# **Vole** instruction interpreter

I've gone ahead and wrote the interpreter of the simple Vole architecture instruon set found in our book.

## Usage

1. Install the required packages using `pip3 install -r requirements.txt` (Make sure you have pip installed on your system)
2. Follow method 1 or 2.

### First Method (Interactive)
Run `python3 cpu.py`

This will run the interactive Vole REPL. You can enter instructions one by one in this prompt.

### Second Method
Create a text file named `source` containing the instructions seperated by new lines.

Run `python3 cpu.py source`

This will start interpreting the source file.

There is already an example file in the `demo` folder.
Go ahead and run `python3 cpu.py demo/example.vole`

## REPL Helpers
After running the first method and getting presented with the Vole REPL, go ahead and type `.help`

You will be offered following options,

`.manual`, use this command to familiarize yourself with the Vole instruction set architecture.
`.debug`, this will enter debug mode. You can inspect the registers and the memory as you like.
`.exit`, exit REPL. Has the same functionality as the instruction `C000`, but included for constistency in the REPL ux.

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
- Jump instruction is not supported in the current version.
- I didn't get a chance to test everything, feel free to create an issue or a pr if anything buggy happens.
