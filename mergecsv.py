import csv
csvlist = ['JCSG.csv','PACT.csv','Wizard12.csv','Wizard34.csv','JB.csv','FS.csv']
array = []
for item in csvlist:
    with open(item) as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            print(row['Combined'])
            array.append(row['Combined'])

    with open('finalist.csv', 'w+') as f:
        for row in array:
            f.write(row)
            f.write("\n")