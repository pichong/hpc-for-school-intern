import os
import sys

# get byte value of ASCII characters 'a' and 'z'
# ASCII characters are consecuvites from a to z
ord_a = ord('a')
ord_z = ord('z')

# open the file
f = open(sys.argv[1], 'r')

# get the number of characters
f.seek(0, os.SEEK_END)
nchars = f.tell()

# process text character by character
num = [0 for i in range(26)]
f.seek(0)
for i in range(nchars):
    c = f.read(1)
    if not c:
        break
    if ord(c) < ord_a or ord(c) > ord_z:
        continue
    num[ord(c) - ord_a] += 1
f.close()

# for each character, display its frequency in the text
for i in range(26):
    print("{}: {:.2f} %".format(chr(ord_a + i), num[i] * 100 / nchars))

