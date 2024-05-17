'''
@Author: Sheikh Jainab
@Date: 2024-17-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title: 8. Write a Python program to remove an item from a tuple.
'''
def remove_item(tup,item):
    lst = list(tup)
    for ele in lst:
        if ele == item:
            lst.remove(ele)
    ans = tuple(lst)
    return ans
def main():
    """
    Main function to execute the program.
    """
    my_tup = (1,4,6 ,'jainab',True, 3.4)
    # index_to_remove = 3
    # ans_tup = my_tup[:index_to_remove] + my_tup[index_to_remove+1:]
    # print(ans_tup)
    # new_tup = my_tup[1:]
    # print(new_tup)
    item = "jainab"
    ans = remove_item(my_tup,item)
    print(ans)
    
  

if __name__ == "__main__":
    main()