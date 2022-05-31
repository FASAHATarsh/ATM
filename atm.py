class atm:
    def __init__(self, card, pin):
        self.card = card
        self.pin = pin
        self.amount = 10000

    def withdraw(self, w_amount):
        p_amount = self.amount
        n_amount = p_amount - w_amount
        print("You have withrawn ₹", n_amount, " from ₹", p_amount, ".")
        print("You have ₹", n_amount, " left in your bank account.")
        p_amount = n_amount

    def deposit(self, d_amount):
        p_amount = self.amount
        n_amount = p_amount + d_amount
        print("You have deposited ₹", d_amount, " to ₹", p_amount, ".")
        print("You have ₹", n_amount, " left in your bank account.")
        p_amount = n_amount

    def money(self):
        n_amount = self.amount
        print("You have ₹", n_amount, " in your bank account.")


def main():
    card_no = input("Enter your card number :")
    pin_no = input("Enter your pin :")
    user = atm(card_no, pin_no)

    obj = int(input("""
Choose your objective (1/2/3) -->
1. Check Balance
2. Deposit
3. Withdraw
--> """))
    if (obj == 1):
        user.money()
    elif(obj == 2):
        amount = int(input("Enter the amount :"))
        user.deposit(amount)
    elif(obj == 3):
        amount = int(input("Enter the amount :"))
        user.withdraw(amount)

if __name__ == "__main__":
    main()
