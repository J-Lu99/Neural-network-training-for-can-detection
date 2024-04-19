#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import shutil
from random import shuffle
import sys


# In[2]:


frames=[file[:-4] for file in os.listdir(sys.argv[1]) if file[-4:]=='.txt']
shuffle(frames)


# In[39]:


N=int(sys.argv[2])
if N>len(frames):
    N=len(frames)
per_70=int(7/10*N)
per_15=int(15/100*N)
per_85=per_70+per_15

#Make dirs
dirs=['train','test','val']

for di in dirs:
    os.makedirs('Train_data/can_detection/images/'+di,exist_ok=True):

    os.makedirs('Train_data/can_detection/labels/'+di,exist_ok=True):

        
#copy to images
for frame in frames[:per_70]:
    shutil.copy('GH012973.MP4_labeled/'+frame+'.jpg','Train_data/can_detection/images/train/GH012973'+frame+'.jpg')
    shutil.copy('GH012973.MP4_labeled/'+frame+'.txt','Train_data/can_detection/labels/train/GH012973'+frame+'.txt')
    
for frame in frames[per_70:per_85]:
    shutil.copy('GH012973.MP4_labeled/'+frame+'.jpg','Train_data/can_detection/images/test/GH012973'+frame+'.jpg')
    shutil.copy('GH012973.MP4_labeled/'+frame+'.txt','Train_data/can_detection/labels/test/GH012973'+frame+'.txt')
    
for frame in frames[per_85:N]:
    shutil.copy('GH012973.MP4_labeled/'+frame+'.jpg','Train_data/can_detection/images/val/GH012973'+frame+'.jpg')
    shutil.copy('GH012973.MP4_labeled/'+frame+'.txt','Train_data/can_detection/labels/val/GH012973'+frame+'.txt')            


# In[41]:



if N == len(frames[:per_70])+len(frames[per_70:per_85])+len(frames[per_85:N]):
    print('Todos los archivos copiados')


# In[ ]:




