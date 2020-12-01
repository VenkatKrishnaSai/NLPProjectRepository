# -*- coding: utf-8 -*-

import pandas as pd

df_entities = pd.read_csv(r"chemprot_training_entities.tsv",sep='\t',names=["DOC ID","Term Number", "Attribute Type","Start Position", "End Position", "Name"])

df_relations = pd.read_csv(r"chemprot_training_relations.tsv",sep='\t',names=["DOC ID","Relation ID", "Relation Type","Relation Name", "Term 1", "Term 2"])

df_abstract = pd.read_csv(r"chemprot_training_abstracts.tsv",sep='\t',names=["DOC ID","text1","text2"])

df_automated_data= df_relations



#df_automated_data=df_relations.sample(frac=1)


abstrct_dict={}
def creatDict(row) :
#    print(row)
    abstrct_dict[row['DOC ID']]=row['text1'] + row['text2'] 
    #    print("--",row)

df_abstract.apply(creatDict,axis=1)




dfpart1 = df_automated_data.iloc[4000:4500,:]

DATASET_final=dfpart1.copy(deep='True')

DATASET_final['abstract']=['']*len(DATASET_final)



#
column_names = ["text","question","answer_term"]

data_bert = pd.DataFrame(columns = column_names)
#
#
#








def checkEnt(ID,T1,T2,rel) :
    x=""
    y=""
#    print(t1,t2)
    row=[]
    
    df_check = df_entities[df_entities['DOC ID']==ID]
    
    ans_df = df_check[df_check['Term Number']==T2]
#    print(ans_df)
    
    start_pos =ans_df.iloc[0]['Start Position']
    end_pos = ans_df.iloc[0]['End Position']
    for index, row in df_check.iterrows():
        if row['DOC ID']==ID and row['Term Number']==T1 :
            x=row['Name']
            break
        
    for index, row in df_check.iterrows():
        if row['DOC ID']==ID and row['Term Number']==T2  :
            y=row['Name']
            break
#            print(x)        
#    X1.append(x)
#    Y1.append(y)
#    REL.append(rel)

#    print("x=",X1)
#    print("y=",Y1)
    
#    print(abstrct_dict[row['DOC ID']])
            
        
    T1_df = df_check[df_check['Term Number']==T1]
    start_pos_t1 =T1_df.iloc[0]['Start Position']
    end_pos_t1 = T1_df.iloc[0]['End Position']
        
        
        
        
            
        
    return abstrct_dict[row['DOC ID']],x,y,rel,start_pos,end_pos,start_pos_t1,end_pos_t1



i=0
for index, row in dfpart1.iterrows():
#    print("index",index)
#    print(row['DOC ID'],row['Term 1'],row['Term 2'])
    id=row['DOC ID']
    rel=row['Relation Name']
    t1 = row['Term 1'].split(":")[1]
    t2 = row['Term 2'].split(":")[1]
    
    
#    print(t1,t2,rel)
#    print(checkEnt(id,t1,t2,rel))
    f=checkEnt(id,t1,t2,rel)
    text = f[0]
    x =f[1]
    y =f[2]
    rel=f[3]
    #sp=f[4]
    #ep=f[5]
    sp_t1=f[6]
    ep_t1=f[7]
    
#    print(text)
#    print(x)
#    print(y)
#    print("rel",rel)
    
    
#    
#    
    
    
#    print(text)
#    print("------------------")
#    print(x,"===",text[sp_t1-1:ep_t1-1])
#    print(y,"===",text[sp-1:ep-1])

    
    
    #min_sp =  min(sp-1,sp_t1-1)
    #max_ep = max(ep-1,ep_t1-1)
    subtext = text[sp_t1-1:ep_t1-1]
    print(subtext)
    subtext_toks = subtext.split()
    
    if(len(subtext.split()) == 0):
        continue
    
    mid_count = len(subtext.split())
    
    left_text = text[0:sp_t1-1]
    right_text = text[ep_t1:]

    
#    print("--",text)
#    print("--",left_text)
#    
    left_tok = left_text.split()
    right_tok = right_text.split()
    
    total_toks = 100
    
    remain_toks= int((total_toks -  mid_count)/2)
    
    
    left_text_toks = left_tok[-remain_toks:]
    finalTextLeft = ""
    for i in range(0,len(left_text_toks)):
        finalTextLeft = finalTextLeft + " "+ left_text_toks[i]
#    subtext_toks
    right_text_toks = right_tok[:remain_toks]
    finalTextRight = ""
    for i in range(0,len(right_text_toks)):
        finalTextRight = finalTextRight + " "+ right_text_toks[i]
   
    
    
    
    
#    print(left_text_toks,subtext_toks,right_text_toks)
#    
#    print(len(subtext_toks))
    
    newtokens = left_text_toks + subtext_toks + right_text_toks
    
    newtext=""
    
    for t in newtokens : 
        newtext+=" "+t
        
        
    #####################
    """compareText = ""
    newsp = 0
    newep = 0
    if(len(y.split()) > 1):
        for i in range(0,len(y.split())):
            compareText = compareText + " "+ subtext_toks[i]
        compareText = compareText[1:]
    else:
        compareText = subtext_toks[0]
        
    compareTextLast = ""
    if(len(y.split()) > 1):
        for k in range(len(y.split()),0,-1):
            compareTextLast = compareTextLast + " "+ subtext_toks[len(subtext_toks) - k]
        compareTextLast = compareTextLast[1:]
    else:
        compareTextLast = subtext_toks[len(subtext_toks) - 1]
    print(y)
    print(compareText)
    print(compareTextLast)
    if compareText == y:
        newsp = len(finalTextLeft)+2
        newep = newsp + len(y)
    elif compareTextLast == y:
        print(len(finalTextLeft),len(subtext),len(y))
        newsp = len(finalTextLeft)+len(subtext) - len(y)+2
        newep = len(finalTextLeft)+len(subtext)+1
        
    
    print(subtext)
    print(newtext)
    print(newsp , newep)"""
    
    print("newtext",newtext)
    print("-----",x,y)
    
    newtext_toks = newtext.split()
    y_toks = y.split()
    print(y_toks)
    s = ""
    newsp = -1
    newep = -1
    if len(y_toks) == 1:
        for new_tok in newtext_toks:
            s += new_tok+" "
            if new_tok == y_toks[0]:
               newsp=len(s)-len(y)
               newep=len(s)
               break
    else:
        p = ""
        for k in range(0,len(newtext_toks)-len(y_toks)):
            p += newtext_toks[k]+" "
            len_tok = ""
            for j in range(0,len(y_toks)):
                len_tok += " "+newtext_toks[k+j]
            len_tok = len_tok[1:]
            if len_tok == y:
                
                newsp = len(p)-len(y)+len(len_tok)-len(newtext_toks[k])
                newep = len(p)+len(len_tok)-len(newtext_toks[k])
                break
    
    
    ######################
    print(newsp,newep)
    print("answer"+newtext[newsp:newep])  
    
        
        
        
    
    
    
#    print(newtext)
      
    data_bert = data_bert.append({'text':newtext,'question': x +" acts as "+ rel+" for what entity? ",'answer_term':y ,'sp':newsp,'ep':newep}, ignore_index=True)    
   
    
    
    print(x)
    print(y)






    
#    DATASET_final.abstract.iloc[i]=checkEnt(id,t1,t2,rel)
    i=i+1
    
data_bert.to_csv('data_bert_100.csv',index=False)


    
###################################################################    















