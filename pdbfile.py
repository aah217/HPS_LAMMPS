import pandas as pd
#read pdb by cols
"""
COLUMNS*        DATA  TYPE    FIELD        DEFINITION
-------------------------------------------------------------------------------------
 1 -  6        Record name   "ATOM  "
 7 - 11        Integer       serial       Atom  serial number.
13 - 16        Atom          name         Atom name.
17             Character     altLoc       Alternate location indicator.
18 - 20        Residue name  resName      Residue name.
22             Character     chainID      Chain identifier.
23 - 26        Integer       resSeq       Residue sequence number.
27             AChar         iCode        Code for insertion of residues.
31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
55 - 60        Real(6.2)     occupancy    Occupancy.
61 - 66        Real(6.2)     tempFactor   Temperature  factor.
77 - 78        LString(2)    element      Element symbol, right-justified.
79 - 80        LString(2)    charge       Charge  on the atom.
"""
#index references
ATOM = 0
serial = 1
name = 3
altloc = 4
resName = 5
chainID = 7
resSeq = 8
iCode = 9
x = 11
y = 12
z = 13
occupancy = 14
tempFactor = 15
element = 17
charge = 18

aadict = pd.read_csv("amino_acid_dict.csv", sep=",",header=0)
def find_aa_stat(what, where, equals):
    return aadict.loc[aadict[where]==equals][what].values[0]

def row(xyz=[0.0,0.0,0.0],aa="PRO",r=1,i=1):
    #default
    row = "ATOM      1  CA  PRO A   1       0.000   0.000   0.000  1.00 99.99           C  "
    this_row = split(row)
    this_row[x] = put(this_row[x],xyz[0])
    this_row[y] = put(this_row[y],xyz[1])
    this_row[z] = put(this_row[z],xyz[2])
    if len(aa)>1: this_row[resName] = put(this_row[resName],aa)
    else: this_row[resName] = put(this_row[resName],aaDict.get(aa,"PRO"))
    this_row[serial] = put(this_row[serial],i)
    this_row[resSeq] = put(this_row[resSeq],r)
    return this_row

def split(r):
    this_row = []
    l = len(r)
    if l>=6: this_row.append(r[:6])
    else: this_row.append(" "*6)
    if l>=11: this_row.append(r[6:11])
    else: this_row.append(" "*5)
    if l>=12: this_row.append(r[11:12])#blank
    else: this_row.append(" ")
    if l>=16: this_row.append(r[12:16])
    else: this_row.append(" "*4)
    if l>=17: this_row.append(r[16:17])
    else: this_row.append(" ")
    if l>=20: this_row.append(r[17:20])
    else: this_row.append(" "*3)
    if l>=21: this_row.append(r[20:21])#blank
    else: this_row.append(" ")
    if l>=22: this_row.append(r[21:22])
    else: this_row.append(" ")
    if l>=26: this_row.append(r[22:26])
    else: this_row.append(" "*4)
    if l>=27: this_row.append(r[26:27])
    else: this_row.append(" "*1)
    if l>=30: this_row.append(r[27:30])#blank
    else: this_row.append(" "*3)
    if l>=38: this_row.append(r[30:38])
    else: this_row.append(" "*8)
    if l>=46: this_row.append(r[38:46])
    else: this_row.append(" "*8)
    if l>=54: this_row.append(r[46:54])
    else: this_row.append(" "*8)
    if l>=60: this_row.append(r[54:60])
    else: this_row.append(" "*6)
    if l>=65: this_row.append(r[60:66])
    else: this_row.append(" "*6)
    if l>=76: this_row.append(r[66:76])#blank
    else: this_row.append(" "*10)
    if l>=78: this_row.append(r[76:78])
    else: this_row.append(" "*2)
    if l>=80: this_row.append(r[78:80])
    else: this_row.append(" "*2)
    return this_row

def put(place,val):
    s = str(val)
    if len(s) > len(place): s = s[:len(place)]
    return " "*(len(place)-len(s))+s
    
def join(row):
    return "".join(row)

def col(s,n):
    return " "*(n-len(s))+s