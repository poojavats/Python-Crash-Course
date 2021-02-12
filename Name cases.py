#!/usr/bin/env python
# coding: utf-8

# In[2]:


name= 'ada lovelace'
print(name.title())


# In[4]:


print(name.upper())


# In[6]:


print(name.lower())


# In[11]:


first= 'ada'
last= 'lovelace'
full_name= f"{first} {last}"
print(full_name)


# In[13]:


print(f"Hello, {full_name.title()}!")


# In[20]:


full_name= "{} {}".format(first , last)
full_name


# In[23]:


language= 'python '
language
language.rstrip()


# In[27]:


language
language= language.rstrip()
language


# In[29]:


language


# In[32]:


hi= ' puja '
hi= hi.strip()
hi


# In[34]:


la= ' okie'
la


# In[36]:


la.lstrip()


# In[40]:


la= la.strip()
la


# In[46]:


message= "one of python's strenth is it's diverse community."
message


# ##  Numbers
# 

# In[48]:


2+3


# In[50]:


2/3


# In[52]:


2-3


# In[55]:


2*3


# In[57]:


2%3


# In[59]:


(2+3)*4


# ## if you are using large numbers, you can group digits using underscores to make large numbers more readable:

# In[61]:


numbers=30_000_000_000


# In[63]:


numbers


# In[65]:


x,y,z= 0,0,0


# In[67]:


y


# ## when we use capital letters of a variable it will be constant variable in entire life of a program and never be changed
# 
# 

# In[93]:


MAX_NUMBERS=5000


# In[94]:


print(MAX_NUMBERS)

