'''
@Author: sheikh jainab

@Date: 2024-05-11 

@Last Modified by: sheikh jainab

@Last Modified time: 2024-05-11 

@Title : 10. Write a Python program to clear a set.


'''
def main():
    my_set ={1,3,5,7}
    ans_set = set()
    print(my_set)
    for item in my_set:
        ans_set.add(item)
        print(ans_set)
        ans_set.remove(item)
    print("printing answer set")
    print(ans_set)
    
    print(my_set)
    print("after for loop")
    
    print(my_set.clear())

    
    
if __name__ == "__main__":
    main()