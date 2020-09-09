#given user input of a company name, return the top 3 most common letters

string = input("your company name: ")

array = sorted(string)
unique = list(set(string))
counts = []
for i in unique:
    count = 0
    for letter in array:
        if letter == i:
            count+=1
    counts.append(count)
    
rank = []
for check in reversed(range(max(counts)+1)):
    for i in range(len(counts)):
        if counts[i] == check:
            rank.append(unique[i])
            
top_3 = rank[:3]
for i in top_3:
    print(i)
