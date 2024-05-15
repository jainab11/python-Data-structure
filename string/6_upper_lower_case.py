'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title :Write a Python script that takes input from the user and displays that input back in
upper and lower cases
'''

def main():
    """
    Main function to execute the program.
    """
    input_str = input("Enter a string : ")
    upper_case = input_str.upper()
    lower_case = input_str.lower()
    print("Upper string is : " , upper_case)
    print("lower case  is : ", lower_case)
    pass
if __name__ == "__main__":
    main()
