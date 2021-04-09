class bankaccount:

    def __init__(self, clname, cltype, cldeposit):
        self.nameclass = clname
        self.typeclass = cltype
        self.depositclass = cldeposit
        self.acc = 0


    def log(self, message):
        self.mylog = open("Log.txt", "a")

        print(message, file = self.mylog)

        self.mylog.close()

    def newacc(self):

        self.log("=================================\n")
        self.log("Acoount name:"+self.nameclass)
        self.log("Acoount type:"+self.typeclass)
        self.log("Desposit amount:"+self.depositclass)

    def findacc(self):
        mylog = open("Log.txt", "a")
        self.acc = mylog.tell()
        mylog.close()
        return self.acc

def findaccount(start,en):
 f1 = open("Log.txt")
 f1.seek(start)

 a = f1.read(en-start)
 print(a)
 f1.close()

def enter():
 name = input("Enter the name of the account holder:")
 type = input("Enter the type of the account:\n"
              "1.Savings account.\n"
              "2.Check aacount.\n"
              ":")
 if type == '1':
     type12 = "Savings account"
 elif type == '2':
     type12 = "Checking account"
 else:
     print("Wrong input!,Enter again")
     exit()

 deposit = input("Enter the deposit amount:")
 return name,type12,deposit

print("      Welcome to Bank of India\n"
      "**************************************")
input("  Please press enter key to Proceed!")

print("*****************************\n"
      "<=   1.Open and account.   =>\n"
      "<=   2.Check your balance  =>\n"
      "*****************************\n")
choice = input("Enter your choice:")
if choice == '1':

 name1, type1, desp1 = enter()
 b = bankaccount(name1,type1,desp1)
 vss = b.findacc()
 b.newacc()
 accountno = b.findacc()

 print("\n===================================\n"
       "Thank your for creating an account!\n"
       "We offer your our best service.\n"
       "        Welcome Customer       \n"
       "Vss id:"+str(vss))
 print("Account NO.:"+str(accountno))

elif choice =='2':
 starttofun = int(input("Enter your Vss id:"))
 endtofun = int(input("Enter your account number code:"))
 findaccount(starttofun, endtofun - 1)













