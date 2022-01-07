import csv
import pandas as pd
file1="Bright_stars.csv"
file2="unit_converted_stars.csv"
d1=[]
d2=[]
with open(file1,"r",encoding="utf8") as f:
    reader=csv.reader(f)
    for i in reader :
        d1.append(i)
with open(file2,"r",encoding="utf8") as f:
    reader=csv.reader(f)
    for i in reader :
        d2.append(i)
h1=d1[0]
h2=d2[0]
p1=d1[1:]
p2=d2[1:]
h=h1+h2
p=[]
for i in p1:
    p.append(i)
for j in p2:
    p.append(j)
with open("total_stars.csv","w",encoding="utf8")as f:
    writer=csv.writer(f)
    writer.writerow(h)
    writer.writerows(p)
df=pd.read_csv("total_stars.csv")
df.tail(8)