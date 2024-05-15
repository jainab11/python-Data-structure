'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 4. Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''
def add_ing(str):
    n = len(str)
    if n < 3:
        return str
    elif str.endswith('ing'):
        return str+'ly'
    else:
        return str+'ing'

def main():
    """
    Main function to execute the program.
    """
    str = input("Enter a string : ")
    result = add_ing(str)
    print(" changed string is : ", result)
if __name__ == "__main__":
    main()
