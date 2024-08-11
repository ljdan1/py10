import random

letter = ['A','B','C','D','E','F','G','H','I','J','K','L',
'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z']

number = ['0','1','2','3','4','5','6','7','8','9']

special_symbol = ['!','@','#','$','%','^','&','*']

print("----------------------------------------------------------")


input_letter = int(input("how many letters you want in your password:"))
input_number = int(input("how many numbers you want to add in your password:"))
input_special_symbol = int(input("how many special symbols you want ro add to your password:"))

password_list =[]

for char in range(1,input_letter+1):
    password_list.append(random.choice(letter))

for num in range(1,input_number+1):
    password_list.append(random.choice(number))
    
for symbol in range(1,input_special_symbol+1):
    password_list.append(random.choice(special_symbol))
   
print(password_list)


password = ""
for char in password_list:
    password = password + char 
print("generated password is ",password)
