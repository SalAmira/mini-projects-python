import  secrets
import random
import array
len_password=int(12)


Capital_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Small_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Numbers=['1','2','3','4','5','6','7','8','9']
Sympols=['#','@','&','_','-','.','%','?','$']


rand_Capital_letters=random.choice(Capital_letters)
rand_Small_letters=random.choice(Small_letters)
rand_Numbers=random.choice(Numbers)
rand_Sympols=random.choice(Sympols)

temp_pass = rand_Capital_letters+rand_Small_letters+rand_Numbers+rand_Sympols

for x in range(len_password):
    temp_pass=temp_pass+random.choice(temp_pass)
    temp_pass_list=array.array('u',temp_pass)
    random.shuffle(temp_pass_list)#The shffle method, it recorganizes the order of items of a sequance(list,tuple...).
    password=" "
for x in temp_pass_list:
        password=password+x
print(password)



