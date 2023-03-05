customer={
"name"
"order_value"
"paid_ammount"
"paying_method"
"tip"
}
max_tip={
 "ammount"
 "name"
}
max_tip.ammount=0
max_order={
 "ammount" 
 "name"
}
max_order.ammount=0
ask=1
i=0
nr_cash=0
nr_card=0
exit_program=1
tip_total=0
order_total=0
customer=[]
while exit_program :
 print('''
 -------------------------------------------------------------------------
 ************          |\   /|  * * *  \   |  |    |          ************
 ************          | \/  |  * *    | \ |  |    |          ************
 ************          |     |  * * *  |   \  |____|          ************
 ------------------------------------------------------------------------- 
 

 ''')
 customer[i].name=input("Please enter the name of your customer : ")
 
 customer[i].order_value=input("Please enter the value of their order : ")
 
 if customer[i].order_value>max_order.ammount :
  max_order.ammount=customer[i].orer_value
  max_order.name=customer[i].name

 order_total+=float(customer[i].order_value)
 
 customer[i].paying_method=input("Cash or card : ")
 

 wrong_input=1
 while wrong_input==1 :
  if customer[i].paying_method == "cash" :
   nr_cash+=1
   wrong_input=0
  elif customer[i].paying_method == "card" :
   nr_card+=1
   wrong_input=0
  else:
   print('Wrong input, enter "cash" or "card" : ')
   customer[i].paying_method=input()
 
 customer[i].paid_ammount=input("How much did they pay : ")
 
 customer[i].tip=float(customer[i].paid_ammount)-float(customer[i].order_value)
 
 
 
 if customer[i].tip > max_tip.ammount :
  max_tip.ammount=customer[i].tip
  max_tip.name=customer[i].name
 tip_total+=float(customer[i].tip)
 
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




print("Today's total is :    "+str(order_total)+'$\n\n')
print("The largest order of today is "+str(max_order.name)+"'s : "+str(max_order.ammount)+"$\n\n")
print("The biggest tipper of today is : "+str(max_tip.name)+" "+str(max_tip.ammount)+"$\n\n")
print(str(nr_cash)+" customers paid with cash.\n\n" )
print(str(nr_card)+" customers paid with card.\n\n")
print('''



-------------------------------------------------------------------------
 ************              * * *  \   |  |\                  ************
 ************              * *    | \ |  | \                 ************
 ************              * * *  |   \  |__\                ************
 ------------------------------------------------------------------------ 
''')  
 


