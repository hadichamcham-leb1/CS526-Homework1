CS526 Homework Assignment 2
#Disclaimer : Notes about background and the use of AI
As I mentioned earlier in the semester, I come from 18 years in fixed income trading and portfolio management, and I had no coding or computer science background before starting this master's. I am learning Python in parallel with this course. Besides the Information Structures with Python course, I took two beginner courses on edX (*Computing in Python I: Fundamentals and Procedural Programming* and *Computing in Python II: Control Structures*) to try and catch up faster.
I used Gemini, ChatGPT and Claude as tutoring help on this assignment, mainly on the coding. I asked them to guide me through the logic of each problem and to explain each function and concept along the way, and I used them to review my code and test edge cases. To be honest, I could not have written this code alone two weeks ago. I worked on Problems 2 and 4 for two weeks, studying classes, functions, modules and recursion, and I am much more comfortable with nodes, pointers and recursive functions than I was at the start. The explanations below are written in my own words, and I describe the mistakes I found along the way, because working through them is where most of my learning happened.

## Introduction
This homework has four problems:
1. Problem 1: a short written question about the advantage of a tail pointer in a linked list.
2. Problem 2: a ‘Node’ class and a ‘SinglyLinkedList’ class with CRUD operations (‘problem2.py’), plus a driver (‘problem2_driver.py’) that reads commands from standard input, calls the matching list method, prints results, and prints a warning for any bad line instead of crashing.
3. Problem 3: a recursive function ‘ways(n)’ that counts the ways to climb ‘n’ stairs taking 1, 2, or 3 steps at a time (‘problem3.py’), plus two written questions.
4. Problem 4: a ‘SortedDoublyLinkedList’ class that always keeps its values in ascending order (‘problem4.py’), with recursive helpers for ‘total’, ‘count’, ‘exists’ and ‘print_list’, plus ‘sum_middle_three’ and ‘median’, and a driver that reads from standard input (‘problem4_driver.py’).

Answer to problem 1: Advantage of a tail pointer
With a tail pointer, adding a node at the end of the list takes the same short time no matter how long the list is, because the list already knows where the last node is. Without it, ‘append’ has to walk from the head through every node to find the end, so each append takes longer as the list grows, and building a list of n items a much longer time. It is like keeping a bookmark on the last page.
The cost of keeping a tail is bookkeeping: every operation that can change the last node (for example ‘delete’) has to update ‘tail’ as well. Also, in a singly linked list the tail does not make removing the last node faster, because we still need the node before it and have no backward link. In a doubly linked list, the tail also helps with the end of the list from the other direction.

Algorithm
Problem 2: singly linked list
I think of the list as a chain of boxes, like the example from lecture 1. Each box (‘Node’) holds a value and an arrow (‘next’) to the next box. The `SinglyLinkedList` object only remembers where the chain starts (‘head’), where it ends (‘tail’), and how many nodes there are (‘count’). There is no stored "position 3", so to reach an index I have to walk from the head, one node at a time.
The main idea for operations that change the chain (‘insert’, ‘delete’, ‘delete_at’) is that I need to stand on the node just before the one I am changing, because only that node's forward arrow can be rewired. This is why the loop in ‘insert’ runs ‘index – 1’ times: starting on the head, each iteration moves one node forward, and after ‘index – 1’ hops, I am standing on the node just before the new position.
- ‘append’ / ‘prepend’ / ‘insert’: if the list is empty, the new node becomes both head and tail. Otherwise ‘append’ attaches after the tail and moves the tail, ‘prepend’ points the new node at the old head and moves the head, and ‘insert’ handles index 0 (prepend) and index equal to the count (append) separately, so the loop only deals with a real position in the middle.
- Rewiring order in ‘insert’: I first save the old next node (‘old_next = temp.next’), then point the previous node at the new node, then point the new node at ‘old_next’. If I changed the arrow first without saving it, the rest of the chain would be lost.
- ‘get’, ‘update’, ‘find’: walk from the head. ‘get’ and ‘update’ stop at the given index, and ‘find’ walks until it finds the value and returns its position, or -1 if it reaches the end.
- ‘delete’/ ‘delete_at’: deleting the head just moves ‘head’. Otherwise, I stand on the node before the one being removed and point its ‘next’ past it. If the removed node was the tail, ‘tail’ has to move back to the previous node, otherwise a later ‘append’ would attach to a node that is no longer in the list. If the list becomes empty, ‘tail’ is set to ‘None’.
- ‘__len__’: returns the stored ‘count’. The name `__len__` is a special method name: Python calls it when we write `len(my_list)`. Keeping a running count means this is instant, instead of walking the whole list.
- ‘print_list’: walks from head to tail, collects the values as text and joins them with ‘" -> "’, or prints ‘(empty)’.
- Index checks: for ‘get’, ‘update’, and ‘delete_at’, the index must satisfy ‘0 <= index < count’; for ‘insert’ it may also equal ‘count’ (inserting at the end). Otherwise, an `IndexError` is raised.
I drew the boxes and arrows on paper for each case (empty list, one node, first node, last node, middle) and checked that ‘head’, ‘tail’ and ‘count’ stay correct.
Driver (‘problem2_driver.py’). For each input line, the driver strips the whitespace, skips blank lines and lines starting with ‘#,’ splits the line into words, and treats the first word as the “directive” and the rest as its “arguments”. It then checks, before calling anything, that the directive is one of the allowed ones, that the number of arguments is right, and that an index is a whole number. If everything is fine it calls the matching method with ‘getattr(my_list, directive)(*args)’, which is the pattern from class. If something is wrong, it prints a warning and continues with the next line. After the last line, it prints ‘Final list:’ followed by the actual list of numbers separated by “- >”.

Problem 3: climbing stairs
The hint says to think about the first move. The first move can be 1, 2, or 3 steps, and after it, we face the same problem on a shorter staircase. So the number of ways is the sum of three groups: ‘ways(n-1)’ (first move 1 step), ‘ways(n-2)’ (first move 2 steps), and ‘ways(n-3)’ (first move 3 steps). These groups do not overlap and together cover every path. I checked this against the example in the assignment: for 4 steps the groups contain 4 + 2 + 1 = 7 paths.
a)	Base cases: ‘ways(n)’ returns 0 when ‘n < 0’, because the move overshot the top and the path is invalid. It returns 1 when ‘n == 0’, because the path landed exactly on the top and counts as one way. ‘ways(0)’ has to be 1 (the one way to climb nothing is to do nothing): every successful path ends by reaching exactly 0, and the recursion adds up these 1s. If ‘ways(0)’ were 0, every answer would be 0.
b)	Only 1 or 2 steps. Then ‘ways(n) = ways(n-1) + ways(n-2)’, which gives the Fibonacci sequence (1, 1, 2, 3, 5, 8, ...). ‘
Output results: ‘ways(3) = 4’, ‘ways(5) = 13’, ‘ways(10) = 274’.

Problem 4: sorted doubly linked list
Each node has a ‘prev’ and a ‘next’ arrow, and the list keeps ‘head’, ‘tail’, and a size (‘_size’, named this way so it does not clash with the ‘count(value)’ method).
- ‘add’ has four cases: (1) empty list, so the new node is both head and tail; (2) the value is less than or equal to the head's value, so it goes at the front; (3) the value is greater than the tail's value, so it goes at the end; (4) otherwise I walk until I find the first node whose value is not smaller, and insert the new node right before it by fixing four arrows (`new.next`, `new.prev`, `curr.prev.next`, `curr.prev`). Duplicates are allowed.
- ‘delete’ walks while values are smaller than the target. If it runs off the end or lands on a different value, it returns `False`. Otherwise it removes the node, fixing the neighbors' arrows and updating ‘head’ or ‘tail’ when the node was at an end.
- Recursive helpers (‘exists’, ‘count’, ‘total’, ‘print_list’): each helper handles one node and then calls itself on ‘node.next’. The base case is ‘node is None’ (we ran past the tail). Because the list is sorted, ‘exists’ and ‘count’ can stop early as soon as they reach a value larger than the target. ‘total’ adds ‘node.value’ to the total of the rest. ‘print_list’ prints each value followed by ‘" <-> "’, except the last one.
- ‘sum_middle_three’ and ‘median’: both use ‘mid = n // 2’. I walk from the head to the node at position ‘mid’ and then use the ‘prev’ and ‘next’ arrows to reach its neighbors. For ‘sum_middle_three’, with odd ‘n’ I add the nodes at ‘mid-1’, ‘mid’ and ‘mid+1’, and with even `n` the nodes at ‘mid-2’, ‘mid-1’ and ‘mid’. 
- For ‘median’, with odd’`n’ I return the middle value, and with even ‘n’ the average of the two middle values. Both raise a `ValueError` when the list is too small (fewer than 3 nodes for `sum_middle_three`, empty for `median`).
Interesting aspects:
- Keeping ‘tail’ and ‘count’ costs extra bookkeeping on every change but makes ‘append’ and ‘len’ fast.
- Dividing the driver's work into "check first, then call" (known directive, right number of arguments, index is a whole number) gives accurate warning messages. A first version relied on catching a `TypeError`, which gave a misleading message for a non-numeric index.
Edge cases I tested: an empty list, a list with one node, operations at the head and the tail, duplicate values, indexes out of range, deleting a value that is not there, unknown directives, wrong argument counts, and non-numeric indexes.

Main issues I encountered when running the completed code with the test files provided on blackboard:

In Problem 2: every warning should start with “line N:” . Instead my code was writing “Warning:”
I fixed this problem by using a “for” loop and by calling the built-in Python function “enumerate”.
In Problem 4: Writing “add” with one or more upper case letters was giving me  an “Unkown directive” error instead of running the code like it does in the “problem_executions” file. I fixed this by adjusting the directive to : directive = parts[0].lower which will translate each character input into lowercases and thus run the code smoothly.


How to run
From the folder containing the files (I use “py” instead of “python3” because “python3” was not recognized on my windows):
```
py problem2_driver.py < problem2_basic.txt  (# and any of the sample files)
py problem4_driver.py < problem4_basic.txt (# and any of the sample files)
```
‘problem2_driver.py’ imports ‘problem2.py’, and ‘problem4_driver.py’ imports ‘problem4.py’, so each pair must be in the same folder.
Test files
I tested all the files from the assignment folder on blackboard for both problem 2 and 4; will paste the command prompt showing the results in the next section. 


