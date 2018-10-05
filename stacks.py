# CS 107, Fall 2018 -- Project 5
# Imperative Data and Stacks
from library import *

class StackUnderflow(Exception):
    pass

# Create an empty stack, whose length is numElements
def make_stack(numElements):
    return [0, [None] * numElements, numElements]

# Does s "look like" a stack
def looksLikeStack(s):
    return len(s) == 3 and type(s[0]) == type(0) and type(s[1]) == type([]) and type(s[2]) == type(0)

# Three accessor functions for stacks
def top(stack): 
    precondition(looksLikeStack(stack))
    return stack[0]

def data(stack): 
    precondition(looksLikeStack(stack))
    return stack[1]

def size(stack): 
    precondition(looksLikeStack(stack))
    return stack[2]

# Return a new copy of the stack, without changing anything
def copyStack(s):
    return [s[0], s[1] + [], s[2]]

# Push an element onto a stack
def push(stack, e):
    precondition(looksLikeStack(stack))
    if (top(stack) >= size(stack)):
        # Reallocate
        newSize = size(stack) * 2
        newData = [None] * newSize
        i = 0
        # Copy old data
        while (i < size(stack)):
            newData[i] = data(stack)[i]
            i = i + 1
        # Add new element
        newData[i] = e
        # Set up stack correctly again
        stack[0] = top(stack) + 1
        stack[1] = newData
        stack[2] = newSize
    else:
        # Add to top of stack and increment "top of stack"
        stack[1][top(stack)] = e
        stack[0] = top(stack) + 1

# Pop the top element from the stack
def pop(stack):
    precondition(looksLikeStack(stack))
    raise UnimplementedExeception

def toArray(stack):
    raise UnimplementedExeception

def reverse(stack):
    raise UnimplementedExeception

def merge(s1,s2):
    raise UnimplementedExeception

