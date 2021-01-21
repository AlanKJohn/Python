maths=int(input("enter your marks for maths"))
history=int(input("enter your marks for history"))
physic=int(input("enter  your marks for physics"))
biology=int(input("enter marks for biology "))
geography=int(input("enter marks for geography"))
chemistry=int(input("enter marks for chemistry"))
english_language=int(input("enter marks for english language"))
english_literature=int(input("enter marks for english literature"))
computer=int(input("enter marks for computer"))
hindi=int(input("enter your marks for hindi"))
print("now we are calculating your total percentage")
X = maths + history + biology + geography + physic + chemistry + hindi + english_language + english_literature + computer 
Y=X/200*100
print("your total percentage is ",Y)
