#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Assignment 1:
"""
Print Bill's salary from the my_list object shown below.

my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

"""


# your code below:
my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

print(my_list[0]['Bill'])


# In[6]:


# Assignment 2:
"""
Using some of the collection data types we learned about
in the course so such as a list and dictionary, create a
data structure that best represents the following scenario:

Tom has a salary of 20000 and is 22 years old. He owns a few items such as
a jacket, a car, and TV. Mike is another person who makes 24000 and is 27 years old
who owns a bike, a laptop and boat.
"""

# your code below:
my_data = {"Tom": {"Salary": 20000,"Age":22,"Items": ["jacket","car", "TV"]},"Mike": {"Salary": 24000,"Age":27,"Items": ["bike","laptop", "boat"]}}

print(my_data["Tom"]["Items"])


# In[15]:


# Assignment 3:
"""
There is a list shown below titled original_list.

Using only what you've learned so far in the course,
write code to create a new list that contains the tuple sorted.

IMPORTANT: you must do this programmatically! Don't just
      hard code a new list with the values rearranged.
"""

original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]

# your code below:
inlist = list(original_list[3])

print(inlist)

inlist.sort()

print(inlist)

original_list[3] = tuple(inlist)

print(original_list)



# In[18]:


# Assignment 4:
"""
In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
"""

my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]


# Your Code Below:

print(my_list)
my_list[2][0][3] = "x"
print(my_list)
my_list[3] = "television"
print(my_list)


# In[ ]:





# In[ ]:




