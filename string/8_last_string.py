'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title :8. Write a Python program to get the last part of a string before a specified character.

'''
def last_string(str, charcter):
    parts = str.split(charcter)
    if len(parts) > 1:
        return parts[-2]
    else:
        return None
def main():
    str = input(" Enter a string : ")
    speicified_string = input(" Enter a specified string : ")
    output = last_string(str, speicified_string)
    print(f"last part before  {speicified_string} is : {output}")
if __name__ =="__main__":
    main()
