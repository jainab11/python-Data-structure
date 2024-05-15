'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 3. Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'

'''

def replace_occurrence(input_str):
    """
    Replace all occurrences of the first character in the input string with '$',
    except for the first character itself.

    Parameters:
    - input_str (str): The input string.

    Returns:
    - str: The modified string with replacements.
    """
    first_char = input_str[0]
    replaced_str = first_char  # Start with the first character unchanged
    for char in input_str[1:]:  # Iterate from the second character onward
        if char == first_char:  # If the character matches the first character
            replaced_str += '$'  # Replace it with '$'
        else:
            replaced_str += char  # Otherwise, keep it unchanged
    return replaced_str

def main():
    """
    Main function to execute the program.
    """
    input_str = 'restart'
    result = replace_occurrence(input_str)
    print(f"The modified string is: {result}")

if __name__ == "__main__":
    main()
