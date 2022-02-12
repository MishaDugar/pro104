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

#mean 
n=len(newdata)
total=0
for x in newdata :
    total+=x 

mean=total/n 
print("mean"+str(mean))    





