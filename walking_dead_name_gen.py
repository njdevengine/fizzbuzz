import string
import random

vowels = ["a","e","i","o","u","y"]
alpha = list(string.ascii_lowercase)

names = []
for i in alpha:
    if i not in vowels:
        names.append(i+"arl")
        names.append(i+"arril")
last_names = []

for i in alpha:
    if i not in vowels:
        last_names.append(i+"ixon")
        last_names.append(i+"ackson")
        
a = random.choice(names).title()
b = random.choice(last_names).title()
print(a,b)

#alternatively, get all unique choices into master list
master = []        
for i in range(20000):
    a = random.choice(names).title()
    b = random.choice(last_names).title()
    full_name = a+" "+b
    master.append(full_name)
    
master = list(set(list(master)))
print(random.choice(master))
