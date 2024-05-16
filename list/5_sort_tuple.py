'''
@Author: Sheikh jainab
@Date: 2024-15-05
@Last Modified by: Author Name
@Last Modified time: 2024-15-05
@Title : Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

def sort_lst(lst):
    '''
    # using lambda function
    sorted_list = sorted(lst, key=lambda x: x[-1])
    return sorted_list
    '''

    """
    Sorts a list of tuples in increasing order by the last element of each tuple.

    Args:
        lst (list): A list of tuples.

    Returns:
        list: The sorted list of tuples.
    """
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            # Compare the last elements of adjacent tuples
            if lst[j][-1] > lst[j+1][-1]:
                # Swap the tuples if the last elements are out of order
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def main():
    """
    Main function to demonstrate sorting of tuples by the last element.
    """
    
    # Sample list of tuples
    my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    
    # Sort the list of tuples
    result = sort_lst(my_list)
    
    # Print the sorted list
    print(result)

if __name__ == "__main__":
    main()
