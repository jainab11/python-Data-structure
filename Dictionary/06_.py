'''

@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title :6. Write a Python program to remove a key from a dictionary.

'''
def remove_key(my_dict):
    ans_dict = list()
    for item in my_dict.values():
        ans_dict.append(item)

    return ans_dict
        
def main():
    my_dict = {1:10,2:20,3:30,4:40} 
    # Using del to remove a dict
    del my_dict[4]
    print(my_dict)
    print(remove_key(my_dict))      
if __name__ == "__main__":
    main()