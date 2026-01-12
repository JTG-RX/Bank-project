import json
DATA_FILE = "users.json"

def encoder (Password):
        encoded = []
        ABCs = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890<>/?{ }[]()_-!@#$%^&*~`,.:;'|"""
        for n in Password: 
            for i in range(len(ABCs)): 
                if n == ABCs[i]:
                    z = i + 4
                    encoded.append(z*3)
        Pass = sum(encoded)
        return Pass

class Authentication:
    def __init__(self):
        self.current_user = None
        self.loaded = False
        self.encoder = encoder
        self.load_users()

    def Register(self,):
        register_User = input("-Enter Username-")
        register_Pass = input("-Enter Password-")
        encodedPass = self.encoder(register_Pass)
        self.users[register_User] = {"password":encodedPass,"balance":454,"records":[]}
        self.save_users()
        return register_User, register_Pass

    def LoadCheck (self,User,Pass,):
            if User not in self.users:
                print("you do not have an account")
                self.loaded = False
                return self.loaded
            else:
                if self.encoder(Pass) == self.users[User]["password"]:
                    self.loaded = True
                    self.current_user = User
                    return self.loaded
                else:
                     print("""wrong password""")
                     self.loaded = False
                     return self.loaded
                
    def deposit(self,):
        depositCheck = False
        while depositCheck == False:
            Deposits = int(input("How much do you want to deposit: numbers only:>"))
            if Deposits <= 0:
                print("youcan not deposit 0 or a negative Balance")
            else:
                depositCheck = True
        self.users[self.current_user]["records"].append(f"{self.current_user} deposited {Deposits}")
        self.users[self.current_user]['balance'] += Deposits
        self.save_users()
        print(f"you now have{self.users[self.current_user]['balance']}")

    def Withdraw(self,):
        WithdrawCheck = False
        while WithdrawCheck == False:
            Withdraw = int(input("How much do you want to Withdraw: numbers only:>"))
            self.users[self.current_user]["records"].append(f"{self.current_user} Withdraw {Withdraw}")
            if Withdraw >= self.users[self.current_user]["balance"]:
                print("you can not withdraw mover than your balance")
            elif Withdraw <= 0:
                print("you can not withdraw a negative amout")
            else:
                WithdrawCheck = True   
        self.users[self.current_user]['balance'] -= Withdraw
        self.save_users()
        print(f"you now have{self.users[self.current_user]['balance']}")
    
    def mainMenu(self,):
        Quit = False
        while Quit == False:
            DW = input("""You can do the following \n -if you want to Deposit enter <Deposit> \n -if you want to Withdraw enter <Withdraw> \n -if you want to see your Record enter <Record>
                        \n- if you want to see your balance <Balance>\n -or if you want to quit enter <Q>""")
            self.users[self.current_user]["records"].append(f"main Menu actions {DW}")
            if DW == "Deposit":
                self.deposit()
            elif DW == "Withdraw":
                self.Withdraw()
            elif DW == "Balance":
                print(f"you balance is {self.users[self.current_user]['balance']}")
            elif DW == "Q": 
                self.save_users()   
                Quit = True
                self.loaded = False
            elif DW == "Record":
                for r in self.users[self.current_user]["records"]:
                    print(r)
            else:
                print("please enter a valid option")
    def load_users(self,):
        try:
            with open(DATA_FILE,'r') as file:
                self.users = json.load(file)
            for user_data in self.users.values():
                if "records" not in user_data or not isinstance(user_data["records"], list):
                    user_data["records"] = []
        except FileNotFoundError:
            self.users = {}
    def save_users(self,):
        with open(DATA_FILE,"w") as file:
            json.dump(self.users, file, indent=4)
   
Bank = Authentication()
while Bank.loaded == False:        
    print("JYK BANK")

    LogOrSign = int(input("if you want to be signed in enter 1 but if you have an account enter 2:>"))

    if LogOrSign == 2:
        User = input("Enter Username")
        Pass = input("Enter Password")
        Bank.LoadCheck(User,Pass)
        if Bank.loaded == True:
            print(f"""welcome{User} \n 
                  your balance is {Bank.users[User]['balance']} """)
            Bank.mainMenu()
    if LogOrSign == 1:
        username,password = Bank.Register()
        Bank.LoadCheck(username,password)
        if Bank.loaded == True:
            print(f"""welcome {username} \n 
                  your balance is {Bank.users[username]['balance']} """)
            Bank.mainMenu() 
