'''
@Author: sheikh jainab

@Date: 2024-05-11 

@Last Modified by: sheikh jainab

@Last Modified time: 2024-05-11 

@Title : 11. Write a Python program to use of frozensets.


'''
def main():
    frozenset_1 = frozenset([1, 2, 3, 4, 5])
    frozenset_2 = frozenset([1,2,5,7,8,34])
    
    print(type(frozenset_1))
    
    print("union of frozzenset",frozenset_1.union(frozenset_2))
    
    print("intersection of frozenset",frozenset_1.intersection(frozenset_2))
    
    print("symmetric diffrence of frozen set",frozenset_1.symmetric_difference(frozenset_2))
    
    print("differnce of froxenset",frozenset_1.difference(frozenset_2))
    
    item = 6
    if item in frozenset_1:
        print("The item is in frozen set")
    elif item in frozenset_2:
        print("tThe item is in set 2")
    else:
        print("Item is not present")
    
    
if __name__ == "__main__":
    main()