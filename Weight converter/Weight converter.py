def conv():
    a = int(input("Enter a weight 👉: "))
    b = str(input("Is this kg or lbs 😝: "))
    if b == 'lbs':
        c = a * 0.45
        print(f"Your weight in kg: {c} 💪")
    elif b == 'kg':
        d = a * 2.20
        print(f"Your weight in lbs: {d} 💪")
    e = str(input("Do you want to continue? 🤭 (write 'yes' or 'no') "))
    if e == 'yes':
        conv()
    elif e == 'no':
        print("Thank you for using my program 😍\nGood bye 👋")

def main():
    print("Hello user 👋\nWelcome in weight converter program ⚖️")
    conv()
if __name__ == '__main__':
    main()