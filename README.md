# CS 107 Project 5 -- Imperative Data and Stacks

**Due: October 24, 6PM**

This project will have you implement several operations over
imperative data to get you comfortable with the ergonomics of
programming with imperative data, loops, etc...

For this project, you'll be implementing operations on a *stack*, a
data structure we discussed in class. Our implementation will be
designed with poor worst-case behavior (O(n) for insertion) but good
amortized behavior (n insertions will take O(n) time).

Our stack representation will hold three things:
- An underlying array representing the stack
- A "next available element" index
- The size of the array available

We will keep these in a list, whose basic constructor is `make_stack`:

```
def make_stack(numElements):
    return [0, [None] * numElements, numElements]
```

For example, one example stack could be:

```
[2, [-5, 7, None, None, None, None], 6]
```

Observe that the `2` represents the next *available* space, and in
particular to get the top of the stack we need to calculate `2-1 = 1`.

As shown in class, stack pushes must reallocate the array and copy
over old elements by increasing the size. This is the key to good
amortized behavior:

```
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
```

You will implement a few operations on these stacks.

## Task 1: Implement `copyStack`

For your first task, you must implement `copyStack`, which takes as
input a stack and provides as output a new stack consisting of the
same elements, but a fresh copy of the underlying array. In other
words, it should be the case that if you change the array in the
return value from `copyStack(s)`, those changes should not be relected
in `s`.

## Task 2: Implement `pop`

You must implement `pop`, which removes the top element from the
stack and returns it.

- `pop` must set the removed element in the array to `None` (rather
  than what was there before).

- `pop` must raise a `StackUnderflowException` when the stack has no
  elements in it.

## Task 3: Implement `toArray(s)`

The function `toArray(s)` takes a stack as an argument and returns an
array representing the stack as an array. While this sounds trivial,
the key is that you must remove all of the unused elements from the
stack. I.e., the `len(toArray(s))` must be equal to `s[0]` rather than
`s[2]`.

## Task 4: Implement `reverse(s)`

This function reverses a stack. In other words, the top of the stack
should become the bottom, and the bottom of the stack should become
the top, but (specifically) the empty space in the array must be left
alone. You should implement your algorithm using loops (or recursion
over indices), and it should not take more than linear time.

## Task 5: Implement `merge(s1,s2)`

We say that a stack is sorted whenever the top of the stack is the
maximum element, the next item down is the next-largest, etc.. For
example, the stack `[2, [235, 1000], 2]` is sorted. Assuming a stack
`s1` is sorted (and has enough space), we can *merge* `s2` into it by
taking each item from `s2` and putting it in `s1` at the right place
in the array, shifting items in `s1` if necessary.

For example:

```
x = [2, [1,3, None, None], 4]
merge(x, [1,[2], 1])
# x[1] is now [1,2,3,None]
```

If merge encounters duplicate elements (e.g., merging two stacks both
containing `1`) it should place them next to each other. This method
should raise an exception (of your choosing) if `s1` is not large
enough to accommodate the elements from `s2`.

- Task 1 (`copyStack`)
  - Public tests: X/2
  - Secret tests: X/2
- Task 2 (`pop`)
  - Public tests: X/2
  - Secret tests: X/2
- Task 3 (`toArray`)
  - Public tests: X/3
  - Secret tests: X/3
- Task 4 (`reverse`)
  - Public tests: X/4
  - Secret tests: X/4
- Task 5 (`merge`)
  - Public tests: X/3
  - Secret tests: X/5
- Style: X/5 (Follows same style rubric as last time)
- Total: X/35
