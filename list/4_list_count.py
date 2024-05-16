'''
@Author: Sheikh jainab
@Date: 2024-15-05
@Last Modified by: Author Name
@Last Modified time: 2024-15-05
@Title : Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are the same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

def count_string_start_last(string):
    """
    Counts the number of strings in a list where the string length is 2 or more 
    and the first and last character are the same.
    
    Args:
        string (list): A list of strings.
        
    Returns:
        int: The number of strings that meet the specified condition.
    """
    count = 0
    for element in string:
        if len(string) >= 2 and element[0] == element[-1]:
            count += 1
    return count

def main():
    """
    Main function to demonstrate the counting of strings with the same first and last character.
    """
    my_list = ['abc', 'xyz', 'aba', '1221']
    result = count_string_start_last(my_list)
    print(result)

if __name__ == "__main__":
    main()
