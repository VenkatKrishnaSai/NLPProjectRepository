# -*- coding: utf-8 -*-
import pandas as pd
data_bert_df = pd.read_csv(r"data_bert_100.csv")

#data_bert_df = data_bert_df.iloc[0:2,:]

# -1 to get the index
#data_bert_df.iloc[0]['text'][1551]



file = open("test_pavan.txt", "w", encoding="utf-8")
dollar_tokens_file = open("dev_dollar_venkatesh.txt", "w", encoding="utf-8")

#file.write() 


def splitter(row):
    
#    answer_term = row['answer_term']
    text = row['text']
    print(text)
    
    
    text2 =text
    question = row['question']#    answer_term_len = len(answer_term.split())
    
    sp=int(row['sp'])
    ep=int(row['ep'])
    
    if sp != -1 and ep != -1:
        pre_ans = text[:sp-1]
    
        ans_text1 = text[sp-1:ep]
    
        ans_tok = ans_text1.split()
    
        temp_ans=""
    
        for at in ans_tok :
            temp_ans+=" $$$" + at
            print(temp_ans)
        

    
    
        post_text = text[ep:]
    
    
        text= pre_ans +" " + temp_ans +" "+ post_text
    
    
    
        print("--------",ans_text1)

    
    ###############
    """
    sp_t1=int(row['sp_t1'])
    ep_t1=int(row['ep_t1'])
    
    
    pre_ans = text2[:sp_t1-1]
    
    ans_text2 = text2[sp_t1-1:ep_t1]
    
#    print("--------",ans_text2)
    
    ans_tok = ans_text2.split()
    
    temp_ans=""
    
    for at in ans_tok :
        temp_ans+=" ^^^" + at
        
        

    
    
    post_text = text2[ep_t1:]
    
    
    text2= pre_ans +" " + temp_ans + " "+ post_text
    
    
    print(text)
    dol_tokens = text.split()
    cap_tokens = text2.split()
    
    
    if len(dol_tokens)!=len(cap_tokens):
        return
    
    
    
    res_tok=[]
    
    for i in range(len(dol_tokens)) :
        print(dol_tokens[i],cap_tokens[i])
        if '$$$' in dol_tokens[i] :
            res_tok.append(dol_tokens[i])
            pos1 =i
        elif  '^^^' in cap_tokens[i]:
            
            res_tok.append(cap_tokens[i][3:]) ### cap tokens but remove tokens now
            pos2 =i

            

            
        else :
#            if dol_tokens[i] != cap_tokens[i]:
#                pass
            res_tok.append(dol_tokens[i])
            
            
    
    
    
#    print(res_tok)
#    print(pos2-pos1)
    subtoken_len= max(pos1-pos2,0) + 1
    target_len =90
    remain_len= int((target_len-subtoken_len)/2)
    
    st = min(pos1,pos2)
    ed = max(pos1,pos2)

    
    print("===================")
    
#    print(st)
#    print(res_tok[st-remain_len:st])
#    print(res_tok[st:ed])
#    print(res_tok[ed:remain_len+ed])
#
#    
    
    #################
#    print(res_tok)
#    print(text2)
    
    
    
    text =""
    
    com = res_tok[st-remain_len:st] + res_tok[st:ed] + res_tok[ed:remain_len+ed]
    print(len(res_tok[st-remain_len:st] + res_tok[st:ed] + res_tok[ed:remain_len+ed]))
    for t in com :
        text+=t+" "
    """
    
    
    
    
    
    
    
    
    
    
    
    

  
    print("====",question)
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
    

        

    dollar_tokens_file.write(dollar_tokens) 

    print("tok:",len(ans_tokens.split('\n')))

#    print("------------",len(tokens))


i=0
for index, row in data_bert_df.iterrows():
    print(index)
    splitter(row)
    dollar_tokens_file.write("\n") 

    file.write("\n")
    

#    print(row)


    
file.close() 

dollar_tokens_file.close()
