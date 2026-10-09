import random
print("="*39)
print("|      🎯 ODD NUMBER HUNTER 🎯        |")
print("="*39)
print("\nWelcome to the Odd Number Hunter! 🕵️‍♂️")
print("\nPick Your Level of Difficulty! 🏹")
print("\n1. Easy (1-25)")
print("2. Medium (1-50)")
print("3. Hard (1-100)")
a = int(input("\nEnter your choice (1-3): "))
if a == 1:
    print("\nYou're going to hunt for an odd number")
    print("between 1 and 25! 🏹")
    secret_number = random.randint(1, 25)
elif a == 2:
    print("\nYou're going to hunt for an odd number")
    print("between 1 and 50! 🏹")
    secret_number = random.randint(1, 50)
elif a == 3:
    print("\nYou're going to hunt for an odd number")
    print("between 1 and 100! 🏹")
    secret_number = random.randint(1, 100)
else:
     print("❌ That's not a valid choice! Please choose 1, 2, or 3. ❌")
if secret_number % 2 == 0:
    secret_number += 1
trys = 0
while True:
    guess = int(input("\nEnter your guess 🎯: "))
    trys += 1
    if guess == secret_number:
        print("🎉 Congratulations! You found the odd number! 🎉")
        print("-"*5, " ૮ ˶ᵔ ᵕ ᵔ˶ ა ", "-"*5)
        print(f"It took you {trys} tries!")
        break
    elif guess < secret_number:
        print("❌ Too low! Try again! ❌")
    else:
        print("❌ Too high! Try again! ❌")
    print(f"You have used {trys} tries so far.")
    if trys == 7:
        print("\n😔 Sorry, you've used all your tries!")
        print("The odd number was:", secret_number)
        break
    if secret_number + 1 == guess or secret_number - 1 == guess:
                    print("\n🔥 You're RED HOT! 🔥")
    elif secret_number + 5 == guess or secret_number - 5 == guess:
                    print("\n🔥 You're WARM! 🔥")
    elif secret_number + 10 == guess or secret_number - 10 == guess:
                    print("\n❄️ You're COLD! ❄️")
    else:
                    print("\n❄️  You're FREEZING!  ❄️")
                    print("But keep trying! You can do it! 💪")
if guess % 2 == 0:
    print("❌ That's not an odd number it's even! ❌")
    print("Please try again! 🎯\n and remember, the secret number is odd! \nso you answer with an odd number only!")
