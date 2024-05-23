'''

@Author: Jainab sheikh

@Date: 2024-05-23

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-23

@Title : 2. Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''
def main():
      dict_1 ={0:10,1:20}
      print("dictionary before adding ",dict_1)
      dict_1[2]=30
      print(dict_1)
      dict_1.update({3:40})
      print(dict_1)
      
      
if __name__ == "__main__":
    main()
