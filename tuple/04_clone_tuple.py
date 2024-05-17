'''
@Author: Sheikh Jainab
@Date: 2024-17-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title: 4. Write a Python program to create the colon of a tuple.
'''
def clone_tuple(tup):
    return tuple(item for item in tup)
# return tup[:]
# return tuple(tup)
def main():
    """
    Main function to execute the program.
    """
    my_tuple = (1,4,6 ,'jainab',True, 3.4)
    ans = clone_tuple(my_tuple)
    print(ans)
  

if __name__ == "__main__":
    main()