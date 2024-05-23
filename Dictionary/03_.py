'''

@Author: Jainab sheikh

@Date: 2024-05-23

@Last Modified by: Jainab sheikh

@Last Modified time: 2024-05-23

@Title :3. Write a Python script to concatenate following dictionaries to create a new
one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
def main():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    new_dict = {"dic1":dic1,
                "dic2":dic2,
                "dic3":dic3}
    print(new_dict)
    # or for one dict can use copy dict
      
            
if __name__ == "__main__":
    main()