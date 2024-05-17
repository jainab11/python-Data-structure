'''
@Author: Sheikh Jainab
@Date: 2024-17-05
@Last Modified by: Author Name
@Last Modified time: 2024-16-05
@Title: 16. Write a Python program to split a list based on first character of word 
'''
def split_list_by_first_character(lst):
    spilt_dict ={}
    for word in lst:
        first_char = word[0]
        # first_char = str(word)[0] # for list numbers
        if first_char not in spilt_dict:
            spilt_dict[first_char] = []
        spilt_dict[first_char].append(word)
    spilt_list = list(spilt_dict.values())
    return spilt_list
def main():
    my_list = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado", "blackberry"]
    second_list = [11,12,32,43,54,12,34,23,5465,23,45,65,56]
    result = split_list_by_first_character(my_list)
    result = split_list_by_first_character(second_list)
   
    print("List split based on first character of word:", result)

if __name__ == "__main__":
    main()
