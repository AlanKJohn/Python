amount=int(input("enter a amount you would like to receive"))
time=int(input("enter how many years you will invest money"))
x = amount/time
print("To recieve "+str(amount)+" in "+str(time)+" years "+"you will need to invest "+str(x)+" per year")
y=x/12
print("also for every year you should deposit "+str(y)+" per month")
