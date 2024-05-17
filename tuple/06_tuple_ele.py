'''
@Author: Sheikh Jainab
@Date: 2024-17-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title: 4. 6. Write a Python program to check whether an element exists within a tuple.

'''
def ele_tuple2(tup, num):
    return num in tup
def ele_tuple1(tup, num):
    try:
        tup.index(num)
        return True
    except ValueError:
        return False

def ele_tuple(tup, num):
    for item in tup:
        if item == num:
            return True
    return False
def main():
    """
    Main function to execute the program.
    """
    my_tuple = (1,4,6,5)
    n = 5
    ans = ele_tuple(my_tuple,n)
    if ans:
        print("element present")
    else:
        print("element not present")
  

if __name__ == "__main__":
    main()