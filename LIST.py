#!/usr/bin/env python
# coding: utf-8

# ## list is a collection of items.
# []-> indicates list

# In[1]:


bicycles= ['trek','cannodable','specialized']
print(bicycles)


# ## Accessing Elements in a list

# In[2]:


print(bicycles[2])


# ## First letter capitalized

# In[3]:


print(bicycles[1].title())


# In[4]:


print(bicycles[-1].title())


# In[5]:


fstring= f"My first bicycle is {bicycles[0].title()}"
print(fstring)


# In[6]:


cars=['Honda','BMW','Maruti']


# In[7]:


cars[0]


# In[8]:


names= f"My first car in the list is {cars[2]}"
print(names)


# ## Changing adding and removing elements

# In[9]:


cars


# In[10]:


cars[0]= 'ducati'


# In[11]:


cars


# In[12]:


cars[2]='suzuki'


# In[13]:


cars


# ## append() method add Yamaha to the end of the list

# In[14]:


cars.append('yamaha')


# In[15]:


cars


# ## let's try with empty list

# In[16]:


bikes=[]
bikes.append('tvs')
bikes.append('suzuki')


# In[17]:


print(bikes)


# In[18]:


print([bikes[1].title()])


# ## Inserting Elements in to a list

# In[19]:


bikes


# In[20]:


bikes.insert(1,'ducati')
print(bikes)


# ## Removing an item using del statement

# In[21]:


bikes


# In[22]:


del bikes[0]
print(bikes)


# ## Removing an item using pop statement
# The pop() method removes the last item in the list, but it lets you work that item after removing it

# In[23]:


bikes


# In[24]:


poped_bikes= bikes.pop()
print(poped_bikes)


# ## Poping items from any position in a list

# In[25]:


bikes=['honda', 'yamaha', 'suzuki']
first= bikes.pop(0)
print(f"The first bike was {first.title()}")


# ## Note: If you don't want to use item after removing from list use del() Method and if we have to use the deleted item from the list then use pop() method

# ## if we don't know about the index value

# In[26]:


bikes


# In[27]:


bikes.remove('suzuki')
print(bikes)


# In[ ]:




