#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:
def MergeLists(list1, list2):
    return list1 + list2

l1 = [1,2,3]
l2 = ["x","y","z"]

print(MergeLists(l1,l2))


# In[7]:


# Assignment 2:
"""
    create a function called separate() that accepts a string as an argument
    and returns a list containing each of the characters of
    the string separated as individual items in the list.

    Make sure to test the function.
"""
# Your Code Below:
def seperate(string):
    return list(string)

print(seperate("Selin"))


# In[18]:


# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""
# Your Code Below:

def multi_merge(list_1, string):
    l1 = list_1
    l2 = string.split()
    l3 = list(string)
    
    return l1+l2+l3

print(multi_merge([1,2,3], "Selin Güneş"))


# In[21]:


# Assignment 4:

"""
Define a function called last_list that can accept an unlimited number
of lists but returns only the last list.

Example:

    For example, the below function call should return ['mike', 'john']

    last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])

"""

# Your code below:

def last_list(*args):
    return(args[-1:])


print(last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john']))



# In[23]:


# Assignment 5:

"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second_folder to last item in the specific list specified by the user of the function.

Example:

    For example, the below function call should return: jan

    key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])

"""

# Your Code Below:
def key_list_items(key, **kwargs):
    return kwargs.get(key)[-2]

print(key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom']))


# In[ ]:




