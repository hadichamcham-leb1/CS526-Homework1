## Introduction

This homework has four problems, each solved in its own file:

Problem 1: reads strings (one per line) from standard input, prints "True" or "False" for each depending on whether it is a palindrome, and finally prints how many palindromes there were. Case matters, and spaces between characters are ignored.

Problem 2: reads one string and prints every unique substring in alphabetical order, followed by how many there are.

Problem 3: three stacks (array, singly linked list, doubly linked list), and two recursive functions that reverse any of them in place. It pushes 1 to 10 on each stack and prints the stack before and after reversing it.

Problem 4: reads Ghostbuster and ghost pairs and prints whether all streams (infinite lines) can fire without crossing.

## Algorithm

### Problem 1: palindrome

The function "is_palindrome(text)" follows the idea from lecture 2.

Base case 1: a string with 0 or 1 characters is a palindrome (there is nothing left). It has to be "True" for the empty string too, because a string like "abba" is reduced to the empty string before the recursion ends.
Base case 2: if the first and last characters differ, it is not a palindrome.
Recursive case: if the ends match, the answer is the answer for the string without its two ends, "text[1:-1]".

The spaces are removed once in "main" ("line.replace(" ", "")"), before the recursion starts, so the recursive function stays simple and does not repeat the cleaning on every call. Case is not changed, so "Aa" is not a palindrome. "main" prints one line per string and counts the "True" results.

### Problem 2: unique substrings

For each start position, the function "grow(text, start, end, found)" adds "text[start:end]" to a set and then calls itself with "end + 1". The base case is when "end" goes past the length of the text. A loop in "main" starts "grow" at every start position, with a first piece of one character ("end = start + 1"), so the substring search itself is done by the recursion. The set is created once and passed to every call. A set ignores repeated values, which removes duplicate substrings. Sets have no order, so the program uses "sorted(found)" to print in alphabetical order and "len(found)" for the final count.

For "abcab" there are 5 + 4 + 3 + 2 + 1 = 15 substrings by position, but "a", "b" and "ab" each appear twice, so there are 12 unique ones.

### Problem 3: reversing a stack with recursion

All three stacks offer "push", "pop", "peek" and "is_empty". The same two recursive functions reverse all three stacks:

- "insert_at_bottom(stack, item)": if the stack is empty, push the item (it becomes the bottom). Otherwise pop the top and keep it, call itself to put the item at the bottom of the smaller stack, then push the kept item back.
- "reverse(stack)": if the stack is empty, stop. Otherwise pop the top and keep it, reverse the smaller stack, then use "insert_at_bottom" to put the kept item at the bottom.

The old top ends up at the bottom and the old bottom ends up on top. The same stack object is changed, nothing new is built, and there are no loops in the reversal.

The stacks differ in how they store the items:
- *Array stack: a Python list, where the end is the top.
- Singly linked stack: the top is the head, so push and pop never walk the list.
- Doubly linked stack: the top is the tail, and "prev" lets "pop" move the tail back directly.

To print the stack from bottom to top without a loop, the linked stacks use a recursive helper, "_collect", that builds the list one node at a time.

### Problem 4: Ghostbusters

A stream is an infinite line, so two streams do not cross only when they are "parallel and not the same line". The program checks that in one pass:

1. Compute the direction of the first stream, "(dx, dy)".
2. For each stream, compute its direction "(ex, ey)" and test whether it is parallel to the first with "dx * ey - dy * ex == 0". This is the slope comparison written as a cross-multiplication, so there is no division and vertical streams ("dx = 0") need no special case. At the first stream that is not parallel, stop and print "not eliminated".
3. For parallel streams, compute the label "dx * by - dy * bx" from the Ghostbuster's position. Streams on the same line get the same label, and streams on different parallel lines get different labels. Put the labels in a set: if the set has fewer items than there are streams, two streams share a line, which counts as crossing.

## Interesting aspects:

In Problem 1, the spaces are removed once, outside the recursion. Letter case is never changed, as the statement requires.
In Problem 4: no division and no floating point, so there are no rounding problems and no special case for vertical streams. The hint given in class was to check whether each slope equals the first one and stop at the first mismatch, which is what the program does.

Edge cases tested: empty and one-character strings, capital letters, spaces inside strings, an empty stack and a one-item stack for the reversal, a single Ghostbuster, streams on the same line pointing in opposite directions, vertical streams, and negative coordinates.

## How to run

From the folder with the files (on Windows, use `py` instead of `python3` if `python3` is not recognized):

```
py problem1.py < testsproblem1/palindrome_input.txt
py problem2.py < testsproblem2/unique_substrings_input1.txt
py problem4.py < testsproblem4/ghostsbusters_input1.txt
```

problem3.py takes no input file, because the problem says to push 1 to 10 itself.

## Test files

I tested all the files from the assignement folder on blackboard for all all problems: I will screenshot the command prompt running and put them in the folder.
