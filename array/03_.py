'''

@@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title : 3. Write a Python program to get the number of occurrences of a specified element in an array.

'''
def count_occurence(arr,ele):
    count = 0
    for cnt in range(len(arr)):
        if ele  ==  arr[cnt]:
            count+=1
    return count
def main():
    arr =[1,2,3,2,3,1,2,4]
    ele = 2
    print(count_occurence(arr,ele)) 
    
    
if __name__ == "__main__":
    main()