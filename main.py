import string
import random
import threading
import os
import sys

def randit(y):
  return ''.join(random.choice(string.ascii_letters)for x in range(y))

def randit1(z):
  return ''.join(random.choice(string.ascii_lowercase)for x in range(z))

def randit2(m):
  return ''.join(random.choice(string.ascii_uppercase)for x in range(m))

#----------------------MENU--------------------------
print("Welcome to Random Character Generator")
print("Leef!#0001 - Discord")
print("""
[1] Generate Random Characters
[2] Generate Random Uppercase Characters
""")
opt1 = input("Choose >: ")

if opt1 == '1':
      os.system('cls')
      opt2 = input("How Many Threads (MAX 99): ")
      opt2 = int(opt2)
      for x in range(opt2):
        while True:
          threads = []
          print(randit(99)) # Generating 99 Random Characters 
if opt1 == '2':
      os.system('cls')
      opt4 = input("How Many Threads (MAX 99): ")
      opt4 = int(opt4)
      for x in range(opt4):
        while True:
          threads = []
          print(randit2(99)) # Generating 99 Uppercase Characters
