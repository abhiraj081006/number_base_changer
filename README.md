# Number Base Converter

## Overview
This Python program allows users to convert numbers between four different bases: Decimal, Binary, Octal, and Hexadecimal. It provides a simple command-line interface where users can specify the type of the input number and the desired output base. The program then prompts for the number and performs the appropriate conversion, displaying the result. All possible conversions between these four bases are supported.

## Features
- Convert numbers between Decimal, Binary, Octal, and Hexadecimal.
- Supports all 12 possible conversion directions (e.g., Decimal to Binary, Binary to Octal, Hexadecimal to Decimal, etc.).
- User-friendly prompts and clear output.
- Handles invalid conversion types gracefully with an error message.

## How It Works
1. The program greets the user and explains its functionality.
2. The user is prompted to enter the type of number they want to convert (e.g., decimal, binary, octal, hexadecimal).
3. The user is then prompted to enter the type they want to convert to.
4. Based on the input, the program asks for the number in the specified base.
5. The program performs the conversion and displays the result.
6. If the user enters an invalid conversion type, an error message is shown.

## Usage
### Running the Program
1. Make sure you have Python installed on your system (Python 3.x recommended).
2. Save the script as `Decimal to Binary.py` (or any name you prefer).
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using:
   ```
   python "Decimal to Binary.py"
   ```

### Example Session
```
Hello, Welcome to our program to convert numbers between different bases.
You can convert numbers between Decimal, Binary, Octal, and Hexadecimal and vice-versa.
Enter the type of number you want to convert: binary
Enter the type of number you want to convert to: decimal
Enter a binary number: 1011
The decimal representation of 1011 is 11.
```

## Supported Conversions
- Decimal ↔ Binary
- Decimal ↔ Octal
- Decimal ↔ Hexadecimal
- Binary ↔ Octal
- Binary ↔ Hexadecimal
- Octal ↔ Hexadecimal

## Code Structure
- The program uses a series of `if-elif-else` statements to determine which conversion to perform based on user input.
- Python's built-in functions `bin()`, `oct()`, and `hex()` are used for conversions from decimal to other bases.
- The `int()` function with a base argument is used for conversions to decimal from other bases.
- Slicing (e.g., `[2:]`) is used to remove the base prefix (`0b`, `0o`, `0x`) from the output of `bin()`, `oct()`, and `hex()`.

## Error Handling
- If the user enters a conversion type that is not supported, the program prints: `Invalid conversion types entered.`
- The program assumes that the user enters valid numbers for the specified base. No additional validation is performed on the input number format.

## Customization
- You can extend the program to add more features, such as input validation, support for repeated conversions in a loop, or a graphical user interface.

## License
This project is published under MIT Licencse and id  provided for educational purposes and is free to use, modify, and distribute.

## Author
- Abhinav Raj

## Acknowledgments
- Python documentation: https://docs.python.org/3/
- Inspired by common number base conversion exercises for beginners.
