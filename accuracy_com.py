# -*- coding: utf-8 -*-

import pandas as pd


true_file = pd.read_csv("truth.txt",sep=" ",header=None)
#true_file =test_file.iloc[:,1]




predict_file = pd.read_csv("pred.txt",sep=" ",header=None)
#preidct_file =preidct_file.iloc[:,1]


X_t=[]
X_p=[]


for i in range(len(true_file)) :
    print(i)
    for j in range(max(0,i-100),min(i+100,len(predict_file))):
        if (predict_file.iloc[j][1] == "O" and true_file.iloc[i][1] == "B") or (predict_file.iloc[j][1] == "B" and true_file.iloc[i][1] == "O") or (predict_file.iloc[j][1] == "B" and true_file.iloc[i][1] == "B"):
            if predict_file.iloc[j][0] == true_file.iloc[i][0]:
                if predict_file.iloc[j-1][0] == true_file.iloc[i-1][0] and predict_file.iloc[j+1][0] == true_file.iloc[i+1][0]:
                    X_t.append(true_file.iloc[i][1])
                    X_p.append(predict_file.iloc[j][1])
                    break
        
                
                
        
           
"""import numpy as np
from sklearn.metrics import precision_recall_fscore_support

precision_recall_fscore_support(X_t, X_p, average='macro') """   

tp=0
fp=0
tn=0
fn=0
for i in range(0,len(X_t)):
    if (X_t[i]=='B' and X_p[i]=='B'):
        tp +=1
    elif (X_t[i]=='O' and X_p[i]=='B'):
        fp +=1
    elif (X_t[i]=='B' and X_p[i]=='O'):
        fn +=1
    else:
        tn +=1
precision=tp/(tp+fp)
print(precision)
recall = float(tp/(tp+fn))
F_measure = (2 * precision * recall) / (precision + recall)
#print(precision)
print(recall)
print(F_measure)

###############################


df = pd.DataFrame()
df['t']=X_t
df['p']=X_p