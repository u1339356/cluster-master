#hello.py
from openmpi/mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print "hello world from process ", rank


#yum install openmpi-devel
#yum install mpi4py-openmpi

