from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD

#getting rank and size
rank = comm.Get_rank()
size = comm.Get_size()

#assign value 
val = 1

#calculate
val *= (rank+1)

#print rank and its current value
print("Rank %d has value %d" % (rank, val))

#gather result
res = comm.reduce(val, op=MPI.PROD, root=0)

#printing result of gathering
if rank == 0:
    print("Rank 0 worked out the total %d" %res)