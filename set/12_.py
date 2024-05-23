'''

@Author: sheikh jainab

@Date: 2024-05-11 

@Last Modified by: sheikh jainab

@Last Modified time: 2024-05-11 

@Title : 12. Write a Python program to find maximum and the minimum value in a set.

'''
def max_min(s):
    new_set = sorted(s)
    print("smallest element is: ", new_set[0])
    print("biggest elemnt is: ",new_set[-1])
    return new_set
    
    
def main():
    my_set = (2,4,6,2,9,3,6)
    # sorted(my_set)
    # print(sorted(my_set))
    print(max_min(my_set))
   
    
if __name__ == "__main__":
    main()