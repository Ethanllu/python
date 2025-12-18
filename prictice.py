import random
Age = random.randint(1,100)
while True:
    s = input("input number:")
    try:
        guess = int(s)
    except ValueError:
        print("please input Number!")
        continue
    if guess < Age:
        print("too small")
    elif guess > Age:
        print("too big")
    else:
        print("right")
        break