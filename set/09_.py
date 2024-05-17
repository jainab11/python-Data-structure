'''
@Author: sheikh jainab

@Date: 2024-05-11 

@Last Modified by: sheikh jainab

@Last Modified time: 2024-05-11 

@Title : 9. Write a Python program to create a symmetric difference.


'''
def symmetric_of_set(set1,set2):
    """

         Description:

            This function is used to show symmetric differnce between two set

         Parameters:
         sets with some value

         Return:

            Returns the symmetric difference .
            
        """ 
    ans_set = set()
    # adding element which is in set 1
    for item in set1:
     if  item not in set2:
            ans_set.add(item)
    # adding element which is set 2
    for item in set2:
        if item not in set1:
            ans_set.add(item)
    return ans_set
            
def main():
    set1 = {1,2,3,4,5}
    set2 = {1,2,4,5,6,7}
    print(symmetric_of_set(set1,set2))# this uotput display function answer
    print(set1.symmetric_difference(set2))#this display by using keyword
    print(f"by using ^ keyword",set1^set2)#this is by using ^ this
    
    
if __name__ == "__main__":
    main()