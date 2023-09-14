
from itertools import product

# Function to generate 4-digit numbers with a wildcard based on user input
def generate_numbers_with_wildcard():
    user_input = input("Enter the digits (0-9) and ? for unknown (separated by spaces, every value needs a digit): ")
    
    # Split the user input into a list of digits and wildcard symbols
    input_parts = user_input.split()
    
    # Replace ? with a range of digits (0-9)
    for i, part in enumerate(input_parts):
        if part == "?":
            input_parts[i] = "0 1 2 3 4 5 6 7 8 9"
    
    # Generate all possible combinations of the user's input
    combinations = list(product(*[part.split() for part in input_parts]))
    
    # Convert combinations to 4-digit numbers
    generated_numbers = []
    for combination in combinations:
        if len(combination) == 4:
            number = int(''.join(map(str, combination)))
            generated_numbers.append(number)
    
    # File path to save the generated numbers
    output_file_path = 'generated_numbers.txt'
    
    # Write the generated numbers to the output file
    with open(output_file_path, 'w') as file:
        for number in generated_numbers:
            file.write(f"{number:04d}\n")
    
    print(f"All generated numbers with wildcard saved to '{output_file_path}'.")

# Call the function to generate numbers with wildcard and save them to a file
generate_numbers_with_wildcard()
