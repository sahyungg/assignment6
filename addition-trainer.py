import random

score = 0

print("Answer the following equations: ")

for i in range(10):
    n1 = random.randrange(0, 99)
    n2 = random.randrange(0, 99)

    print('Add: %s + %s' % (n1, n2))
    answer = n1 + n2

    player = int(input("="))
    
    if player == answer:
         print("Hooray! You got it right!")
         score += 1
    elif player != answer:
        print("Aww too bad.. Try again!")

print(f"Total score: {score}/10")

if score > 7:
    print("Wow! You're so smart! Sana all...")
else:
    print("You can do better next time!")