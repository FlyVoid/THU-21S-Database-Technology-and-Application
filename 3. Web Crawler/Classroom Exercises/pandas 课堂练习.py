import numpy as np
import pandas as pd

string = input().split('\n')

dic = {}

dicHeight = {}
dicWeight = {}

dicTotal = {'学号':[],'身高':[],'体重':[]}
listName = []

for s in string:
    s = s.split('\t')
    dic[s[0]] = int(s[1])
    
    dicHeight[s[0]] = int(s[2])
    dicWeight[s[0]] = int(s[3])
    
    dicTotal['学号'].append(int(s[1]))
    dicTotal['身高'].append(int(s[2]))
    dicTotal['体重'].append(int(s[3]))
    listName.append(s[0])
    
    
ser = pd.Series(dic)
df1 = pd.DataFrame([dic,dicHeight,dicWeight],['学号','身高','体重'])
df2 = pd.DataFrame(dicTotal,listName)



