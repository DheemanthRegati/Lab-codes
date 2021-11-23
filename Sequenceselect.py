#Read introduction in the other python file for documentation. 
#ENSURE findseq.py is in same folder as this. 
#DO NOT EDIT FINDSEQ.PY AT ANY COST!!!!
from pymol import cmd #, stored # This is the pymol library
from findseq import * #Importing functions from findseq.py

array1 = ['2vbc.pdb','2bhr.pdb','2qeq.pdb','2wv9.pdb','6adw.pdb','1yks.pdb','7jno.pdb','2z83.pdb']#,'5i2s.pdb','vsvgmonomer.pdb'] #Array of pdbfile to be edited, P.S. ALL FILES NEED TO BE PRESENT BEFOREHAND 
array2 = ['...[RK][RK][STGA]....','...QR[STGA]....']#,'[ACD]y.','YT[AD]'] #Array of list of Regex notations of cleavage sites
# FETCH FUNCTION DISABLED
for x in array1:
    cmd.load(x) #Loading files
    for i,y in enumerate(array2):
        case= x.split('.')[0]
        userSelection = 'CS' + x.split('.')[0]+ str(i)
        findseq(y,case,userSelection) 
        #findseq('[LIHD]i.' ,x.split('.')[0],'Cleavage_site' + x.split('.')[0],1,1) # 1,1 refers to hetatm and first instance. REad 
        #documentation in findseq.py
        cmd.color('white',userSelection) #ALL selections are white for now

        stored.residues = set()
        cmd.iterate(selector.process(userSelection), 'stored.residues.add(resv)')
        tempset = []
        for r in stored.residues:
            tempset.append(r)
        tempset.sort()
        #In the following part we are trying to separate the selections into individual parts. 
        #As we are trying to search for a motif in a PDB file, all the similar motifs gets selected as a single selection
        #this part is okay for viewing the motifs but not for calculating the avarage B-factor.
         
          # inthe following part we are trying to separate the individual selctions by considering them as separate non overlapping strech of residues
        discona,disconb = [],[]
        for ind,a in enumerate(tempset):
            if a != tempset[ind-1]+1:
            # here we are trying to findout the first residue of a selection by finding out that residue whose index is not exactly 1 more than its previous one
         
                discona.append(a)
            if a == tempset[-1]:
                disconb.append(a)
                break
                # here we want to end the loop to stop running at the very last residue of the chain.
            if a!= tempset[ind+1]-1:
                disconb.append(a)
                # here we are trying to findout the last residue of a selection by finding out that residue whose index is not exactly 1 less than its subsequent residue.
        for z in range(len(discona)):
            k = cmd.get_unused_name(userSelection)
            cmd.select(k,''+ case +'/ resi %d-%d' %(discona[z],disconb[z]))
            
