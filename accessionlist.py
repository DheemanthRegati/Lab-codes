file=open('denv_isolates.fa','r')
#temp=file.read()
#file.close()

txt=open('outputdet.txt','w+')
for line in file:
    if line[0]=='>':
        if line[1:10] not in txt:
            txt.write(line)#[1:10])
        #print(line[1:10])
        #txt.write(line[1:10])
txt.close()
file.close()
