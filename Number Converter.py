## This code takes 4 types of number from the user and converts them to the type specified by the user.
## It supports conversion between Decimal, Binary, Octal, and Hexadecimal.
 
# Introduce the user to the program and its functions.

print("Hello, Welcome to our program to convert numbers between different bases.")
print("You can convert numbers between Decimal, Binary, Octal, and Hexadecimal and vice-versa.")

# Taking input from the user

num_type = input("Enter the type of number you want to convert: ")
convert_type = input("Enter the type of number you want to convert to: ")

# Convert from Decimal to Binary

if num_type == "decimal" and convert_type == "binary":
    value = int(input("Enter a decimal number: "))
    result = bin(value)[2:]
    print(f"The binary representation of {value} is {result}.")
    

# Convert from Binary to Decimal

elif num_type == "binary" and convert_type == "decimal":

    value = input("Enter a binary number: ")
    result = int(value, 2)
    print(f"The decimal representation of {value} is {result}.")

# Convert from Decimal to Octal

elif num_type == "decimal" and convert_type == "octal":
    value = int(input("Enter a decimal number: "))
    result = oct(value)[2:]
    print(f"The octal representation of {value} is {result}.")

# Convert from Octal to Decimal

elif num_type == "octal" and convert_type == "decimal":
    value = input("Enter an octal number: ")
    result = int(value, 8)
    print(f"The decimal representation of {value} is {result}.")

# Convert from Decimal to Hexadecimal

elif num_type == "decimal" and convert_type == "hexadecimal":
    value = int(input("Enter a decimal number: "))
    result = hex(value)[2:]
    print(f"The hexadecimal representation of {value} is {result}.")

# Convert from Hexadecimal to Decimal

elif num_type == "hexadecimal" and convert_type == "decimal":
    value = input("Enter a hexadecimal number: ")
    result = int(value, 16)
    print(f"The decimal representation of {value} is {result}.")

# Convert from Binary to Octal

elif num_type == "binary" and convert_type == "octal":
    value = input("Enter a binary number: ")
    decimal = int(value, 2)
    result = oct(decimal)[2:]
    print(f"The octal representation of {value} is {result}.")

# Convert from Octal to Binary

elif num_type == "octal" and convert_type == "binary":
    value = input("Enter an octal number: ")
    decimal = int(value, 8)
    result = bin(decimal)[2:]
    print(f"The binary representation of {value} is {result}.")

# Convert from Binary to Hexadecimal

elif num_type == "binary" and convert_type == "hexadecimal":
    value = input("Enter a binary number: ")
    decimal = int(value, 2)
    result = hex(decimal)[2:]
    print(f"The hexadecimal representation of {value} is {result}.")

# Convert from Hexadecimal to Binary

elif num_type == "hexadecimal" and convert_type == "binary":
    value = input("Enter a hexadecimal number: ")
    decimal = int(value, 16)
    result = bin(decimal)[2:]
    print(f"The binary representation of {value} is {result}.")

# Convert from Binary to Octal

elif num_type == "octal" and convert_type == "hexadecimal":
    value = input("Enter an octal number: ")
    decimal = int(value, 8)
    result = hex(decimal)[2:]
    print(f"The hexadecimal representation of {value} is {result}.")

# Convert from Octal to Hexadecimal

elif num_type == "hexadecimal" and convert_type == "octal":
    value = input("Enter a hexadecimal number: ")
    decimal = int(value, 16)
    result = oct(decimal)[2:]
    print(f"The octal representation of {value} is {result}.")

# If the user enters an invalid conversion type

else:
    print("Invalid conversion types entered.")