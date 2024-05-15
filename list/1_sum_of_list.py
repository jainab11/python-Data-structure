'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 1. Write a Python program to sum all the items in a list.
'''
def sum_of_list_items(lst):
    """
    Calculate the sum of all items in a list.

    Args:
        lst (list): The input list.

    Returns:
        int or float: The sum of all items in the list.
    """
    sum = 0
    for num in lst:
        sum +=num
    return sum

def main():
    my_list = [1, 2, 3, 4, 5]
    sum_of_list = sum_of_list_items(my_list)
    print("Sum of all items in the list:", sum_of_list)

if __name__ == "__main__":
    main()