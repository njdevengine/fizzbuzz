string = """your email Cc: email@chain.com; <you@email.com>;"""
array = string.split(";")

for i in range(len(array)):
    array[i] = array[i].replace('<','').replace('To: ','').replace('>','').replace('Cc: ','')
    
new = []
for i in array:
    new.append(i.split(" "))
    
for i in range(len(new)):
    if new[i][0] == '':
        new[i] = new[i][1:]
    else:
        pass
        
for i in new:
    if "filter word" not in i[-1]:
        print(i[-1].lower()+"*"+(' ').join(i[:-1]))
