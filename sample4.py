import random  ### to generate random word from the sequence
from words import word_list  ### generate list from another file
import time   ###to kill the time for a specific amount of time given
 
 
print("welcome to Hangman")
time.sleep(2)
name=input("write your name: ")
print("Hello!" +name+ ",,All the best")
time.sleep(2)

hangman1=[
   """
+-----+
      |
      |
      |
      |
      |
   ======      
   """,
"""
+-----+
   |  |
   0  |
      |
      |
      |
   ======      
   """,
"""
+-----+
   |  |
   0  |
   |  |
      |
      |
   ======      
   """,
   """
+-----+
   |  |
   0  |
  /|\ |
      |
      |
   ======      
   """,
"""
+-----+
   |  |
   0  |
  /|\ |
   |  |
      |
   ======      
   """,
"""
+-----+
   |  |
   0  |
  /|\ |
   |  |
  / \ |
   ======      
   """,
   
]
word=random.choice(word_list).lower()
guessed_correctly=[]
guessed_incorrectly=[]
tries=6
hangman_count=-1
while tries>0:
   output=""
   for letter in word:
      if letter in guessed_correctly:
         output+=letter
      else:
         output="_ "
   if output==word:
      break
   
   print("guess the word:- ", output)
   print(tries, ":chances left")
   guess=input("enter your guess:-").lower()
   if guess in guessed_correctly or guess in guessed_incorrectly:
      print("Already guess", guess)
   elif guess in word:
      print("YES!! you guess correct letter")
   else:
      print("SORRY!! you guess wrong letter")
      hangman_count+=1
      tries-=1
      guessed_incorrectly.append(guess)
      print(hangman1[hangman_count])
if tries>0:
   print("You guess correctly.....  and YOU WIN")
else:
   print("You guess it wrong..... TRY AGAIN")