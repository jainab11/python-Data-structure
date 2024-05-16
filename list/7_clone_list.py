'''
@Author: Sheikh jainab
@Date: 2024-15-05
@Last Modified by: Author Name
@Last Modified time: 2024-15-05
@Title : 7. Write a Python program to clone or copy a list.
'''
def main():
    """
    Clone or copy a list.
    """
    
    lst = [1,3,5,7]
    copy = []
     # Iterate over the elements of lst and append them to copy
    for item in range(0,len(lst)):
        copy.append(lst[item])
    return copy

if __name__ == "__main__":
    
     clone = main()
     print("clones list is :" , clone)