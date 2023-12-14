import os
import sys
from openmpi.mpi4py import MPI

comm = MPI.COMM_WORLD
nranks = comm.Get_size()
rank = comm.Get_rank()

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
# each rank process a portion of the file
num = [0 for i in range(26)]
f.seek(rank * (nchars // nranks))
for i in range(nchars // nranks):
    c = f.read(1)
    if not c:
        break
    if ord(c) < ord_a or ord(c) > ord_z:
        continue
    num[ord(c) - ord_a] += 1
f.close()

# aggregate results
agg_num = [0 for i in range(26)]
for i in range(26):
    agg_num[i] = comm.reduce(num[i], op=MPI.SUM, root=0)

# for each character, display its frequency in the text
if rank == 0:
    for i in range(26):
        print("{}: {:.2f} %".format(chr(ord_a + i), agg_num[i] * 100 / nchars))

