'''
@Author: Sheikh Jainab
@Date: 2024-17-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title: 10. Write a Python program to reverse a tuple.
'''

def reverse_tup(tup):
    return(tuple(reversed(tup)))

def main():
    
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(reverse_tup(my_tuple))
    
    
if __name__ == "__main__":
    main()