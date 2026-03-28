balance=0
while True:
    print("---ATM MENU---")
    print("1. Check Balnce")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("choose an option:")
    if choice =="1":
        print("Your balance is:",balance)
    elif choice =="2":
        amount= float(input("Enter amount to deposit: "))
        balance += amount
        print ("Deposited:", amount)
    elif choice == "3":
        amount=float(input("Enter amount to withdraw:"))
        if amount > balance:
            print ("Insufficient funds!")
        else:
            balance-= amount
            print("Withdrawn:, amount")
    elif choice =="4":
        print("Thank you, have a nice day!")
        break
    else:
      print("Invalid option. Try again.")


    
