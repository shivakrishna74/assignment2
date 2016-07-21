import csv
import calendar

d={}
k=[]

try:
    f=open('precipitation.csv','rt')
    r=csv.reader(f)
    for row in f:
        if(row[0:6] not in k):
            k.append(row[0:6])
        else:
            pass

    f.close()
            
    p=open('precipitation.csv','rt')
    m=csv.reader(p)

    i=0
    
    value=0.0

    for row in m:
        try:
            if(row[0][0:6] == k.__getitem__(i)):
                value += float(row[1])
                continue
            else:
                 i=i+1
                 pass
    
        except ValueError:
            pass

        d.update({k.__getitem__(i-1):value})
        value=0
    
        
    d.update({k.__getitem__(i):value})

    s=input("enter filename for writing")
    o=open(s,"wt",newline='')
    v=csv.writer(o)

    for key,value in sorted(d.items()):
        v.writerow([key,value])
    o.close()
 
except Exception:
    print("file not fund")

U=[]
c={}
try:
    j=open(s,"rt")
    y=csv.reader(j)

    for row in y:
        if (row[0][4:6] not in U):
            U.append(row[0][4:6])
        else:
            continue

    v = 0
    for a2 in U:
        a1=open(s,"rt")
        a3=csv.reader(a1)
        for row in a3:
            try:
                if(row[0][4:6]==a2):
                    v+=float(row[1])
                    continue
                else:
                    pass

            except ValueError:
                pass

            except IndexError:
                pass

        c.update({calendar.month_name[int(a2)]:(v/10)})
        v=0
    
    
    print("                                                 ")
    print("average monthly rainfall over period of 10 years")
    print("#############################################")
    months=['January','February','March','April','May','June','July','August','September','October','November','December']
    for k,v in (sorted(c.items(), key =lambda t:months.index(t[0]))):
        print (k,v)

except IOError:
    print("file not found")
