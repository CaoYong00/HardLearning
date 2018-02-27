
# coding: utf-8

# In[ ]:


#coding = utf-8


# In[5]:


import requests


# In[6]:


import itchat


# In[8]:


KEY = '54c0bca3c4d841238f953b4bfed1dac9'


# In[15]:


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {'key':KEY, 'info': msg, 'userid': '曹勇'}
    try:
        r = requests.post(apiUrl, data = data).json()
        return r.get('text')
    except:
        return


# In[18]:


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: '+ msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply


# In[ ]:


itchat.auto_login(hotReload = True)
itchat.run()


# In[ ]:


python3 main.py

