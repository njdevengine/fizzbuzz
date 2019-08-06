#get alphabet as a list
import string
alpha = list(string.ascii_lowercase)

#divide length by 2 and convert to closest int
length = int(len(alpha)/2)

for i in range(length):
    print(alpha[i])
    
for i in range(length,len(alpha)):
    print(alpha[i])
