from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Simple message exchange
meta = 5*str(rank)
msg = ""

if rank % 2 == 0:
    # even rank
    comm.send(meta, dest = rank + 1)
    msg = comm.recv(source = rank + 1)
elif rank % 2 == 1:
    # odd rank
    msg = comm.recv(source = rank - 1)
    comm.send(meta, dest = rank - 1)

print("Rank {} received message : {}".format(rank, msg))
