import time

class CryptoLocking:

    def __init__(self):
        self.accounts = {}

    def deposit(self, user, amount, lock_seconds):

        unlock_time = time.time() + lock_seconds

        self.accounts[user] = {
            "amount": amount,
            "unlock_time": unlock_time
        }

        print(f"{amount} ETH deposited for {user}")
        print(f"Funds will unlock after {lock_seconds} seconds.\n")

    def withdraw(self, user):

        if user not in self.accounts:
            print("No deposit found.")
            return

        current_time = time.time()

        if current_time < self.accounts[user]["unlock_time"]:
            print("Withdrawal blocked! Lock period has not ended.\n")
            return

        amount = self.accounts[user]["amount"]

        print(f"{user} successfully withdrew {amount} ETH\n")

        del self.accounts[user]


# Example
wallet = CryptoLocking()

wallet.deposit("0xABC123", 5, 10)

wallet.withdraw("0xABC123")

print("Waiting for lock period to expire...")
time.sleep(10)

wallet.withdraw("0xABC123")