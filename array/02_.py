'''

@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title : 2. Write a Python program to reverse the order of the items in the array.


'''
def reverse_array(arr):
    rev_arr = []
    for item in range(len(arr)-1,-1,-1):
        rev_arr.append(arr[item])
    # print(rev_arr)
    return rev_arr
    
def main():
    arr =[2,4,6,8]
    print(f"original array is  {arr}")
    
    print(f"reversed array is {reverse_array(arr)}")
    
    
if __name__ == "__main__":
    main()