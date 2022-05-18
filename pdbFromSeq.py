import sys
import pdbfile as p

file = sys.argv[1]
i = int(sys.argv[2])

with open(file) as f:
    for line in f:
        for c in line:
            c = c.strip()
            if len(c)>0:
                print(p.join(p.row([0.0,0.0,i*3.81],p.find_aa_stat("tla","abc",c),i,i)))
                i = i+1