'''

@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title : 4. Write a Python program to remove the first occurrence of a specified element from an array.
'''
def remove_occ(arr,ele):
    """
    Function : This function return an array after removing  first occurence of sepcified numbers 
    
    Parameters : Function takes two parametesd array and element whic we want to remove
    
    Returns:
        int: return an array after removing that element
    """
    new_arr = []
    for item in range(len(arr)):
        new_arr.append(arr[item])
        if item == ele:
            new_arr.remove(ele)           
    return new_arr 
def main():
    arr = [2,1,2,1,1,43,1,2,1,3,4,5,3,4]
    sep_ele = 1
    print(remove_occ(arr,sep_ele))  
if __name__ == "__main__":
    main()