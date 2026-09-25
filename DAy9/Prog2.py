from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
class SMSNotification(Notification):
    def send(self, message):
        print("Sending SMS:", message)

class EmailNotification(Notification):
    def send(self, message):
        print("Sending email:", message)
class WhatsAppNotification(Notification):
    def send(self, message):
        print("Sending WhatsApp message:", message)
        
sms = SMSNotification()
sms.send("Your food is out for delivery")

email = EmailNotification()
email.send("Your order has been confirmed")

whatsapp = WhatsAppNotification()
whatsapp.send("Your delivery partner has arrived")