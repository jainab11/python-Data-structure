'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 3. Write a Python program to get the smallest number from a list.


'''
def smallest(lst):
    smaller =lst[0]
    for ele in lst:
        if smaller > ele:
            smaller = ele
    return smaller
    

def main():
    my_list = [9, 2, 3, 4, 5]
    smallest_item = smallest(my_list)
    print(smallest_item)


if __name__ == "__main__":
    main()