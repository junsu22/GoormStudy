#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import os
os.environ['TF_USE_LEGACY_KERAS'] = '1'

import tensorflow as tf

# GPU 메모리 점진적 할당
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    tf.config.experimental.set_memory_growth(gpus[0], True)


# In[2]:


# pip install transformers==4.35.0


# In[3]:


# pip install --upgrade jupyter ipywidgets


# In[4]:


import warnings
warnings.filterwarnings('ignore')


# In[5]:


get_ipython().system('pip install transformers')


# In[6]:


# pip install protobuf==3.20.3


# In[7]:


import tensorflow as tf
from transformers import AutoTokenizer
from transformers import TFGPT2LMHeadModel


# In[8]:


tokenizer = AutoTokenizer.from_pretrained('skt/kogpt2-base-v2', bos_token='</s>', eos_token='</s>', pad_token='<pad>')
model = TFGPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2', from_pt=True)


# In[9]:


print(tokenizer.bos_token_id)
print(tokenizer.eos_token_id)
print(tokenizer.pad_token_id)
print('-' * 10)
print(tokenizer.decode(1))
print(tokenizer.decode(2))
print(tokenizer.decode(3))
print(tokenizer.decode(4))


# In[10]:


import pandas as pd
import tqdm
import urllib.request


# In[11]:


urllib.request.urlretrieve("https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv", filename="ChatBotData.csv")
train_data = pd.read_csv('ChatBotData.csv')


# In[12]:


len(train_data)


# In[13]:


batch_size = 32


# In[14]:


def get_chat_data():
  for question, answer in zip(train_data.Q.to_list(), train_data.A.to_list()):
    bos_token = [tokenizer.bos_token_id]
    eos_token = [tokenizer.eos_token_id]
    sent = tokenizer.encode('<usr>' + question + '<sys>' + answer) 
    yield bos_token + sent + eos_token


# In[15]:


dataset = tf.data.Dataset.from_generator(get_chat_data, output_types=tf.int32)


# In[16]:


dataset = dataset.padded_batch(batch_size=batch_size, padded_shapes=(None,), padding_values=tokenizer.pad_token_id)


# In[17]:


for batch in dataset:
    print(batch)
    break


# In[18]:


tokenizer.decode(batch[0])


# In[19]:


print(batch[0])


# In[20]:


print(tokenizer.encode('</s><usr> 12시 땡!<sys> 하루가 또 가네요.</s><pad><pad><pad><pad><pad><pad><pad><pad><pad><pad><pad><pad><pad><pad><pad>'))


# In[21]:


adam = tf.keras.optimizers.Adam(learning_rate=3e-5, epsilon=1e-08)


# In[ ]:


steps = len(train_data) // batch_size + 1
print(steps)


# In[ ]:


EPOCHS = 3

for epoch in range(EPOCHS):
  epoch_loss = 0

  for batch in tqdm.tqdm_notebook(dataset, total=steps):
      with tf.GradientTape() as tape:
          result = model(batch, labels=batch)
          loss = result[0]
          batch_loss = tf.reduce_mean(loss)
          
      grads = tape.gradient(batch_loss, model.trainable_variables)
      adam.apply_gradients(zip(grads, model.trainable_variables))
      epoch_loss += batch_loss / steps

  print('[Epoch: {:>4}] cost = {:>.9}'.format(epoch + 1, epoch_loss))


# In[ ]:


import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))


# In[ ]:


text = '오늘도 좋은 하루!'


# In[ ]:


sent = '<usr>' + text + '<sys>'


# In[ ]:


input_ids = [tokenizer.bos_token_id] + tokenizer.encode(sent)
input_ids = tf.convert_to_tensor([input_ids])


# In[ ]:


output = model.generate(input_ids, max_length=50, early_stopping=True, eos_token_id=tokenizer.eos_token_id)


# In[ ]:


decoded_sentence = tokenizer.decode(output[0].numpy().tolist())


# In[ ]:


decoded_sentence.split('<sys> ')[1].replace('</s>', '')


# In[ ]:


output = model.generate(input_ids, max_length=50, do_sample=True, top_k=10)
tokenizer.decode(output[0].numpy().tolist())


# In[ ]:


def return_answer_by_chatbot(user_text):
  sent = '<usr>' + user_text + '<sys>'
  input_ids = [tokenizer.bos_token_id] + tokenizer.encode(sent)
  input_ids = tf.convert_to_tensor([input_ids])
  output = model.generate(input_ids, max_length=50, do_sample=True, top_k=20)
  sentence = tokenizer.decode(output[0].numpy().tolist())
  chatbot_response = sentence.split('<sys> ')[1].replace('</s>', '')
  return chatbot_response


# In[ ]:


return_answer_by_chatbot('안녕! 반가워~')


# In[ ]:


return_answer_by_chatbot('너는 누구야?')


# In[ ]:


return_answer_by_chatbot('사랑해')


# In[ ]:


return_answer_by_chatbot('나랑 영화보자')


# In[ ]:


return_answer_by_chatbot('너무 심심한데 나랑 놀자')


# In[ ]:


return_answer_by_chatbot('영화 해리포터 재밌어?')


# In[ ]:


return_answer_by_chatbot('너 딥 러닝 잘해?')


# In[ ]:


return_answer_by_chatbot('너 취했어?')


# In[ ]:


return_answer_by_chatbot('커피 한 잔 할까?')

