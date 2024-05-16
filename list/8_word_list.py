'''
@Author: Sheikh jainab
@Date: 2024-15-05
@Last Modified by: Author Name
@Last Modified time: 2024-15-05
@Title : 8. Write a Python program to find the list of words that are longer than n from a
given list of words
'''
def long_word_list(word_lst ,n):
    list_longer_word = []
    for word in word_lst:
        if len(word)> n:
            list_longer_word.append(word)
    return list_longer_word
            
def main():
    list_input = ["APPLE","BANANA","MANGO","GRAPE","KIWI","ORANGE","PINEAPPLE","WATERMELON","012345"]
    n = 5
    result = long_word_list(list_input,n)
    print("Words longer than", n, "characters:", result)

if __name__ == "__main__":
    
    main()
     