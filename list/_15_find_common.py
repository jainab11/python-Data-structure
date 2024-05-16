''''
@Author: Sheikh jainab
@Date: 2024-16-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title :14. Write a python program to check whether two lists are circularly identical.
'''
def common_list(list1, list2):
    common_items = []
    for item in list1:
        if item in list2:
            common_items.append(item)
    return common_items

def main():
    list1 = [1, 12,4, 33, 44, 5]
    list2 = [23,45,6,432,4]
    result = common_list(list1, list2)
    print("Common items:", result)
if __name__ == "__main__":
    main()

