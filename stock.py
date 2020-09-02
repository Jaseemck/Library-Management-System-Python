def stock():
    global bookName
    global authorName
    global issued
    bookName=[]
    authorName=[]
    issued=[]
    with open("stock.txt","r") as f:   
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    bookName.append(a)
                elif(ind==1):
                    authorName.append(a)
                elif(ind==2):
                    issued.append(a)
                ind+=1
