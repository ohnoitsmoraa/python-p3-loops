#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i>=0:
        print(i)
        i -= 1
        print("Happy New Year!")
 
    # code goes here!
    pass

def square_integers(int_list):
  for number in  int_list:
      print(number ** 2)
      return [number **2 for number in int_list]

    # code goes here!
    

def fizzbuzz():
     i = 0
     while (i < 100):
        i += 1
        if (i % 3 == 0 and i % 5 ==0):
             print("FizzBuzz")
        elif(i % 3 == 0):
             print("Fizz")
        elif(i % 5 == 0):
             print("Buzz")
        else:
             print(i)

    # code goes here!