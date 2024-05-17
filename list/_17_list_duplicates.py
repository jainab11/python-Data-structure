'''
@Author: Sheikh Jainab
@Date: 2024-17-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title: 17. Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]'''
# def remove_duplicates(lst):
def remove_duplicates(input_list):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

def main():
    my_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    result = remove_duplicates(my_list)
    print(result)

if __name__ == "__main__":
    main()
