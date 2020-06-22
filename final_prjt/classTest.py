class BusinessCard:
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):
        print("Name is:", self.name)
        print("Email is:",self.name)

member1 = BusinessCard()
member1.set_info("testName",
                 "testEmail",
                 "testAddr")
member1.print_info()
print("="*30)

class Stock:
    market = 'kospi'
print(dir())
