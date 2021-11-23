from pymol import cmd#,stored

select = ['10ns']#,'lipid','peptide']
for sel in select:
    k = cmd.count_states(sel)
    for i in range(k):
        model = cmd.get_model(sel,i)
        x, y, z,tm = 0, 0, 0, 0.0
        count = 0
        for a in model.atom:
            try:
                m = a.get_mass()
                x += a.coord[0] * m
                y += a.coord[1] * m
                z += a.coord[2] * m
                tm += m
                count +=1
               # pass
            except KeyError :
                x += a.coord[0] * 35.453
                y += a.coord[1] * 35.453
                z += a.coord[2] * 35.453
                tm += 35.453
                count += 1
        print(sel, i, x/tm,y/tm,z/tm,count)
