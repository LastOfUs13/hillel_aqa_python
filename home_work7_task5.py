def atm(*args):
    """pin_code = 1366"""
    ask_first = int(input("Please type the pin_code - "))
    if ask_first == 1366:
        print('Here is your money >>')
    elif ask_first != 1366:
        ask_second = int(input("Wrong data.Try again - "))
        if ask_second == 1366:
            print('Here is money >>')
        elif ask_second != 1366:
            ask_third = int(input("Wrong data.You have last try - "))
            if ask_third == 1366:
                print('Here is your money >>')
            else:
                print('Card is blocked')

if __name__ == "__main__":
    atm()

