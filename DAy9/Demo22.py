from abc import ABC , abstractmethod
class A(ABC) :
    @abstractmethod 
    def withdraw(self,msg):
        pass;
	#logic 

class B(A) :
	def withdraw(self,msg):
		 balace =amount - userneterdAmount;