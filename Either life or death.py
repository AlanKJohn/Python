print(" Wecome to EITHER LIFE OR DEATH")
A=input("whats your name ?")

while True:
    C=int(input("Your in one end of the room.you need to get to other end of the room where your friend is waiting.but there are zombies.how will you kill the zombies enter value 1 for knife and 2 for fire"))
    if C!=2:
       D=("zombies cant be cut.they ate you and you died.game over start again")
       print(D)
       C=0
    if C==2:
       break     
E=("congrats you have advanced to the next level")
print(E)
F=input("what's your friend name?")
while True:
    G=int(input("you and"+F+" have escaped sucessfully. now you guys are surrounded by zombies in the stadium now what do you do know 1 for digging a tunnel and 2 for turning of the lights next to you."))
    if G!=2:
       H=("it takes time to dig a tunnel until then you will be eaten up. game over")
       print(H)
       G=0
    if G==2:
        break 
I=("the zombies can't even see as the lights are turned of. you and"+F+" have escaped and entered the wild jungle.")
print(I)
while True:
    J=int(input("You and"+F+" have entered the wild jungle.Now you and"+F+" sees a wild bear, use your resources to deafet the wild bear the rescources are enter the rescources number to use it 1 for knife and 2 for firetorch"))
    if J!=2:
        K=("It is a wild bear so while you try to kill it avoides your attack and eat you. GAME OVER")
        print(K)
        J=0
    if J==2:
        break
L=("The wild bear has ran away due to the fire torch")
print(L)
while True:
    M=int(input("you and"+F+" have entered a cave then suddenly an earthquake occurs and the entrance of the cave had closed now you and"+F+" have got trapped in the cave you see some miner tools they are (enter the value for using the item) 1 for an explosive landmine and 2 for drilling machine."))  
    if M!=2:
        O=("The landmine had exploded to much that the rocks above you have fallen on you and"+F+" have died.GAME OVER.")
        print(O)
        M=0
    if M==2:
        break
N=("Great choice you and"+F+" have drilled the rocks and escaped.")
print(N)
while True:
    P=int(input("you and"+F+" have entered a ruined town by zombies you both see a labrotary fully surrounded by zombies. Now you and"+F+" need to enter the labratory you see a coat covered in blood inside the pocket you see a scientific compass. Now for what do you use the compass for (Enter The Value for doing a specified task) 1 for act like zombies and enter the labratory and 2 for digging where the compass needle starts spinning"))
    if P!=2:
        Q=("the zombies can smell you so you got caught and died.GAME OVER")
        print(Q)
        P=0
    if P==2:
        break
R=("Great you had a shovel with you now you and"+F+" see a secret labratory tunnel.")
print(R)
print("You and"+F+" have found a antidote to the zombie.")
print("SUCESSFULLY COMPLETED THE GAME. THANK YOU FOR PLAYING")
print("Creators:")
print("Story Developers: Ashwin")
print("Code Developers: Malyadri,Mohith,Alan")
print("Helpers: Nitin,Eric")
