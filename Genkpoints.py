import os.path
from numpy import *
data=loadtxt("input.dat", unpack='true')
nx=int(data[0,0])
ny=int(data[1,0])
nz=int(data[2,0])

nkpt=(nx+1)*(ny+1)*(nz+1)

fp2 = open("KPOINTS","w")
fp2.write("Explicit k-points list")
fp2.write('\n')
fp2.write("{}".format(nkpt))
fp2.write('\n')
fp2.write("Reciprocal lattice")  
fp2.write('\n')

for i in range(nx+1):
    for j in range(ny+1):
        for k in range(nz+1):
            fp2.write("  {:.6f}  {:.6f} {:.6f}  {}".format(i/nx,j/ny,k/nz,1))
            fp2.write('\n')
