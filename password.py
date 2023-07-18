import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters=(int(input("How many letters do u need?\n")))
nr_numbers=(int(input("How many numbers do u need?\n")))
nr_symbols=(int(input("How many symbols do u need?\n")))



password_list=[]
# storing random letters to password_list
for i in range(1,nr_letters+1):
    password_list+=random.choice(letters)
    
# storing random numbers to password_list    
for i in range(1,nr_numbers+1):
    password_list+=random.choice(numbers)
    
#  storing random symbols to password_list   
for i in range(1,nr_symbols+1):
    password_list+=random.choice(symbols)
    
print(password_list)



# printing password as a shuffled list
random.shuffle(password_list)
print(password_list)



# printing password as a single string
password=""
for i in password_list:
    password+=i
print(password)








