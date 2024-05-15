'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : 10. Write a Python program to count occurrences of a substring in a string.

'''
def occurence(str,substr):
    count = 0
    start = 0
    while True:
        start = str.find(substr,start)
        if start != -1:
            count +=1
            start +=1
        else:
            break
    return count
    
def main():
    str = input(" Enter a string : ")
    substring = input(" Enter substring : ")
    output = occurence(str,substring)
    print(f"occurence of substring is {output}")
if __name__ =="__main__":
    main()