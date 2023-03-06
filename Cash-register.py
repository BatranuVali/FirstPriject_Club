
from max_tip import Max_tip
from customer import Customer
from max_order import Max_order

customer=[]

ask=1
i=0
nr_cash=0
nr_card=0
exit_program=1
tip_total=0
order_total=0

max_order_ammount=0.0
max_order_name="None"


max_tip_tip=0.0
max_tip_name="None"


while exit_program :
 name="None"
 order_value=0.0
 paid_ammount=0.0
 paying_method="None"
 tip=0.0


 print('''
 -------------------------------------------------------------------------
 ************          |\   /|  * * *  \   |  |    |          ************
 ************          | \/  |  * *    | \ |  |    |          ************
 ************          |     |  * * *  |   \  |____|          ************
 ------------------------------------------------------------------------- 
 

 ''')
 name=input("Please enter the name of your customer : ")
 
 order_value=float(input("Please enter the value of their order : "))
 
 if order_value>max_order_ammount :
  max_order_ammount=order_value
  max_order_name=name

 order_total+=float(order_value)
 
 paying_method=input("Cash or card : ")
 

 wrong_input=1
 while wrong_input==1 :
  if paying_method == "cash" :
   nr_cash+=1
   wrong_input=0
  elif paying_method == "card" :
   nr_card+=1
   wrong_input=0
  else:
   print('Wrong input, enter "cash" or "card" : ')
   paying_method=input()
 
 paid_ammount=input("How much did they pay : ")
 
 tip=float(paid_ammount)-float(order_value)
 
 
 
 if tip > max_tip_tip :
  max_tip_tip=tip
  max_tip_name=name
 tip_total+=float(tip)
 customer.append(Customer(name,order_value,paid_ammount,paying_method,tip))
 i+=1
 print('''
 Do you want to add another customer? 
        Enter("y" or "n")  
          ''')
 while ask :
  x=input()
  if x=='n':
   exit_program=0
   ask=0
  elif x=='y':
   exit_program=1
   ask=0
  else:
   print('Wrong input, please enter "y" or "n" : ')
 


Max_tip(max_tip_name,max_tip_tip)
Max_order(max_order_name,max_order_ammount)


print("Today's total is :    "+str(order_total)+'$\n\n')
print("The largest order of today is "+str(max_order_name)+"'s : "+str(max_order_ammount)+"$\n\n")
print("The biggest tipper of today is : "+str(max_tip_name)+" "+str(max_tip_tip)+"$\n\n")
print(str(nr_cash)+" customers paid with cash.\n\n" )
print(str(nr_card)+" customers paid with card.\n\n")
print('''



-------------------------------------------------------------------------
 ************              * * *  \   |  |\                  ************
 ************              * *    | \ |  | \                 ************
 ************              * * *  |   \  |__\                ************
 ------------------------------------------------------------------------ 
''')  
 


