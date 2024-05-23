'''

@Author: Jainab sheikh

@Date: 2024-05-23

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-23

@Title : 12. Write a Python program to check multiple keys exists in a dictionary.

'''
def main():
    dict_1 = {1:12,1:23,2:34,4:23}
    # check using comaprison oprator and write key
    print(dict_1.keys()>={1,2,4})

        
 
if __name__ == "__main__":
    main()