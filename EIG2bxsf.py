
import os.path
from numpy import *

filename=os.path.abspath("EIGENVAL")
fp=open(filename,"r")

for i in range(1,7):
  line=fp.readline();
 
linetmp=line.split()
nkpt=int(linetmp[1])
nband=int(linetmp[2])
######################read the Eigenval
kpt=([]);
Eigen=([]);
line=fp.readline();
for i in range(nkpt):
    for j in range(nband+2):
        line=fp.readline();
        if j==0:
            linetmp=line.split()
            kpt.append(linetmp)
        elif (j !=0 and j !=nband+1):
              linetmp=line.split()
              Eigen.append(linetmp)
        
kpt=array(kpt)
Eigen=array(Eigen)
Energy=Eigen[:,1]
EIG=Energy.reshape(nkpt,nband)
################

data=loadtxt("input.dat", unpack='true')
nx=int(data[0,0])
ny=int(data[1,0])
nz=int(data[2,0])
E_fermi=data[0,1]
nkpt=(nx+1)*(ny+1)*(nz+1)

fp2 = open("Python.bxsf","w")
fp2.write(" BEGIN_INFO")
fp2.write('\n')
fp2.write(" #")
fp2.write('\n')
fp2.write(" # this is a Band-XCRYSDEN-Structure-File")
fp2.write('\n')
fp2.write(" # aimed at Visualization of Fermi Surface")
fp2.write('\n')
fp2.write(" #")
fp2.write('\n')
fp2.write(' # Case:   ***.bxsf')
fp2.write('\n')
fp2.write(" #")
fp2.write('\n')
fp2.write("{} {}"  .format(" Fermi Energy:",E_fermi))
fp2.write('\n')
fp2.write(" END_INFO")
fp2.write('\n')
fp2.write(" BEGIN_BLOCK_BANDGRID_3D")
fp2.write('\n')
fp2.write(" band_energies")
fp2.write('\n')
fp2.write(" BANDGRID_3D_BANDS")
fp2.write('\n')

fp2.write("  {}".format(nband))
fp2.write('\n')
fp2.write("  {}   {}    {}".format(nx+1,ny+1,nz+1))
fp2.write('\n')
fp2.write("  0.000000  0.000000  0.000000")
fp2.write('\n')
fp2.write("  {:.6f}  {:.6f}  {:.6f}".format(data[0,2],data[1,2],data[2,2]))
fp2.write('\n')
fp2.write("  {:.6f}  {:.6f}  {:.6f}".format(data[0,3],data[1,3],data[2,3]))
fp2.write('\n')
fp2.write("  {:.6f}  {:.6f}  {:.6f}".format(data[0,4],data[1,4],data[2,4]))
for i in range(nband):
    fp2.write(  "\n {}  {}  \n".format("BAND:",i+1));
    for j in range(nkpt):
        if   mod(j+1,6)!=0:
            fp2.write(  " {}".format(EIG[j,i]));
        elif mod(j+1,6)==0:
            fp2.write(  " {} \n".format(EIG[j,i]));
        
fp2.write("\n END_BANDGRID_3D")
fp2.write("\n END_BLOCK_BANDGRID_3D")




