def factorial_machine(n):
    # Initialize tapes
    input_tape = [int(digit) for digit in str(n)]  # Represent number n on the first tape
    output_tape = [1]  # Initial value of factorial on the second tape
    
    # Algorithm steps
    for i in range(1, n + 1):
        # Multiply the current factorial value by the current loop value
        output_tape = multiply(output_tape, [int(digit) for digit in str(i)])
        print("Step", i, ": Current factorial =", ''.join(map(str, output_tape)))
    
    # Return the result (factorial value on the second tape)
    return int(''.join(map(str, output_tape)))

def multiply(num1, num2):
    # Multiplication of two numbers represented as lists of digits
    
    # Convert lists of digits into integers
    num1 = int(''.join(map(str, num1)))
    num2 = int(''.join(map(str, num2)))
    
    # Calculate the product
    result = num1 * num2
    
    # Convert the result back into a list of digits
    return [int(digit) for digit in str(result)]

# Get the input number from the user
user_input = int(input("Enter a number for which you want to compute the factorial: "))

# Calculate the factorial using our Turing machine with two tapes
result = factorial_machine(user_input)

# Display the result
print("The factorial of", user_input, "is", result)
