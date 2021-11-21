def bank_balance():
    BANK_BALANCE = 0
    ask_user_for_transactions = input("Did you earn or spend this week?")
    print(ask_user_for_transactions)
    while ask_user_for_transactions != "No":
        list_of_words = ask_user_for_transactions.split()
        print(list_of_words)
        length_of_list_of_words = len(list_of_words)
        if "earn" in list_of_words or "earned" in list_of_words :
            earnings_str = list_of_words[length_of_list_of_words -1]
            earning_int = int(earnings_str)
            BANK_BALANCE += earning_int
            print("Your bank balance is: $" + str(BANK_BALANCE))
            ask_user_for_transactions = input("Did you earn or spend anything else this week?")
        elif "spent" in list_of_words or "bought" in list_of_words:
            spending_str = list_of_words[length_of_list_of_words - 1]
            spending_int = int(spending_str)
            BANK_BALANCE -= spending_int
            if BANK_BALANCE < 0:
                print("You have budgeted poorly and spent more than your earnings.")
                break
            else:
                print("Your bank balance is: $" + str(BANK_BALANCE))
                ask_user_for_transactions = input("Did you earn or spend anything else this week?")
    if (BANK_BALANCE > 0):
        print("Well done, you have a savings of: $" + str(BANK_BALANCE))
    else:
        print("You have spent poorly and have to budget properly")
bank_balance()


