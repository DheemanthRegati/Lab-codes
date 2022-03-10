import csv
def prevcheck(array,matrix,c):#check if condition has been repeated previously
    sa = set(array)
    k=0
    for i in matrix:
        k+=1
        si = set(i)
        if si == sa:
            print("match :",i,"at",k)
            c+=1 #updating total matches found
    return c


rows,exist = [],[]
with open('finalist.csv','r+') as data:
    text = csv.reader(data)
    for row in text:
        rows.append(row)
    count = 0
    for line in rows:
        res=prevcheck(line,exist,count)
        count=res
        exist.append(line)
    print("number of matches :",count)
