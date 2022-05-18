import sys
import pdbfile as p

file = sys.argv[1]
mol_num = sys.argv[2]
mol_size = sys.argv[3]
idx_shift = (int(mol_num)-1)*int(mol_size)
x_shift = sys.argv[4]
y_shift = sys.argv[5]
z_shift = sys.argv[6]
    
delta = 0

def str_add (str1,str2):
    return str(round(float(str1)+float(str2),2))

with open(file,'r') as f:        
    for i,r in enumerate(f):
        this_row = p.split(r.strip())
        if this_row[p.ATOM].strip() != "ATOM":
            delta = delta + 1
            continue
        this_idx = p.col(str(i + idx_shift + 1 - delta),4)
        this_type = p.find_aa_stat("type","tla",this_row[p.resName])
        this_charge = p.find_aa_stat("charge","tla",this_row[p.resName])
        x = str_add(this_row[p.x],x_shift)
        y = str_add(this_row[p.y],y_shift)
        z = str_add(this_row[p.z],z_shift)
        print("\t"+this_idx+"\t"+mol_num+"\t"+str(this_type)+"\t"+str(this_charge)+"\t"+x+"\t"+y+"\t"+z)
        