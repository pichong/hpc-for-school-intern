from mpi4py import MPI
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Send and receive buffer
msg = ""

tgt = rank + 1
src = rank - 1
if rank == 0:
    msg = str(rank)
    comm.send(msg, dest=tgt)
elif rank != size - 1:
    msg = comm.recv(source=src)
    msg = msg + "-" + str(rank)
    comm.send(msg, dest=tgt)
else:
    msg = comm.recv(source=src)
    msg = msg + "-" + str(rank)
    print("Rank {} received message: {}".format(rank, msg))


