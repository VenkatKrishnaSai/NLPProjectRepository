# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import pandas as pd

df_entities = pd.read_csv(r"chemprot_training_entities.tsv",sep='\t',names=["DOC ID","Term Number", "Attribute Type","Start Position", "End Position", "Name"])

df_relations = pd.read_csv(r"chemprot_training_relations.tsv",sep='\t',names=["DOC ID","Relation ID", "Relation Type","Relation Name", "Term 1", "Term 2"])

df_abstract = pd.read_csv(r"chemprot_training_abstracts.tsv",sep='\t',names=["DOC ID","text1","text2"])

df_automated_data= df_relations



df_automated_data=df_relations.sample(frac=1)


abstrct_dict={}
def creatDict(row) :
#    print(row)
    abstrct_dict[row['DOC ID']]=row['text1'] + row['text2'] 
    #    print("--",row)

df_abstract.apply(creatDict,axis=1)






#
column_names = ["text","question","answer_term"]

data_bert = pd.DataFrame(columns = column_names)

###################################################################    

def checkEnt(ID,T1,T2,rel) :
    x=""
    y=""
#    print(t1,t2)
    row=[]
    
    df_check = df_entities[df_entities['DOC ID']==ID]
    
#    ans_df = df_check[df_check['Term Number']==T2]
#    print(ans_df)
    

    for index, row in df_check.iterrows():
        if row['DOC ID']==ID and row['Term Number']==T1 :
            x=row['Name']
            break
        

        
    T1_df = df_check[df_check['Term Number']==T1]
    start_pos_t1 =T1_df.iloc[0]['Start Position']
    end_pos_t1 = T1_df.iloc[0]['End Position']
        
        

    return abstrct_dict[row['DOC ID']],x,y,rel,0,0,start_pos_t1,end_pos_t1

###############################################################################



















###################################################################
all_ids = set(df_relations['DOC ID'])
column_names = ['DOC ID', 'Relation ID', 'Relation Type', 'Relation Name', 'Term 1','Term 2']
data_wrong = pd.DataFrame(columns = column_names)

def wrong_rel(docid) :
    column_names = ['DOC ID', 'Relation ID', 'Relation Type', 'Relation Name', 'Term 1','Term 2']

    data_wrong = pd.DataFrame(columns = column_names)
    
        
    doc_df = df_relations[df_relations['DOC ID']==docid]
    
    
    all_rel = set(doc_df['Relation Name'])
    
    all_term1 = set(doc_df['Term 1'])
    
    
    rel_list = list(doc_df['Relation Name'])
    term1_list = list(doc_df['Term 1'])
    
    correct_rel =[]
    
    for i in range(len(rel_list)) :
        correct_rel.append([rel_list[i],term1_list[i]])
        
    
    


#    print(doc_df)
    
#    newrow= {'DOC ID' : docid, 'Relation ID': 'X' , 'Relation Type' : 'X' , 'Term 1': t, 'Term 2' : "None"}
    for rel in all_rel :
        for t in all_term1 :   
            if [rel,t] in correct_rel :
                continue
            
            newrow={'DOC ID' : docid, 'Relation ID': 'X' , 'Relation Type' : 'X' , 'Relation Name': rel,'Term 1': t, 'Term 2' : "None"}
            data_wrong=data_wrong.append(newrow, ignore_index=True)
            
    
#    print(data_wrong)
    return data_wrong    
    
    
    
    
x =list(all_ids)


for docid in  x[200:300] :
    dx =wrong_rel(docid)
    data_wrong=data_wrong.append(dx, ignore_index=True)
    


######################################################################


data_wrong=data_wrong[1:20]
i=0
for index, row in data_wrong.iterrows():
#    print("index",index)
#    print(row['DOC ID'],row['Term 1'],row['Term 2'])
    id=row['DOC ID']
    rel=row['Relation Name']
    t1 = row['Term 1'].split(":")[1]
#    t2 = row['Term 2'].split(":")[1]
    
    
#    print(t1,t2,rel)
#    print(checkEnt(id,t1,t2,rel))
    f=checkEnt(id,t1,0,rel)
    text = f[0]
    x =f[1]
    y =f[2]
    rel=f[3]
    sp=f[4]
    ep=f[5]
    sp_t1=f[6]
    ep_t1=f[7]
 
    
    
    data_bert = data_bert.append({'text':text,'question': x +" acts as "+ rel+" for what entity? ",'answer_term':y ,'sp':sp,'ep':ep,'sp_t1':sp_t1,'ep_t1':ep_t1}, ignore_index=True)    
   
    
    
    print(x)
    print(y)



#    DATASET_final.abstract.iloc[i]=checkEnt(id,t1,t2,rel)
    i=i+1
    
data_bert.to_csv('wrong_relations.csv',index=False)



#######################################
file = open("wrong_relations_dev.txt", "w", encoding="utf-8")


######################################

def splitter(row):
    
#    answer_term = row['answer_term']
    text = row['text']
    print(text)
    
    
    text2 =text
    question = row['question']#    answer_term_len = len(answer_term.split())
    
    sp_t1=int(row['sp_t1'])
    ep_t1=int(row['ep_t1'])
    
    
    subtext = text[sp_t1-1:ep_t1-1]
    print(subtext)
    subtext_toks = subtext.split()
    
#    if(len(subtext.split()) == 0):
#        continue
    
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
    
    
    print("====",question)
    text=newtext
    text = question +" "+ text
    tokens = text.split()
    flag=0
    
    
    ans_tokens=""
    dollar_tokens=""
    

    for tok in tokens :   
#        print(tok)
        
#        res = re.sub(r'[.,]', '', tok) 
#        str.startswith( 'this' )
#        print(tok)
        if tok[-1]=='.' or tok[-1]==',' or tok[-1]==':' or tok[-1]=='?' or tok[-1]=='/' :
            if tok.startswith("$$$")== True and flag==0 : 
                ans_tokens+=tok[3:-1]+" "+"B"
                dollar_tokens+=tok[:-1]+" "+"B"
                file.write(tok[3:-1]+" "+"B") 
                flag=1
            elif  tok.startswith("$$$")== True and flag==1 : 
                
                file.write(tok[3:-1]+" "+"I") 
                ans_tokens+=tok[3:-1]+" "+"I"
                dollar_tokens+=tok[:-1]+" "+"I"

           
            else : 
                file.write(tok[:-1]+" "+"O") 
                ans_tokens+=tok[:-1]+" "+"O"
                dollar_tokens+=tok[:-1]+" "+"O"

                
                
                
                
            file.write("\n") 
            ans_tokens+="\n"
            dollar_tokens+="\n"


            file.write(tok[-1]+" "+"O") 
            ans_tokens+=tok[-1]+" "+"O"
            dollar_tokens+=tok[-1]+" "+"O"

            

        else :   
            if tok.startswith("$$$")== True and flag==0 :                
                file.write(tok[3:]+" "+"B") 
                ans_tokens+=tok[3:]+" "+"B"
                dollar_tokens+=tok[:]+" "+"B"
                flag=1
            elif  tok.startswith("$$$")== True and flag==1 :                
                file.write(tok[3:]+" "+"I") 
                ans_tokens+=tok[3:]+" "+"I"
                dollar_tokens+=tok[:]+" "+"I"
            else :
                file.write(tok[:]+" "+"O") 
                ans_tokens+=tok[:]+" "+"O"
                dollar_tokens+=tok[:]+" "+"O"


                
        file.write("\n") 
        ans_tokens+="\n"
        dollar_tokens+="\n"
    

        

#    dollar_tokens_file.write(dollar_tokens) 

    print("tok:",len(ans_tokens.split('\n')))

#    print("------------",len(tokens))


i=0
for index, row in data_bert.iterrows():
    splitter(row)
#    dollar_tokens_file.write("\n") 

    file.write("\n")
    

#    print(row)
    
    
file.close() 


#############################################################


file1 = open('test.txt', 'r') 
Lines = file1.readlines() 
i=0
for l in Lines :
    print(i+1)
    i=i+1
    print(l)





















