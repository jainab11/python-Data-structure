'''
@Author: Sheikh Jainab
@Date: 2024-17-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title: 5. Write a Python program to find the repeated items of a tuple.

'''
def rep_tup(tup):
    ans_tup =set()
    for item in tup:
        if tup.count(item)>1:
            ans_tup.add(item)
    return ans_tup
def main():
    """
    Main function to execute the program.
    """
    my_tuple = (1,4,6,1,2,3,4)
    ans = rep_tup(my_tuple)
    print(ans)
  

if __name__ == "__main__":
    main()