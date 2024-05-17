'''
@Author: Sheikh Jainab
@Date: 2024-17-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title: 3. Write a Python program to unpack a tuple in several variables.
'''
def main():
    """
    Main function to execute the program.
    """
    my_tuple = (1,4,6 ,'jainab',True, 3.4)
    a,b,c,d,e,f = my_tuple
    print(a,b,c,d,e,f, sep ='\n')
    print(type(my_tuple))
    print(my_tuple)

if __name__ == "__main__":
    main()

