#!/usr/bin/env python
# coding: utf-8

# In[8]:


####  1.program to find all pairs of an integer array whose sum is equal to a given number

array = [2,4,5,7,8,5]
sum = 10
def find_pairs(array,sum):
    pairs = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == sum:
                pairs.append((array[i], array[j]))
    return pairs
pairs = find_pairs(array,sum)
print(pairs) 


# In[41]:


#### 2.program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.


def reverse_array(array):
    left, right = 0, len(array) - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

array_num= [1, 2, 3, 4, 5]
reverse_array(array_num)
print(array)


# In[16]:


### 3.program to check if two strings are a rotation of each other
   
def rotation(s1, s2):
   if len(s1) != len(s2):
       return False
   
   s3 = s1 + s1
   
   if s2 in s3:
       return True
   else:
       return False

string1 = "abcd"
string2 = "cdab"
if is_rotation(string1, string2):
   print("The strings are rotations of each other.")
else:
   print("The strings are not rotations of each other.")


# In[24]:


### 4.program to print the first non-repeated character from a string

def first_non_repeated_char(string):
    char_counts = {}
    
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None

string = "edyoda"
result = first_non_repeated_char(string)
if result:
    print("first non-repeated character is:", result)
else:
    print("There are no non-repeated characters in the string.")


# In[ ]:


### 5.Read about the Tower of Hanoi algorithm. Write a program to implement it.
         The Tower of Hanoi is a classic problem in computer science that involves moving a stack of disks from one peg to another. The problem is typically stated as follows:
There are three pegs (A, B, and C) and a stack of n disks on peg A, arranged in increasing size from top to bottom. The goal is to move the entire stack to peg C, while obeying the following rules:

1.Only one disk can be moved at a time.
2.Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty peg.
3.No disk may be placed on top of a smaller disk.


# In[39]:


def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from peg", source, "to peg", destination)
        return
    
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print("Move disk", n, "from peg", source, "to peg", destination)
    tower_of_hanoi(n-1, auxiliary, source, destination)
n = 2
tower_of_hanoi(n, 'A', 'B', 'C')


# In[ ]:


### 6.Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.


Infix: The typical mathematical form of expression that we encounter generally is known as infix notation. In infix form, an operator is written in between two operands.
Prefix: In prefix expression, an operator is written before its operands. This notation is also known as “Polish notation”.
Postfix: In postfix expression, an operator is written after its operands. This notation is also known as “Reverse Polish notation”.


# In[38]:


def postfix_to_prefix(postfix):
    stack = []
    for token in postfix.split():
        if token.isdigit():
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(token + " " + operand1 + " " + operand2)
    return stack.pop()

postfix = "3 4 +"
prefix = postfix_to_prefix(postfix)
print("Prefix notation:", prefix)


# In[40]:


## 7. program to convert prefix expression to infix expression.

def prefix_to_infix(prefix):
    stack = []
    for token in reversed(prefix.split()):
        if token.isdigit():
            stack.append(token)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append("(" + operand1 + " " + token + " " + operand2 + ")")
    return stack.pop()

prefix = "+ 3 4"
infix = prefix_to_infix(prefix)
print("Infix notation:", infix)


# In[42]:


### 8.program to check if all the brackets are closed in a given code snippet.

def check_brackets(code):
    stack = []
    for char in code:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif char in [')', ']', '}']:
            if len(stack) == 0:
                return False
            elif char == ')' and stack[-1] != '(':
                return False
            elif char == ']' and stack[-1] != '[':
                return False
            elif char == '}' and stack[-1] != '{':
                return False
            else:
                stack.pop()
    return len(stack) == 0

code1 = "def foo():\n    if (a + b) * c == d:\n        print('Hello World!')"
code2 = "def foo():\n    if (a + b * c == d:\n        print('Hello World!')"
if check_brackets(code1):
    print("All brackets are closed in code1")
else:
    print("Some brackets are not closed in code1")
if check_brackets(code2):
    print("All brackets are closed in code2")
else:
    print("Some brackets are not closed in code2")


# In[43]:


### 9. program to reverse a stack.
def reverse_stack(stack):
    if len(stack) == 0:
        return
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
        return
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)
stack = [1, 2, 3, 4, 5]
print("Original stack:", stack)
reverse_stack(stack)
print("Reversed stack:", stack)


# In[46]:


### 10.program to find the smallest number using a stack.
class smallStack:
   def __init__(self):
       self.stack = []
       self.min_stack = []

   def push(self, item):
       self.stack.append(item)
       if len(self.min_stack) == 0 or item <= self.min_stack[-1]:
           self.min_stack.append(item)

   def pop(self):
       if len(self.stack) == 0:
           return None
       item = self.stack.pop()
       if item == self.min_stack[-1]:
           self.min_stack.pop()
       return item

   def get_min(self):
       if len(self.min_stack) == 0:
           return None
       return self.min_stack[-1]
stack = smallStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)
print("Smallest item:", stack.get_min())
stack.pop()
print("Smallest item:", stack.get_min())


# In[ ]:




