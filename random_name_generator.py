import random
#test is an array of fullnames

fname = []
lname = []
for i in test:
    try:
        fname.append(i.split(" ")[0])
        lname.append(i.split(" ")[1])
    except: pass

random.choice(fname)+" "+random.choice(lname)
