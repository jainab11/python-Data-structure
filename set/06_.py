'''
@Author: sheikh jainab

@Date: 2024-05-11 

@Last Modified by: sheikh jainab

@Last Modified time: 2024-05-11 

@Title : 6. Write a Python program to create an intersection of sets.


'''

def intersection_of_set(set1,set2):
    ans_set = {0}
    for item in set1:
        if item in set2:
            ans_set.add(item)
    return ans_set
            
    
def main():
    set1 = {1,2,3,4,5}
    set2 = {1,2,4,5,6}
    
    result = set1.intersection(set2) # this is by using set intersection key word
    print(result)
    # anither method is by using & 
    print("The common elemnts in set is ")
    print(set1&set2)
    
    ans = intersection_of_set(set1,set2)
    
    
if __name__ == "__main__":
    main()