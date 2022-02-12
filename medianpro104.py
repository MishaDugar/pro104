import csv 

with open("HeightWeight.csv",newline='') as f:
    reader=csv.reader(f) 
    filedata=list(reader)

filedata.pop(0)

#sottting data to get the height of the people 
newdata=[]
for p in range(len(filedata)):
    n_num=filedata[p][2]
    newdata.append(float(n_num))

#medain 
n=len(newdata)
newdata.sort()

if n%2==0:
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2

else:
    median=newdata[n//2]  

print("median="+str(median)) 





