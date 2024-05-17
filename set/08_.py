'''

@Author: sheikh jainab

@Date: 2024-05-17

@Last Modified by: sheikh jainab

@Last Modified time: 2024-05-17

@Title :  8. Write a Python program to create set difference.


'''
def diff_of_set(set1,set2):
    ans_set = set()
    for item in set1:
        if item  not in set2:
            ans_set.add(item)
    return ans_set
def main():
    set1 = {1,2,2,3,4,5}
    set2 = {1,2,4,5,6}
    print("difference of set is ",diff_of_set(set1,set2))
    print(set1-set2) # by using -
    print("by using diiference keyword")
    print(set1.difference(set2))
    
if __name__ == "__main__":
    main()