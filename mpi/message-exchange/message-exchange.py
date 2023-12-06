from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Simple message exchange
meta = 5*str(rank)
msg = ""

if rank == 0:
    comm.send(meta, dest=1)
    msg = comm.recv(source=1)
elif rank == 1:
    msg = comm.recv(source=0)
    comm.send(meta, dest=0)

print("Rank {} received message : {}".format(rank, msg))
