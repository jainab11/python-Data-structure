'''

@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title : 11. Write a Python program to convert a list into a nested dictionary of keys.

'''
def convert_list(lst,lst2,lst3):
    ans_dict ={}
    for lit in range(len(lst)):
        nested_dict = {lst2[lit]:lst3[lit]}
        ans_dict[lst[lit]] = nested_dict
    return ans_dict
def main():
    list_1 = [1,2,3,4]
    list_2 = ['a','b','c','d']
    list_3 = ['1a','2b','3c','4d']
    print(f"Nested dictionary is : {convert_list(list_1,list_2,list_3)}")
        
 
if __name__ == "__main__":
    main()
