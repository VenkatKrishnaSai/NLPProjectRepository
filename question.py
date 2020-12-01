# -*- coding: utf-8 -*-





import pandas as pd
data_bert_df = pd.read_csv(r"data_bert.csv")


from transformers import AutoTokenizer, TFAutoModelForQuestionAnswering
import tensorflow as tf
tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = TFAutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad", return_dict=True)




def tester(text , question, answer) :
  
        questions = [
           question
        ]
        for question in questions:
            inputs = tokenizer(question, text, add_special_tokens=True, return_tensors="tf")
            input_ids = inputs["input_ids"].numpy()[0]
            text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
            answer_scores = model(inputs)
            answer_start = tf.argmax(
                answer_scores["start_logits"], axis=1
            ).numpy()[0]  # Get the most likely beginning of answer with the argmax of the score
            answer_end = (
                tf.argmax(answer_scores["end_logits"], axis=1) + 1
            ).numpy()[0]  # Get the most likely end of answer with the argmax of the score
            answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
            print(f"Question: {question}")
            print(f"Answer: {answer}")








for index, row in data_bert_df.iterrows():
    text=row['text']
    question=row['question']
    answer=row['answer_term']
    tester(text , question, answer)
    
    
    
