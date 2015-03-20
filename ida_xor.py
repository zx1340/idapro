loc = 0x8048104
endloc = 0x080482e8
for i in range(endloc -loc):
        b = Dword(loc+i*4)
        decode = b ^ 0x8048FC1
        PatchDword(loc+i*4,decode)
# For byte using b = Byte(loc+i) and PathByte(...)
