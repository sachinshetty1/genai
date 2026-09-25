class Payment:
    def process(self, amount):
        print("pay through the CASH method");
class UPIPayment(Payment):
    def process(self, amount):
        print(f"Processing UPI payment of Rs.{amount}")
        print("UPI payment completed successfully")
class CardPayment(Payment):
    def process(self, amount):
        print(f"Processing card payment of Rs.{amount}")
        print("Card payment completed successfully")
class NetBankingPayment(Payment):
    def process(self, amount):
        print(f"Processing net banking payment of Rs.{amount}")
        print("Net banking payment completed successfully")
# Pure object creation and method calling
upi_payment = UPIPayment()
upi_payment.process(1500)
print()
card_payment = CardPayment()
card_payment.process(2500)
print()
net_banking_payment = NetBankingPayment()
net_banking_payment.process(3500)