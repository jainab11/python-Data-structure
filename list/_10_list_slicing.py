'''
@Author: Sheikh jainab
@Date: 2024-16-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title :10. Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''
def slice_list(lst, index1):
    """
    Removes elements from a list based on specified indices.

    Args:
        input_list (list): The input list.
        indices (list): The indices of elements to remove.

    Returns:
        list: The list after removing the specified elements.
    """
    result =[]
    n = len(lst)
    for item in range(n):
        if item not in index1:
            result.append(lst[item])
    return result
            
def main():
    lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    index_to_remove= [0,4,5]
    result = slice_list(lst ,index_to_remove)
    print(result)

if __name__ == "__main__":
    
    main()
