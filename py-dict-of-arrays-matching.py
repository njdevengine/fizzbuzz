people = {100:["Bob","Ace","Faizon","Nimrod","Abe"],
          101:["Qood","Lorza"],
          102:["Salazar","Will","Abbey","Abaloney"]}

database = {1:["Jimmy","Quazir","Nimrod","Abaloney","Positron","Abe"],
            2:["Quid","Qood","Food"],
            3:["Bob","Alize","Alice","Lorenzo"]}
            
for a in people:
    for b in people[a]:
        for c in database:
            for d in database[c]:
                if b == d:
                    print(b,d)       
#RETURNS:
#Bob Bob
#Nimrod Nimrod
#Abe Abe
#Qood Qood
#Abaloney Abaloney
