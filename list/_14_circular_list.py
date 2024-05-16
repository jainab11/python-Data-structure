''''
@Author: Sheikh jainab
@Date: 2024-16-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title :14. Write a python program to check whether two lists are circularly identical.
'''
def circular_list(lst1,lst2):
    """
    Check whether two lists are circularly identical.

    Parameters:
    - list1 (list): The first list to compare.
    - list2 (list): The second list to compare.

    Returns:
    - bool: True if the lists are circularly identical, False otherwise.

    Circularly identical lists are lists that contain the same elements in the same order,
    but one list is a circular permutation of the other. For example, [1, 2, 3, 4, 5] and
    [3, 4, 5, 1, 2] are circularly identical because one can be obtained from the other
    by rotating the elements.

    This function checks if list2is a circular rotation of list1. It does this by rotating
    list1 one position at a time and comparing it to list2. If list2 is found to be equal
    to any of the circular rotations of list1, the function returns True, indicating that
    the lists are circularly identical. Otherwise, it returns False.

    Examples:
    >>> are_circularly_identical([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    True
    >>> are_circularly_identical([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
    False
    """
    ''' if len(lst1)!=len(lst2):
        return False
    
    dq_lst = deque(lst1)
    for _ in range(len(lst1)):
        dq_lst.rotate(1)
        if dq_lst == lst2:
            return True
    else:
        return False
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2]
result = circular_list(list1, list2)
print("Are the lists circularly identical?", result)'''
    
def are_circularly_identical(list1, list2):
    # Check if the lengths of both lists are the same
    if len(list1) != len(list2):
        return False

    # Concatenate list1 with itself
    concatenated_list = list1 + list1

    # Check if list2 is a sublist of the concatenated list
    if list2 in [concatenated_list[i:i+len(list2)] for i in range(len(list1))]:
        return True
    else:
        return False

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2]
result = are_circularly_identical(list1, list2)
print("Are the lists circularly identical?", result)

        