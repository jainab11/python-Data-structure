'''
@Author: Sheikh jainab
@Date: 2024-16-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title :13. Write a Python program to append a list to the second list.

'''
def append_list(lst1,lst2):
    lst1.extend(lst2)
    return lst1
# Example usage:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = append_list(list1, list2)
print("Appended list:", result)

'''def append_lists(list1, list2):
    return list1 + list2

# Example usage:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = append_lists(list1, list2)
print("Appended list:", result)
'''