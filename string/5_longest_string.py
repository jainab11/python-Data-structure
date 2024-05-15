'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 5. Write a Python function that takes a list of words and returns the length of the longest one. 
'''
def longest_string(lst):
    max_length = 0
    for word in lst:
        if len(word) > max_length:
            max_length = len(word)
    return max_length
def main():
    """
    Main function to execute the program.
    """
    lst = input("Enter words seprated by comma : ").split(',')
    output = longest_string(lst)
    print("longest string is ", output)
if __name__ == "__main__":
    main()
