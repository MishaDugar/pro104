import csv 
from  collections import Counter

with open("HeightWeight.csv",newline='') as f:
    reader=csv.reader(f) 
    filedata=list(reader)

filedata.pop(0)

#sottting data to get the height of the people 
newdata=[]
for p in range(len(filedata)):
    n_num=filedata[p][2]
    newdata.append(float(n_num))

#mode 
data=Counter (newdata)
datarange={
    "50-60":0,
    "60-70":0,
    "70-80":0 

}

for height,occurrence in data.items():
    if 50<float(height)<60:
        datarange["50-60"]+=occurrence

    elif 60<float(height)<70:
        datarange["60-70"]+=occurrence

    elif  70<float(height)<80:
        datarange["70-80"]+=occurrence

moderange,modeoccurrence=0,0
for range,occurrence in datarange.items():
    if occurrence>modeoccurrence:
        moderange,modeoccurrence=[int(range.split("-")[0]),int(range.split("-")[1])],occurrence

mode=float((moderange[0]+moderange[1])/2)
print(mode)

