
def encoder (Password):
        encoded = []
        ABCs = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 """
        for n in Password: # this make every thing lower case to mach the ABCs
            for i in range(len(ABCs)): # make the AbBCs in to number for 0,26
                if n == ABCs[i]:#  if a letter in my name is the same as the letter in the ABCs then to multpy it by 3
                    z = i + 4
                    encoded.append(z*3)
        Pass = sum(encoded)
        return Pass

class Athentication:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.loaded = False
        self.encoder = encoder 

    def Register(self,):
        register_User = input("-Enter Username-")
        register_Pass = input("-Enter Password-")
        encodedPass = self.encoder(register_Pass)
        self.users[register_User] = encodedPass
        print(self.users)

    def LoadCheck (self,User,Pass,):
        if self.loaded is False :
            if User not in self.users:
                print("you do not have an account")
                self.loaded = False
                return self.loaded
            else:
                if self.encoder(Pass) == self.users[User]:
                    self.loaded = True
                    print(self.users)
                    return self.loaded
                else:
                     print("""wrong password""")
                     self.loaded = False
                     return self.loaded
        
Bank = Athentication()
while Bank.loaded == False:        
    print("JYK BANK")

    LogOrSign = int(input("if you want to be signed in enter 1 but if you have an account enter 2:>"))

    if LogOrSign == 2:
        User = input("Enter Username")
        Pass = input("Enter Password")
        Bank.LoadCheck(User,Pass)
    if LogOrSign == 1:
        Bank.Register()
        Money = int(input("how much money do you want deposit"))

#add away to add money/ also use the corint user