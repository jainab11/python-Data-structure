'''

@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title : 1. Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.


'''
def arrays(arr):
    for item in range(len(arr)):
        print(f" Index is {item} and element is -> {arr[item]}")

def main():
    arr = [1,3,5,7,9]
    print(arrays(arr))
    
    
if __name__ == "__main__":
    main()