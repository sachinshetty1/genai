class BankAccount(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def show_balance(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
    @abstractmethod
    def calculate_interest(self):
        pass
class SavingsAccount(BankAccount):
    def calculate_interest(self):
        interest = self.balance * 0.04
        print("Interest:", interest)
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Interest: 0")

savings = SavingsAccount(1001, 50000)
savings.show_balance()
savings.calculate_interest()

current = CurrentAccount(1002, 80000)
current.show_balance()
current.calculate_interest()