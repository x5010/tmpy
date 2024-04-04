# Turing Machine Factorial Calculator

This Python program computes the factorial of a given non-negative integer using a simulated Turing machine with two tapes.

### Algorithm Overview

- The input number is represented on the first tape.
- The second tape serves as the output tape to compute the factorial.
- The algorithm iterates through each integer from 1 to the input number, multiplying the current factorial value on the output tape by the current integer.

### How to Use

1. Clone the repository or download the `tm.py` file.
2. Run the program using Python.
3. Enter a non-negative integer when prompted.
4. The program will compute the factorial of the input number and display the result.

### Example

```bash
$ python3 tm.py
Enter a number for which you want to compute the factorial: 5
The factorial of 5 is 120
# tmpy


Let's break down how the Turing machine computes the factorial step by step:

Initialization:

The input tape contains the list of digits of the input number, for example, [5].
The output tape is initialized with the value 1 since the factorial of 0 and 1 is 1: [1].
First Iteration (i = 1):

Input tape: [5].
Output tape: [1].
Calculating the product of the current factorial (1) and the current loop value i (1) gives: 1 * 1 = 1.
Now, the output tape stores the value 1.
Second Iteration (i = 2):

Input tape: [5].
Output tape: [1].
Calculating the product of the current factorial (1) and the current loop value i (2) gives: 1 * 2 = 2.
Now, the output tape stores the value 2.
Third Iteration (i = 3):

Input tape: [5].
Output tape: [2].
Calculating the product of the current factorial (2) and the current loop value i (3) gives: 2 * 3 = 6.
Now, the output tape stores the value 6.
Fourth Iteration (i = 4):

Input tape: [5].
Output tape: [6].
Calculating the product of the current factorial (6) and the current loop value i (4) gives: 6 * 4 = 24.
Now, the output tape stores the value 24.
Fifth Iteration (i = 5):

Input tape: [5].
Output tape: [24].
Calculating the product of the current factorial (24) and the current loop value i (5) gives: 24 * 5 = 120.
Now, the output tape stores the value 120.
Result:

The factorial of the number 5, which is 120, is computed and stored on the output tape.
Thus, the Turing machine sequentially multiplies the current factorial value by the current loop value until it reaches the final value n. Each iteration updates the factorial value on the output tape by applying the next number in the sequence.
