'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 12. Write a Python program to lowercase first n characters in a string.
'''
def lower_case(str,length):
    if length <= 0:
        return str
    result = ""
    for word,char in enumerate(str):
        if word<length:
            if 'A'<= char <='Z':
                result += chr(ord(char)+32)
            else:
                result += char.lower()
                
        else:
            result+=char
    else:
        return result
    
def main():
   string = "HELLO, HOW ARE YOU "
   length = 12
   output = lower_case(string,length)
   print(output)
if __name__ == "__main__":
    main()
    
# def lowercase_first_n(string, n):
#     if n <= 0:
#         return string
#     return string[:n].lower()+string[n:]