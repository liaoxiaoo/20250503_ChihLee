import random
min = 1
max = 99
random_number = random.randint(min,max)
count = 0
print(random_number)
print("=======Guess Game Start=======\n\n")
while True:
  input_number = int(input(f"Input number({min})~({max}):"))
  count += 1
  if (input_number == random_number):
    print(f"BINGO!,The answer is {input_number}")
    print(f"u guess {count} times")
    break
  elif (input_number > random_number):
    print(f"Too Big !")
    max = input_number - 1
  elif (input_number < random_number):
    print(f"Too Small !")
    min = input_number + 1
  print(f"u guessed {count} times")

print("Congratulations!")
print("^___^")