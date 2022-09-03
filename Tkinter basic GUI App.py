#!/usr/bin/env python
# coding: utf-8

# In[15]:


from tkinter import *


# In[16]:


import os


# In[17]:


os.system('clear')


# In[37]:


root = Tk()
root.title('Tkinter basic GUI App')
root.geometry("400x400")

def hello():
    hello_label= Label(root, text="Hello" +"  "+ myTextbox.get())
    hello_label.pack()
myLabel = Label(root, text="Enter your first name: ")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text="Submit", command= hello)
myButton.pack()
root.mainloop()


# In[ ]:





# In[ ]:




