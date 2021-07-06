import random

up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num= ['0','1','2','3','4','5','6','7','8','9']
sp = ["!","@","#","$","%","^","&"]

passw = random.choice(up)+random.choice(lo)+random.choice(sp)+random.choice(lo)+random.choice(num)+random.choice(num)+random.choice(up)+random.choice(sp)

print(passw)
