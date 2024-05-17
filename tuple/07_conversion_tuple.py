'''
@Author: Sheikh Jainab
@Date: 2024-17-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title: 7. Write a Python program to convert a list to a tuple.
'''
def main():
    """
    Main function to execute the program.
    """
    my_list = [1,4,6 ,'jainab',True, 3.4]
    print(type(my_list))
    my_tuple = tuple(my_list)
    print(type(my_tuple))
    
  

if __name__ == "__main__":
    main()