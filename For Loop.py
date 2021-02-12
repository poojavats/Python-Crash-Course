#!/usr/bin/env python
# coding: utf-8

# ## For Loop Exercise

# In[4]:


magicians=['alice','bob','jon']
for magician in magicians:
    print(magician)


# In[10]:


magicians


# In[13]:


for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")


# In[15]:


magicians


# In[27]:


for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f" I can't wait to see your next trick {magician.title()}.\n")
    print(f" you are wonderful magician {magician.title()}.\n")
    print('Thank you Everyone!')


# In[32]:


pizza= ['cheeze','Tomato','chilly']
for piz in pizza:
    print(piz)


# In[44]:


pizza= ['cheeze','Tomato','chilly']
for piz in pizza:
    print(f" I like pepperoni pizza{piz.title()}")
    print("how much you like pizza?")
    print(f" I really love pizza{piz.title()}\n")


# In[61]:


Animals=['Cow','got','hen']
for ani in Animals:
    print(ani,":")
    print(f"A dog is a good friend of {ani.title()}")
    print(f"Any of these Animals would be a great pet {ani.title()}\n")

