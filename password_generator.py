import random
import string
print("Welcome to our Random Password Generator")
length=int(input("Enter the length of Password you want: "))
lowerD=string.ascii_lowercase
upperD=string.ascii_uppercase
digitD=string.digits
symbolsD=string.punctuation
combine=lowerD+upperD+symbolsD+digitD
x=random.sample(combine,length)
password="".join(x)
print(f"your password is : {password}")


