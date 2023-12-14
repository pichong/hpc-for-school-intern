import os
import sys

# open the file
f = open(sys.argv[1], 'r')

# get the number of characters
f.seek(0, os.SEEK_END)
nchars = f.tell()

# process text character by character
num_e = 0
f.seek(0)
for i in range(nchars):
    c = f.read(1)
    if c == 'e':
        num_e += 1
f.close()

# display number of 'e' characters and its frequency in the text
freq = num_e * 100 / nchars
print("{} 'e' characters, {:.2f} % frequency".format(num_e, freq))

