import csv
num=(input("enter number"))
#this will print values in incidents file 
def offenses():
        
    f = open("incidents.csv","rt")
    r=csv.reader(f)
    m=[]
    for row in r:
        try:
            if(int(row[3]) not in m):
                m.append(row[3])
        except ValueError:
            pass
    result_dict = dict( [ (i, m.count(i)) for i in set(m) ] )
    #print(result_dict)
    #counter dictionary prints offenses file
    f1 = open("offenses.csv","rt")
    r1=csv.reader(f1)
    counter={}
    for row1 in r1:
            counter.update({row1[0]:row1[1]})
    #print(counter)
    del counter ['Offense']
    #two for loops appending
    d5={}
    for z in result_dict:
        for z in counter:
            d5.update({counter[z]:result_dict[z]})
    for k,v in sorted(d5.items()):
        print(k,v)
            
            

#zipcode program
def zipcode():
    f = open("incidents.csv","rt")
    r=csv.reader(f)
    k=[]
    for row in r:
        try:
            if(int(row[4]) not in k):
                k.append(row[4])
        except ValueError:
            pass
    result_dict = dict( [ (i, k.count(i)) for i in set(k) ] )
    print("1:summary by zipcode")
    for key,value in sorted(result_dict.items()):
        
        print(key,value)
    
if(num=='1'):
    print("1.summary by zipcode")
    zipcode()
elif(num=='2'):
    print("2.victium count by offense type ")
    offenses()
elif(num=='Q'):
    print(".Q.QUIT")
    quit()
else: 
     print("you must choose one of the selections 1,2,Q")








   
    
    

             
    
