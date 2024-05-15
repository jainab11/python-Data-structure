'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
'''

def print_unique_sorted_words(words):
    """
    Print the unique words in sorted form (alphanumerically) from the given input.

    Parameters:
    - words (str): A comma-separated sequence of words.

    Returns:
    - None
    """
    # Split the input string into a list of words
    word_list = words.split(',')
    # Remove leading and trailing whitespaces from each word and convert to lowercase
    word_list = [words.strip().lower() for words in word_list]
    # Remove duplicates by converting the list to a set
    unique_words = set(word_list)

    # Sort the unique words alphabetically
    sorted_words = sorted(unique_words)

    # Print the sorted unique words
    print("Unique words in sorted form:", ", ".join(sorted_words))

def main():
    """
    Main function to execute the program.
    """
    # Take input from the user
    user_input = input("Enter a comma-separated sequence of words: ")

    # Call the function to print unique words in sorted form
    print_unique_sorted_words(user_input)

if __name__ == "__main__":
    main()
