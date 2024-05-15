'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 2. Write a Python program to multiplies all the items in a list.

'''
def mul_of_list_items(lst):
    """
    Calculate the multiplication all items in a list.

    Args:
        lst (list): The input list.

    Returns:
        int or float: The sum of all items in the list.
    """
    mul = 1
    for num in lst:
        mul *=num
    return mul

def main():
    my_list = [1, 2, 3, 4, 5]
    mul_of_list = mul_of_list_items(my_list)
    print("multiplication of all items in the list:", mul_of_list)

if __name__ == "__main__":
    main()