'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 2. Write a Python program to count the number of characters (character frequency) in a string

'''
def count_characters(input_str):
    """
    Count the number of characters (character frequency) in the input string.

    Parameters:
    - input_str (str): The input string for which character frequency needs to be counted.

    Returns:
    - dict: A dictionary containing character frequencies.
    """
    char_freq = {}
    for char in input_str:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq

def main():
    """
    Main function to execute the program.
    """
    input_str = "google.com"
    result = count_characters(input_str)
    print("Character frequency:", result)

if __name__ == "__main__":
    main()
