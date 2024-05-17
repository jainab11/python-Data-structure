'''

@Author: sheikh jainab

@Date: 2024-05-11 

@Last Modified by: sheikh jainab

@Last Modified time: 2024-05-11 

@Title : 5. Write a Python program to remove an item from a set if it is present in the set.

'''
def remove_item(item,set1):
    if item in set1:
        set1.remove(item)
    return set1

def main():
    my_set ={1,3,5,7}
    remo = 9
    ans = remove_item(remo, my_set)
    print(ans)
    
    
if __name__ == "__main__":
    main()