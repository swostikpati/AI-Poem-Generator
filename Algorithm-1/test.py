# -*- coding: utf-8 -*-
'''
Created on Tue Oct  4 00:03:16 2022

@author: Swostik Pati
'''

#%%

# Importing random module
import random
  
# Defining list of phrases which will help to build a story
  
Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
character = [' there lived a king.',' there was a man named Jack.',
             ' there lived a farmer.']
time = [' One day', ' One full-moon night']
story_plot = [' he was passing by',' he was going for a picnic to ']
place = [' the mountains', ' the garden']
second_character = [' he saw a man', ' he saw a young lady']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
work = [' searching something.', ' digging a well on and roadside.']

  

# Selecting an item from each list and concatenating them.
for i in range(10):
    print(random.choice(Sentence_starter)+random.choice(character)+
          random.choice(time)+random.choice(story_plot) +
          random.choice(place)+random.choice(second_character)+
          random.choice(age)+random.choice(work))
    
#%%
import random

subject = ['you',  'I', 'sun', 'life', 'the one', 'my', 'your']
phrases =  ['crave and desire', 'eternal',    'whole',  'company']
actions =["love", "caresss", "admire"]


for i in range(6):
    print(random.choice(subject) + " " +random.choice(actions)+ " "+
          random.choice(phrases))