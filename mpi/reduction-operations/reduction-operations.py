from mpi4py import MPI
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Variable is initialized to rank number
var = rank

# Sum
sum = comm.reduce(var, op=MPI.SUM, root=0)
prod = comm.reduce(var, op=MPI.PROD, root=0)
max = comm.reduce(var, op=MPI.MAX, root=0)

if rank == 0:
    print("Sum is {}".format(sum))
    print("Product is {}".format(prod))
    print("Max is {}".format(max))

