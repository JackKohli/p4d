# age = 29

# if age > 30:
#     print("you're getting old")
# else:
#     print("you're the right side of 30")

# grade = int(input("what was your score? "))
# if grade > 100:
#     print("extra credit?")
# if grade >= 90:
#     print("A grade")
# elif grade >= 80:
#     print("B grade")
# elif grade >= 70:
#     print("C grade")
# elif grade >= 0:
#     print("Fail")
# else:
#     print("how did you manage a negative score?")

# num = int(input("give me a number: "))
# if num >= 10 and num <=20:
#     print(f"{num} between 10 and 20")
# else:
#     print(f"{num} is not between 10 and 20")

fruits = ["bannana", "apple", "pear"]

for i in range(5):
    print(i)

num = 0
while num < 5:
    print(num)
    num += 1

print("2 to 20")
for x in range(2,21,2):
    print(x)

print("countdown")
num = 10
while num:
    print(num)
    num -= 1

import random

num = random.randint(1,10)
guess = 0
while guess != num:
    guess = int(input("guess a number: "))
    if guess > num:
        print("too high")
    if guess < num:
        print("too low")
    else:
        print("correct")

