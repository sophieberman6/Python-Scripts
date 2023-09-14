from itertools import product

# Function to generate all possible 4-digit numbers based on user input
def generate_all_possible_numbers():
    user_input = input("Enter the digits (0-9) you want to include (separated by spaces): ")
    
    # Split the user input into a list of digits
    selected_digits = [int(digit) for digit in user_input.split()]
    # selected_digits.append(0)
    
    # Check if the user has selected at least 1 digit
    if len(selected_digits) == 0:
        print("No digits selected. Please choose at least one digit (0-9).")
        return
    
    # Generate all possible 4-digit numbers based on selected digits
    
    output_file_path = '4digit.txt'
    
    with open(output_file_path, 'w') as file:
            

        for combination in product(selected_digits, repeat=4):
            number = int(''.join(map(str, combination)))
            digit = (f"{number:04d}")
            print(digit)
            file.write(f"{digit}\n")


    
    # Write the generated numbers to the output file

    
    print(f"All generated numbers saved to '{output_file_path}'.")



# Call the function to generate all possible numbers
generate_all_possible_numbers()
