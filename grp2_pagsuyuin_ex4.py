#1 Create a Python program to perform arithmetic Operations  (Addition, Subtraction, Division, Multiplication, Modulus, Exponent) using two variable numbers for int, float and complex
#Integer Operations
num1_int = 15
num2_int = 4
print("--- Integer Operations ---")
print(num1_int + num2_int) # Addition
print(num1_int - num2_int) # Subtraction
print(num1_int * num2_int) # Multiplication
print(num1_int / num2_int) # Division
print(num1_int % num2_int) # Modulus
print(num1_int ** num2_int) # Exponent

#Float Operations
num1_float = 50.75
num2_float = 12.25
print("\n--- Float Operations ---")
print(num1_float + num2_float)
print(num1_float - num2_float)
print(num1_float * num2_float)
print(num1_float / num2_float)

#Complex Operations
num1_complex = 5 + 10j
num2_complex = 2 + 3j
print("\n--- Complex Operations ---")
print(num1_complex + num2_complex)

#2 Write a program that creates two variables, num1 and num2. Both num1 and num2 should be assigned the integer literal 25000000, one written with underscores and one without. Print num1 and num2 on two separate lines.
num1 = 25000000
num2 = 25_000_000
print("\n--- Task #2: Large Numbers ---")
print(num1)
print(num2)

#3 Creating int,float and complex variable then check the type using the Python Code
print("\n--- Task #3: Type Checking ---")
print(type(num1_int))
print(type(num1_float))
print(type(num1_complex))
