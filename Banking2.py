def deposit():
  print("Enter account number , in which you want to Deposit")
  doc=int(input())
  t=all_accnum.count(doc)
  if t!=0 :
      ind=all_accnum.index(doc)
      print("Enter amount to Deposit")
      depamt=int(input())
      all_accbal[ind] = all_accbal[ind] + depamt
      print("Deposited Sucesfully")
      print("New Balance is ",all_accbal[ind])
  else :
      print("Invalid Account Number")

def withdraw():
  print("Enter account number , from which you want to Withdraw")
  doc = int(input())
  t = all_accnum.count(doc)
  if t != 0:
    ind = all_accnum.index(doc)
    print("Enter amount to Withdraw")
    witamt = int(input())
    all_accbal[ind] = all_accbal[ind] - witamt
    print("Withdraw Sucesfully")
    print("New Balance is ", all_accbal[ind])
  else:
    print("Invalid Account Number")

def pin_chng():
  print("Enter Account Number in which you want to change PIN :")
  doc=int(input())
  t=all_accnum.count(doc)
  ind = all_accnum.index(doc)
  print("Enter New pin")
  new_pin=int(input())
  print("Old PIN was :", all_pin[ind])
  all_pin[ind] = new_pin
  print("New Pin Number is :",new_pin)

def check_bal():
  print("Enter Account Number , for which you want to Check Balance :")
  doc = int(input())
  t = all_accnum.count(doc)
  ind = all_accnum.index(doc)
  print("Your Account Balance is : ",all_accbal[ind] )

def check_minBal():
  print("Enter Account Number , for which you want to check Minimum Balance :")
  doc = int(input())
  t = all_accnum.count(doc)
  ind = all_accnum.index(doc)
  if all_accbal[ind] < 2000:
    print("Account Balance is less than the limit")
    print("You have been charged a fee of 20rs for keeping a balance less than Minimum Required Balance")
    print("your acc balance is :",all_accbal[ind] - 20)
  else :
    print("Minimum balance required is 2000,You have :", all_accbal[ind])

def add_intrest():
  print("Enter Account Number , in which you want to Add Intrest :")
  doc = int(input())
  t = all_accnum.count(doc)
  ind = all_accnum.index(doc)
  intr = (all_accbal[ind]/100)*4
  all_accbal[ind] = all_accbal[ind] + intr
  print("Following Amount has been credited as Intrest :", intr)
  print("New Balance is ", all_accbal[ind])

def transfer_funds():
  print("Enter acc no from which you want to transfer funds ")
  doc = int(input())
  t = all_accnum.count(doc)
  ind = all_accnum.index(doc)
  print("Current acc has Rs:",all_accbal[ind])
  a=int(input("Enter the Amount you want to transfer :"))
  print("Enter Account Number , in which you want to Transfer the Funds :")
  newdoc = int(input())
  r=all_accnum.count(newdoc)
  index= all_accnum.index(newdoc)
  all_accbal[index]= all_accbal[index] + a
  print("Money Transfer Succefull , Acc balance is : ",all_accbal[index])
  all_accbal[ind] = all_accbal[ind] - a
  print(" Succefully Money Deducted From Acc, New Balance is :",all_accbal[ind])

def showall_details():
  print("Enter Account Number , for which you want All details to be Displayed  :")
  doc = int(input())
  t = all_accnum.count(doc)
  ind = all_accnum.index(doc)
  print("Account Number is :",all_accnum[ind])
  print("Account Balance is : ",all_accbal[ind])
  print("Account Pin is : ",all_pin[ind])

def addnew_acc():
    acc_no = int(input("Enter New Account Number :"))
    all_accnum.append(acc_no)
    acc_bal = int(input("Enter New Account's Balance :"))
    all_accbal.append(acc_bal)
    acc_pin = int(input("Enter New Account's PIN Number :"))
    all_pin.append(acc_pin)

def Exi():
  exit(0)


all_accnum = []
all_accbal = []
all_pin = []

i=1
while i<3:
  print("Accepting details of Account :",i)
  acc_no = int(input("Enter Initial Account Number :"))
  acc_bal = int(input("Enter Initial Account Balance :"))
  acc_pin = int(input("Enter Initial Account pin Number :"))
  all_accnum.append(acc_no)
  all_accbal.append(acc_bal)
  all_pin.append(acc_pin)
  i=i+1


while True:
    print("Select an Operation -")
    print("1) DEPOSIT")
    print("2) WITHDRAWAL")
    print("3) PIN CHANGE")
    print("4) SHOW BALANCE IN ACCOUNT")
    print("5) CHECK MINIMUM BALANCE")
    print("6) ADD INTREST")
    print("7) SHOW ACCOUNT INFORMATION")
    print("8) TRANSFER FUNDS")
    print("9) ADD NEW ACCOUNT")
    print("10) EXIT")
    choice = int(input())
    if choice==1:
        deposit()
    elif choice==2:
        withdraw()
    elif choice==3:
        pin_chng()
    elif choice==4:
        check_bal()
    elif choice==5:
        check_minBal()
    elif choice==6:
        add_intrest()
    elif choice==7:
        showall_details()
    elif choice==8:
        transfer_funds()
    elif choice==9:
        addnew_acc()
    elif choice==10:
        Exi()
