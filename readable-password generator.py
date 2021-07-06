import random

wordlist = []
sp = ["!","@","#","$","%","^","&"]

with open('C:\\Users\\ROEDY\\Desktop\\practice\\PasswordGenerator\\wiki.txt','r') as file:
    data = file.readlines()

    for line in data:
        words = line.split()

        for item in words:
            if len(item) > 5 :
                wordlist.append(item.capitalize())

word = random.choice(wordlist)
schar = random.choice(sp)
num = str(random.randint(10,99))

passw = word+schar+num

print(passw)