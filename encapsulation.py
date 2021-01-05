class customer:
    custacno=123456789
    custname="vishal"
    custaddress="hyderabad"
    custbal=1000000.00
    def deposite(self,damt):
        self.custbal=self.custbal+damt
        print(self.custbal)
    def withdraw(self,wamt):
        self.custbal=self.custbal-wamt
        print(self.custbal)

    def display(self):
        print(self.custacno)
        print(self.custname)
        print(self.custaddress)
        print(self.custbal)
c1=customer()

c1.deposite(5000.00)
c1.withdraw(10000.00)
c1.display()
