'''

@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title : 13. Write a Python program to count number of items in a dictionary value
that is a list.
'''
def count_list(lst):
    count = 0
    for x in lst:
        if isinstance(lst[x],list):
         count +=len(lst[x])
    return count
def main():
    my_dict = {'l1': [1,2,3], 'l2':[4,5,6], 'l3':[7,8,9]}
    print(type(my_dict))
    print(f"Number of item is list  :{count_list(my_dict)}")

        
 
if __name__ == "__main__":
    main()