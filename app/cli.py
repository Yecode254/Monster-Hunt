
def main():
    print(" Welcome to Monster Hunt CLI!")
    while True:
        print("\nMain Menu:")
        print("1. Catch a Monster")
        print("2. View My Collection")
        print("3. Battle a Wild Monster")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ")

        if choice == "1":
            print("Catching logic goes here...")
        elif choice == "2":
            print("Viewing collection...")
        elif choice == "3":
            print("Initiating battle...")
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1–4.")

if __name__ == "__main__":
    main()
