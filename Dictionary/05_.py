'''

@Author: Jainab sheikh

@Date: 2024-05-23

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-23

@Title :5. Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
def root_dict(n):
    """ Write a Python script to generate and print a dictionary that contains a
    number (between 1 and n) in the form (x, x*x).

    Args:
        n (_int_): takes an input
    result:
        stores the value in dictionary
    """
    my_dict= dict()
    for item in range(1,n+1):
        # adding values to dictionary
        my_dict[item]= item*item    
    print(my_dict)
def main():
    
    n = 5
    print(root_dict(n))
            
if __name__ == "__main__":
    main()