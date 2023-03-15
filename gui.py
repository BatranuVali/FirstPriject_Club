from tkinter import*
from customer import*

customer=[]
customer_number=1
nr_cash=0
nr_card=0
order_value=0

root = Tk()
root.geometry("500x500")
root.title("Cash Register")


def counter () :
    customer_number+=1

client_number_msg=Label(text= "Client number : "+str(customer_number), font=75)
client_number_msg.grid(row=0,column=0)


order_value_msg=Label(text= "Order value : ", font=75)
order_value_msg.grid(row=1,column=0)

order_value=IntVar()
order_value_entr=Entry(root)
order_value_entr.grid(row=1,column=1)
order_value=order_value_entr.get()


payment_msg=Label(text= "Payment : ", font=75)
payment_msg.grid(row=2,column=0)

button_cash=Checkbutton(root,text="Cash",font=75,variable=nr_cash)
button_cash.grid(row=2,column=1)

button_card=Checkbutton(root,text="Card",font=75,variable=nr_card)
button_card.grid(row=2,column=2)

 










root.mainloop()