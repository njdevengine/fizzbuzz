#goal is to create an algorithm that goes through an array and concatenates, WITHOUT join
#puts alphabet into an array
ray =[]
array1 = (string.ascii_lowercase)
for i in array1:
    ray.append(i)
    
#['a','b','c'...'z']
    
array_length = len(ray)-1
for i in range (1,array_length):
    ray[0] = ray[0]+ray[i]

#ray[0] is now 'abcdefg...'
