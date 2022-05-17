# x_var = '22';
# print(type(x_var))
# int_var = int(x_var)
# print(type(int_var))

# a = 5
# b = 7
# c = -1

# my_calc = -b + (b**2 - 4*a*c)**0.5
# print(my_calc)
# final_calc = my_calc / (2*a)
# print(final_calc)


# a = 4/3
# pii = 3.142
# r= 5
# question_sln = a * pii * (r)**3
# print(question_sln)

# cover_price = (60/100) * 24.95 * 60
# print(cover_price)
# first_copy = (3 * 1) 
# print(first_copy)
# rem_copies = (0.75 * 59) 
# print(rem_copies)
# total_cost = first_copy + rem_copies + cover_price
# print(total_cost)

# start_time =  6*3600 + (52*60)
# easy_time = ((8*60) + 15)* 2
# tempo_time = ((7 * 60) + 12) * 3

# run_time = easy_time + tempo_time

# end_time = start_time + run_time
# end_time_hr = end_time//3600
# end_time_min = (end_time%3600)//60

# print(f"{end_time_hr}:{end_time_min}am")

# string_3 = "ghhh"
# # The three strings allows you to write on different linesin the editor
# string_4 = """ bdyuu
# hbj""" 

# string_1 = "This is a string"
# string_2 = "I love this string"
# print(string_1+ " " +string_2)
# print(string_1[:12])

# Hlai

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# username = first_name[:3]+last_name[-2:] 

# print(f"""Welcome , {first_name} {last_name}
# Your username will be {username}. 

# You have signed up successfully.
# cheers, 
# Himmie Team""")

# my_word = "The person is nice"


# print(count)

# your_word = input("Enter your sentence: ")
# word = your_word.lower()
# count = word.count("is")
# new_fmt = word.replace("is", "IS")
# print(f"""Your word is {word}, 
# the number of results found is {count}, 
# new result is {new_fmt}
# """)


# text = """An alternative to the life that we are living ehnnn, just do good and leave the rest to GOD, we are what we want to be
# not what they want us to be """
# search_for = input("Type here:").lower()
# print(f"{text.lower().count(search_for)} result(S) found")
# print(f"{text.lower().replace(search_for, search_for.upper())}")

# first_no = input("First Number Here: ")
# second_no = input("Second Number Here: ")
# third_no = input("Third Number Here: ")

# first = int(first_no)
# second = int(second_no)
# third = int(third_no)

# all_average = (first + second + third ) / 3

# print(f"""The average of the numbers {first_no}, {second_no} and {third_no} is {all_average}""")

# my_sentence = input("write something here: ")
# new_sentence = my_sentence.lower()
# final_sentence = new_sentence.capitalize()
# print(f"""Your sentence changed from {my_sentence}
# to {final_sentence}""")


# my_text = "I am learning python"
# new_text = my_text.replace("I am" , "You are")
# print(new_text)

# the_text = "I hope you had fun today in class"
# count_text = the_text.count("a")
# print(f"""The string 'a' appeared in the sentence 
# '{the_text}' a number of {count_text} times"""

#Functions
# greeting = 'Hello'
# def my_name():
#     print(greeting)

# my_name()  

# def fun2(n:int):
#     print(n**2)

# fun2(10)    

# def fun3(a,b,c):
#     print(a,b,c)
    
# fun3(1,2,3)
# fun3(a=3,b=1,c=3)

# fun3(2, b=2, c=4)
# arr = [2,3,4]

# def mean(arr):
#     mean = sum(arr)/len(arr)
#     return round(mean, 2)


# print("Enter your numbers")    
# vals = input(">>: ").split(",")
# mapped = list(map(int,vals))
# print(mean(mapped))

# score = int(input("Enter your exam score:\n:>"))
# if score <= 100:
#   if score >= 90:
#     print('A')
#   elif score >= 80:
#     print('B')
#   elif score >= 70:
#     print('C')    
#   elif score >= 60:
#     print('D') 
#   elif score >= 50:
#     print('E')   
#   elif score >= 40:
#     print('F')   
#   else:
#     print("Comrade why now!")   
# else:
#      print("You too sabi")    

# my_str = "my string is a string"
# a = list(map(lambda f:f.upper(), my_str))
# print("".join(a))

# help('keywords')

# import random
# a = [1,2,3,4,5,6,7,8,9]
# # random.shuffle(a)
# # b = random.sample(a,3)
# random.shuffle(a)
# com_choice = random.choice(a)
# user = int(input("Your choice\n:>"))
# if user == com_choice:
#    print("You win")
# else:
#     if user > com_choice:
#        print("Too high")
#     else:
#         print("Too low")
#     print("You lose")       


# import random
# val = ['scissors','rock','paper']
# random.shuffle(val)
# com_choice = random.choice(val)
# # print(com_choice)
# print("This is a game of rock, paper, scissors")
# user = input("Your choice\n:>").lower()
# if user == com_choice:
#   print("It is a tie")
# else:
#      if (user == "rock" and com_choice == "scissors"):
#         print("User wins")
#      if (user == "scissors" and com_choice == "rock"):
#         print("computer wins") 
#      if (user == "scissors" and com_choice == "paper"):
#         print("User wins")
#      if (user == "paper" and com_choice == "scissors"):
#         print("computer wins")  
#      if (user == "paper" and com_choice == "rock"):
#         print("User wins")
#      if (user == "rock" and com_choice == "paper"):
#         print("computer wins") 
#      if (user != val[0] and user != val[1] and user != val[2]  ):  
#         print("Input is not valid") 
# print("Play again")             


# for i in range(10):
#  if i == 5:
#      break
#     #continue
#  print(i)    

# for i in range(90, 120):
#     if i % 2 != 1:
#       continue
#     print(i)

# my_arr = [1,2,3,4,15,22,21,33,50,55,72,66,96]

# for i in my_arr:
#     if i % 5 == 0 or i % 3 == 0:
#        print(i)






# def prime_no(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     else: 
#         return True      

# no = int(input("Enter a number\n>>: "))
# if prime_no(no):
#     print(prime_no(no))
#     print(no, "is prime")
# else:
#     print(prime_no(no))
#     print(no, "isn't prime")

import random
print("Guess tje computer's choice to win the price")
a = [1,2,3,4,5]

random.shuffle(a)
trial = 3
score = 0

while trial > 0:
    print("\n Select a random number ")
    com_choice = random.choice(a)
    user = int(input("Your choice\n:>"))
    if user == com_choice:
        print("You win!")
        score+=2
        trial+=1
        print(f"You have won an extra trial")
        print(f"{trial} trial(s) left")
    else:
        if user > com_choice:
            print("Too High")
        else:
            print("Too Low")
        trial-=1
        print(f"{trial} trial(s) left")
print(f"\nYou scores {score} points") 
print("Game over")                      

  

   
  




