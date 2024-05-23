'''

@Author: Jainab sheikh

@Date: 2024-05-18

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-18

@Title : 8. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''
def string_val(string):
    """ This functio convert the string to dictionary 

    Args:
        string (string and int): function atakes an string 

    Returns:
        Dictionary : This function return dictionary and count the number of charcter present in the string 
    """
    
    my_dict ={}
    for item in string:
       my_dict[item] = my_dict.get(item,0)+1
    return my_dict

def main():
    string  = "pineapple12" 
    result = string_val(string)
    print(result)
if __name__ == "__main__":
    main()
