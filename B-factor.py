'''
Program to get average b-factor over a sequence of residues. Independent of Pymol.

'''
import math
import os

def Bfact(r1, r2, file):
    result = 0
    for row in file:
        if (row[23:26] >= r1 and row[23:26] <= r2) and (row[:4] == 'ATOM' or row[:4] == 'HETA'):
            result += getbfact(row) 
            #print('1 ',result)
            #print(int(r2) - int(r1))
    print(result)
    return result / ((int(r2) - int(r1)))
def getbfact(line):#function to give co-ordinates given atom no.
    var1 = float(line[61:66])
    #print('2 ',var1)
    return var1

pdb = open('3duz.pdb','r')
print(Bfact(' 25',' 27',pdb)) #Ensure that total length of input residue number is exactly 3. Add spaces in front if residue number is less than 100.
# print(int(r2) - int(r1))

#bjouxz