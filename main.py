#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

randnumber = random.randint(0, 1)

if randnumber == 1:
  print("Heads")
else:
  print("Tails")








