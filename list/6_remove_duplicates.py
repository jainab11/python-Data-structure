'''
@Author: Sheikh jainab
@Date: 2024-15-05
@Last Modified by: Author Name
@Last Modified time: 2024-15-05
@Title : 6. Write a Python program to remove duplicates from a list.

'''
def duplicate(lst):
    lst.sort()
    unique_lst = []
    for i in range(len(lst)):
        if i==0 or lst[i]!=lst[i-1]:
            unique_lst.append(lst[i])
    return unique_lst
def remove_duplicates(input_list):
    """
    Removes duplicates from a list while preserving the order of elements.

    Args:
        input_list (list): The input list with duplicates.

    Returns:
        list: The list with duplicates removed.
    """
    # Initialize an empty list to store unique elements
    unique_list = []
    
    # Iterate over the input list
    for item in input_list:
        # Add the item to the unique list if it's not already present
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

def main():
    """
    Main function to demonstrate removing duplicates from a list.
    """
    # Sample list with duplicates
    sample_list = [1, 1, 1, 1, 2,2,3,4,  4, 5, 6, 4]
    
    # Remove duplicates from the sample list
    result = remove_duplicates(sample_list)
    
    # Print the result
    print("List after removing duplicates:", result)
    result_2 = duplicate(sample_list)
    print(result_2)

if __name__ == "__main__":
    main()
