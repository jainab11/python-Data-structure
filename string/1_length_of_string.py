'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 1. Write a Python program to calculate the length of a string.

'''
def string_length(str):
    count = 0
    for length in str:
        count +=1
    return count
        
def main():
    str = input("Enter  a string")
    length = string_length(str)
    print("length of a string is ", length)
if __name__== "__main__":
    main()
    
    
'''
Anoter way to do this program 
'''
""" 
def string_length(input_str):
    return len(input_str)

def main():
    input_str = input("Enter a string: ")
    length = string_length(input_str)
    print("Length of the string:", length)

if __name__ == "__main__":
    main()
"""