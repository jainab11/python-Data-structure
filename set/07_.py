'''

@Author: sheikh jainab

@Date: 2024-05-17

@Last Modified by: sheikh jainab

@Last Modified time: 2024-05-17 

@Title : 7. Write a Python program to create a union of sets.


'''

def union_of_set(set1,set2):
    ans_set = set()
    for item in set1:
        ans_set.add(item)
    for item   in set2:
            ans_set.add(item)
    return ans_set
            
def main():
    set1 = {1,2,2,3,4,5}
    set2 = {1,2,4,5,6}
    
    result = set1.union(set2) # this is by using set union key word
    print(result)
    # anither method is by using & 
    print("The union of elemnts in set is ")
    print(set1|set2)
    
    ans = union_of_set(set1,set2)
    print("function code")
    print(ans)
    
    
if __name__ == "__main__":
    main()