
import math


# def greet():
#     print("Hello")
#     print("How do your do ")
#     print("ist´t the weather nice today")

# greet()


#functions that allows for inputs

# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"How do you do {name} ?")

# greet_with_name("Navjot")


#Function with more then one parameter


# def greet_with(name, location):
#     print(f"helloe {name}")
#     print(f"How is to be like in {location}")


# greet_with(name="Navjot",location="vienna")


# Write your code below this line 👇
# def paint_calc(height, width,cover):
#     number_of_cans = (height * width) / cover 
#     rounded_num_cans = math.ceil(number_of_cans)
#     print(f"You'll need {rounded_num_cans} cans of paint.")

# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)



# def prime_checker(number):
#     is_prime =  True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It´s a prime number")
#     else:
#         print("It´s not a prime number")

# n = int(input())
# prime_checker(number = n)


#* Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encrypt(text,shift):
#     slice_removed = alphabet[:shift]
#     slice_shifted = alphabet[shift:]
#     slice_shifted.extend(slice_removed)    
#     word = [] 
#     #find the index of letters in normal alpha bets
#     for i,val in enumerate(text):
#         normal_alpha = alphabet.index(val)
#         word.append(slice_shifted[normal_alpha])
        
#     cipher_text = ",".join(word)
#     print(f"The encoded text is {cipher_text}")

#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index (letter)
#         new_position = position - shift_amount
#         plain_text += alphabet [new_position]
#     print(f"The decoded text is {plain_text}")



# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# if direction == "encode":
#     encrypt(text=text, shift=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)


#########
#* FINAL
#########

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    