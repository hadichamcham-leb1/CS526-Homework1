# CS526-Homework1
Homework 1 : Hadi Chamcham
PART 1: INTRODUCE YOURSELF

1. How many programming classes have you taken?
I have not taken formal programming classes prior to this semester. I am currently taking Information Structures with Python (MET CS 521) alongside this course to build my foundational programming skills.

2. Do you know Java or Python or both?
I am currently learning Python.

3. What year are you in?
I am just starting my Master's in Applied Data Analytics at Boston University Metropolitan College.

4. What is your experience level with algorithms and data structures?
I am a complete beginner. As a student entering the program without a prior coding background, I am taking Information Structures with Python and Data Structures and Algorithms concurrently to meet my core prerequisites. After feeling overwhelmed during our first lecture, I spoke with my academic advisor and immediately enrolled in the MET LB110: Principles of Software, Logic, and Hardware lab for hands-on foundational support. For Homework 1, I worked step-by-step with AI tools as a learning assistant to understand standard input redirection and Python script execution.










IMPLEMENTATION OVERVIEW:
The program imports Python's standard `sys` module to read from standard input (`sys.stdin`). It iterates line-by-line over incoming text and prints each line using `print(line, end='')`. The `end=''` argument prevents adding extra newline characters, ensuring the output matches the input file line-for-line.
So, we created a Python file named helloworld.py containing the following text:

```python
import sys

def main():
    # Read line by line from standard input
    for line in sys.stdin:
        print(line, end='')

if __name__ == "__main__":
    main()
```
    
Then, in the exact same folder that contains our Python file, we created a plain text file named myfile. Inside, we type the output we are aiming for:
Hello from David Mellor
Since we are aiming to get the output using Command Prompt:
We open our Command Prompt in Windows, type cd , space, and then drop the folder containing the two files in the terminal window; 
Once it is in the prompt, we can run the following command and press Enter:
python3 helloworld.py < myfile
Last step: The output: The screen displays in plain text, 
Hello from David Mellor
No matter how many lines the “myfile” has, once we run the command, the loop continuously listens to standard input and prints each line one by one until it reaches the End Of File.


