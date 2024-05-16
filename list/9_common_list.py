'''
@Author: Sheikh jainab
@Date: 2024-15-05
@Last Modified by: Author Name
@Last Modified time: 2024-15-05
@Title : 9. Write a Python function that takes two lists and returns True if they have at
least one common member.
'''
def common_member(lst_1,lst_2):
    """
    Checks if two lists have at least one common member.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        bool: True if at least one common member exists, False otherwise.
    """
    for item in lst_1:
        if item in lst_2:
            return True
    return False
def main():
    list_1 = [1,3,4,5,6,7]
    list_2 = [11,33,55,1]
    ouput = common_member(list_1,list_2)
    # if ouput:
    #     print("list have common element ")
    # else:
    #     print("list does not have common element")
    print(ouput)
if __name__ == "__main__":
    
    main()