
# coding: utf-8

# In[1]:


import itchat


# In[2]:


itchat.login()


# In[3]:


friends = itchat.get_friends(update = True)[0:]


# In[20]:


male = female = other = 0


# In[23]:


for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1


# In[9]:


total = len(friends[1:])
print(total)


# In[24]:


male


# In[25]:


female


# In[26]:


print("男性好友:  %.2f%%" %(float(male)/total*100)+ "\n"+
"女性好友:  %.2f%%" %(float(female)/total*100)+ "\n"+
"不明性别好友:  %.2f%%" %(float(other)/total*100))


# In[27]:


def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


# In[28]:


NickName = get_var('NickName')
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')


# In[29]:


from pandas import DataFrame


# In[31]:


data = {'NickName':NickName, 'Sex':Sex, 'Provinnce':Province, 'City':City, 'Signature':Signature}


# In[33]:


frame = DataFrame(data)
frame.to_csv('data.csv',index = True)

