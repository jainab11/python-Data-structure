'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 10. Write a Python program to count occurrences of a substring in a string.
'''
def reverse_string(str):
    reverse = ''
    for i in range( len(str) -1,-1,-1):
        reverse += str[i]
    return reverse
def main():
    string1 = "jainab"
    # reverse_string = string1[::-1]
    output = reverse_string(string1)
    print(output)
if __name__ == "__main__":
    main()