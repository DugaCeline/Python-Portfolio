#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Assignment 1

"""

Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.

twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True

"""

# Your Code Below:
def twelver(a,b):
    if a == 12 or b == 12 or a+b == 12:
        return True
    else:
        return False
    
print(twelver(3, 12))
print(twelver(4, 9))
print(twelver(9, 3))


# In[10]:


# Assignment 2

"""
Create a method called pay_extra that accepts 2 parameters:
 working, and hour. This method will be used to decide whether
 an employee will receive extra pay or not. If an employee is working
 during the hrs of 8pm until 8am in the morning, that means they
 should be paid extra. In that situation the method should return true,
 otherwise it should return false.

 NOTE: the hour parameter should be from 0-23.
        So 8AM is hour 8, and 8PM is hour 20.

Example:
    pay_extra(True, 11) -> false
    pay_extra(False, 5) -> false
    pay_extra(True, 6)  -> true
"""

# Your Code Below:
def pay_extra(working, hour):
    return (working == True) and (hour < 8 or hour > 18)
  
    
print(pay_extra(True, 11))
print(pay_extra(False, 5))
print(pay_extra(True, 6))


# In[21]:


# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

# Your Code Below:
def sequence(list_val):
    for i in range(len(list_val)-2):
        if list_val[i] == 1 and  list_val[i + 1] == 2 and list_val[i +2] == 3:
            return True
        
    return False

print(sequence([1, 1, 2, 3, 1]))
print(sequence([1, 1, 2, 4, 1]))
print(sequence([1, 1, 2, 1, 2, 3]))
print(sequence([1, 2]))
print(sequence([]))


# In[34]:


# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""

# Your Code Below:

def grow_string(string_val):
    grow_val = ""
    
    for i in range(len(string_val)):
        grow_val  +=  string_val[0:i]
            
    return grow_val + string_val


print(grow_string('Code')) #→ 'CCoCodCode'
print(grow_string('abc')) # → 'aababc'
print(grow_string('ab')) # → 'aab')
    
    


# In[41]:


# Assignment 5

"""
Define a method that accepts a list as an argument
and returns True if one of the first_folder 4 elements
in the list is a 6. The list length may be less than 4.


first3([1, 2, 6, 3, 4]) → True
first3([1, 2, 3, 4, 6]) → False
first3([1, 2, 3, 4, 5]) → False

"""

# Your Code Below:

def first3(list_val):
    len_val = 0
    if len(list_val)  < 4:
      len_val = len(list_val)
    else :
        len_val = 4 
    for i in range(len_val):
        if list_val[i] == 6:
            return True
    return False

print(first3([1,2,6,3,0,0])) # true
print(first3([1,2,3,3,0,6])) # false
print(first3([6])) # true
print(first3([])) # false


# In[57]:


# Assignment 6

"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""

# Your Code Below:
def last2(string_val):
    l1 = string_val[-2:-1]
    l2 = string_val[-1:]
    count = 0
    
    if len(string_val) < 2:
        return count
    
    for i in range(len(string_val)-3):
        if string_val[i] == l1 and string_val[i +1] == l2:
            count += 1
    return count                   
    

print(last2('hixxhi')) #→ 1
print(last2('xaxxaxaxx')) #→ 1
print(last2('axxxxaaxx')) #→ 3


# In[68]:


# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""

#Your Code Below:

def string_match(string_val1,string_val2):
    
    count = 0;
    
    if len(string_val1) <2 or len(string_val2) <2:
        
        return count
    
    for i in range(min(len(string_val1),len(string_val2)) -1):
    
        if string_val1[i:i+2] == string_val2[i:i+2]:
        
            count+= 1

    return count        
    
    

print(string_match('xxcaazz', 'xxbaaz')) # → 3
print(string_match('abc', 'abc')) # → 2
print(string_match('abc', 'axc')) # → 0    


# In[11]:


# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""

#Your Code Below:


def sum78(list_val):
    

    sum_val = 0 
    exclude = False
    i = 0
    
    while i < len(list_val):
        
        if list_val[i] == 7:
            exclude = True
            
        if list_val[i] == 8 and i != len(list_val) -1:
            i += 1
            exclude = False
    
        if not exclude:
            sum_val += list_val[i]
        i += 1    
        
    return sum_val    



print(sum78([1, 2, 2])) #→ 5
print(sum78([1, 2, 2, 7, 99, 99, 8])) # → 5
print(sum78([1, 1, 7, 8, 2])) # → 4


# In[53]:


# Assignment 9

"""
We have 2 variables. fr and d. fr is a list of strings and d is a dictionary with email
addresses as keys and numbers as values (numbers in string format).
Write code to replace the email address in each of the strings in the fr list with
the associated value of that email looked up from the dictionary d.
If the dictionary does not contain the email found in the list, add a new entry
in the dictionary for the email found in the fr list. The value for this new email key
will be the next highest value number in the dictionary in string format.

Once the dictionary is populated with this new email key and a new number value,
replace that email's occurrence in the fr list with the number value.

The output of running your completed code should be the following:

Value of fr:
['199|4|11|GDSPV', '199|16|82|GDSPV', '205|12|82|GDSPV', '206|19|82|GDSPV']
Value of d:
{'7@comp1.COM': '199', '8@comp4.COM': '200', '13@comp1.COM': '205', '26@comp1.COM': '206'}

"""

# Don't manually change fr and d.

# Your Code Below:
# -------------------------------------

def update_mail(list_fr,list_d):
    
    for i in range(len(list_fr)):
        
        #divide alla eeleements of the list iteem to another list.
        inline_list = list_fr[i].split("|")
        
        #update if exists, insert if not
        if inline_list[0] in list_d.keys():
            inline_list[0] = list_d[inline_list[0]]
            
        else:
            list_d[inline_list[0]] = int(max(list_d.values())) + 1
            inline_list[0] = list_d[inline_list[0]]
        
        #prepare the new element of list_fr
        string = ""    
        
        for s in range(len(inline_list)-1):
            string += str(inline_list[s]) + "|"
        string += str(inline_list[s])
        list_fr[i] = string    

fr = [
'7@comp1.COM|4|11|GDSPV',
'7@comp1.COM|16|82|GDSPV',
'13@comp1.COM|12|82|GDSPV',
'26@comp1.COM|19|82|GDSPV'
]

d= {
'7@comp1.COM': '199',
'8@comp4.COM': '200',
'13@comp1.COM': '205'
}

update_mail(fr,d)
print("sonuç fr=" + str(fr))
print("sonuç d=" + str(d))


# In[ ]:




